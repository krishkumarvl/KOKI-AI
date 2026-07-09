# brain/git_tool.py — Project KOKI
# "git commit X" sunke auto add + commit + push karta hai

import subprocess
import os

def git_commit(message: str, repo_path: str = ".") -> str:
    """
    Git add . → commit → push karta hai.
    message: commit message
    repo_path: project folder path (default current dir)
    """
    try:
        # git add .
        subprocess.run(
            ["git", "add", "."],
            cwd=repo_path,
            check=True,
            capture_output=True
        )

        # git commit
        subprocess.run(
            ["git", "commit", "-m", message],
            cwd=repo_path,
            check=True,
            capture_output=True
        )

        # git push
        subprocess.run(
            ["git", "push"],
            cwd=repo_path,
            check=True,
            capture_output=True
        )

        return f"✓ Committed and pushed: '{message}'"

    except subprocess.CalledProcessError as e:
        error = e.stderr.decode().strip() if e.stderr else "Unknown error"
        if "nothing to commit" in error:
            return "Kuch naya nahi hai commit karne ke liye."
        if "rejected" in error:
            return "Push reject ho gaya — pehle git pull karo."
        return f"Git error: {error}"

    except Exception as e:
        return f"Kuch ho gaya — {e}"