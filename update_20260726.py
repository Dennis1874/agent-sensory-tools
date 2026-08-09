#!/usr/bin/env python3
import os
import json
import urllib.request
import urllib.error

TOKEN = os.environ.get("GITHUB_TOKEN", "GITHUB_TOKEN_PLACEHOLDER")
REPO = "Dennis1874/agent-sensory-tools"
API = f"https://api.github.com/repos/{REPO}"
HEADERS = {
    "Authorization": f"token {TOKEN}",
    "Accept": "application/vnd.github.v3+json",
    "User-Agent": "agent-sensory-tools-bot"
}

def api_request(method, url, data=None):
    if data:
        data = json.dumps(data).encode("utf-8")
    req = urllib.request.Request(url, data=data, headers=HEADERS, method=method)
    try:
        with urllib.request.urlopen(req) as resp:
            return json.loads(resp.read().decode("utf-8"))
    except urllib.error.HTTPError as e:
        body = e.read().decode("utf-8")
        print(f"HTTP Error {e.code}: {body}")
        return None

# Get main branch ref
ref = api_request("GET", f"{API}/git/ref/heads/main")
if not ref:
    print("Failed to get main ref")
    exit(1)
main_sha = ref["object"]["sha"]
print(f"Main SHA: {main_sha}")

# Get commit
commit = api_request("GET", f"{API}/git/commits/{main_sha}")
tree_sha = commit["tree"]["sha"]
print(f"Tree SHA: {tree_sha}")

# Files to update
base_dir = "/app/data/所有对话/主对话/agent-sensory-tools"
files = [
    "README.md",
    "categories/vision/README.md",
    "categories/code-awareness/README.md",
    "categories/web-data/README.md",
    "categories/file-document/README.md",
    "categories/execution/README.md",
    "categories/monitoring/README.md",
]

# Create blobs
tree_entries = []
for fp in files:
    full_path = os.path.join(base_dir, fp)
    with open(full_path, "r") as f:
        content = f.read()
    blob = api_request("POST", f"{API}/git/blobs", {"content": content, "encoding": "utf-8"})
    if blob:
        tree_entries.append({"path": fp, "mode": "100644", "type": "blob", "sha": blob["sha"]})
        print(f"  Blob: {fp} -> {blob['sha'][:8]}")

# Create tree
new_tree = api_request("POST", f"{API}/git/trees", {"base_tree": tree_sha, "tree": tree_entries})
if not new_tree:
    print("Failed to create tree")
    exit(1)
new_tree_sha = new_tree["sha"]
print(f"New tree: {new_tree_sha}")

# Create commit
msg = "weekly update: 2026-07-26 - 新增9个工具 (Stealth Browser MCP/Vessel Browser/Codebase Memory MCP/Google Workspace MCP/NotebookLM MCP/Markdownify MCP/Talonic MCP/OpenWorker/MCP Memory Service)"
new_commit = api_request("POST", f"{API}/git/commits", {
    "message": msg,
    "tree": new_tree_sha,
    "parents": [main_sha]
})
if not new_commit:
    print("Failed to create commit")
    exit(1)
new_commit_sha = new_commit["sha"]
print(f"New commit: {new_commit_sha}")

# Update ref
result = api_request("PATCH", f"{API}/git/refs/heads/main", {"sha": new_commit_sha})
if result:
    print(f"\n✅ Successfully pushed: {msg}")
    print(f"   URL: https://github.com/{REPO}/commit/{new_commit_sha}")
else:
    print("\n❌ Failed to update ref")
