'''
This programme could be used to track issues, milestones and commits related to them and create an automated report for a github repository

Guidelines:
- Install Github CLI from https://cli.github.com/
- Open a terminal and use: "gh auth login"
- Replace REPO value in line 11 with your own
- Run the python file in a terminal
'''

import subprocess
import json
import sys
from datetime import datetime

# -----------------------------
# CONFIGURATION
# -----------------------------
REPO = "OWNER/REPO"
ISSUE_LIMIT = 100 
OUTPUT_FILE = "Project_Progress_Report.md"

def run(cmd):
    try:
        result = subprocess.check_output(cmd, shell=True, stderr=subprocess.STDOUT)
        return result.decode()
    except subprocess.CalledProcessError:
        return ""

# -----------------------------
# DATA EXTRACTION
# -----------------------------
print(f"Extracting Engineering Data from {REPO}...")

issues_raw = run(
    f'gh issue list -R {REPO} --state closed --limit {ISSUE_LIMIT} '
    '--json number,title,body,createdAt,closedAt,milestone'
)

issues = json.loads(issues_raw) if issues_raw.strip() else []
issues.sort(key=lambda x: x['number']) # Ascending order

# -----------------------------
# REPORT GENERATION
# -----------------------------
with open(OUTPUT_FILE, "w", encoding="utf-8") as f:
    # 1. Formal Header
    f.write(f"# Project Technical Development Progress Report\n")
    f.write(f"**Repository:** `{REPO}`  \n")
    f.write(f"**Date Generated:** {datetime.now().strftime('%Y-%m-%d %H:%M %p')}  \n\n")
    f.write("---\n\n")

    # 2. Executive Summary
    f.write("## 1. Executive Summary\n")
    milestone_stats = {}
    for i in issues:
        m = i.get("milestone")
        m_title = m.get("title") if m else "General Development"
        milestone_stats[m_title] = milestone_stats.get(m_title, 0) + 1

    f.write(f"**Overall Status:** {len(issues)} Tasks Completed  \n\n")
    f.write("| Milestone Phase | Tasks Completed |\n")
    f.write("| :--- | :---: |\n")
    
    for m_name, count in milestone_stats.items():
        f.write(f"| {m_name} | {count} |\n")
    f.write("\n")

    # 3. Task Inventory
    f.write("## 2. Technical Task Index\n")
    f.write("| Ref | Milestone | Task Title | Completion Date |\n")
    f.write("| :--- | :--- | :--- | :--- |\n")
    for issue in issues:
        m = issue.get("milestone")
        m_title = m.get("title") if m else "---"
        closed_date = issue['closedAt'][:10] if issue['closedAt'] else "N/A"
        f.write(f"| #{issue['number']} | {m_title} | [{issue['title']}](#task-{issue['number']}) | {closed_date} |\n")
    
    f.write("\n---\n\n")

    # 4. Detailed Engineering Logs
    f.write("## 3. Detailed Engineering Logs\n\n")

    for issue in issues:
        num = issue.get("number")
        m = issue.get("milestone")
        m_title = m.get("title") if m else "Unassigned"
        
        f.write(f"### <a name='task-{num}'></a> Issue #{num}: {issue.get('title')}\n")
        f.write(f"**Milestone Alignment:** `{m_title}`  \n")
        f.write(f"**Cycle:** {issue['createdAt'][:10]} to {issue['closedAt'][:10]}  \n\n")
        
        f.write(f"**Technical Objectives:** \n")
        f.write(f"> {issue.get('body', '').strip() or 'No technical documentation provided.'}\n\n")

        # Fetch PR & Commits with Datetime
        detail_raw = run(f'gh issue view {num} -R {REPO} --json closedByPullRequestsReferences')
        pr_refs = json.loads(detail_raw).get("closedByPullRequestsReferences", []) if detail_raw else []

        if pr_refs:
            for pr_ref in pr_refs:
                pr_num = pr_ref.get("number")
                pr_raw = run(f'gh pr view {pr_num} -R {REPO} --json commits,title')
                pr = json.loads(pr_raw) if pr_raw else {}

                f.write(f"**Implementation Source:** Pull Request #{pr_num}  \n")
                f.write("| Timestamp | Contributor | Revision | Commit Message |\n")
                f.write("| :--- | :--- | :--- | :--- |\n")
                
                for c in pr.get("commits", []):
                    sha = c.get("oid")[:7]
                    msg = c.get("messageHeadline")
                    # Formatting Datetime
                    raw_date = c.get("committedDate", "Unknown")
                    fmt_date = raw_date.replace("T", " ").replace("Z", "")[:16] # YYYY-MM-DD HH:MM
                    
                    # Contributor identification
                    auth_data = c.get("author", {})
                    user_handle = auth_data.get("user", {}).get("login") if auth_data.get("user") else None
                    git_name = auth_data.get("name", "Unknown")
                    author = f"@{user_handle}" if user_handle else git_name
                    
                    f.write(f"| {fmt_date} | **{author}** | `{sha}` | {msg} |\n")
                f.write("\n")
        else:
            f.write("*Note: Task resolution managed via direct repository updates.*\n\n")
        f.write("---\n\n")

print(f"✅ Professional Technical Report successfully generated: {OUTPUT_FILE}")