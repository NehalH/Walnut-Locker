import subprocess
import re
import os

script_dir = os.path.dirname(os.path.abspath(__file__))

# path to the lock file
lockfiles_path = os.path.join(script_dir, "data", "lockfile.txt")

# path to the Unlock.py script
unlock_script_path = os.path.join(script_dir, "grant.py")

def run_grant_script(filepath):
    # Read the lockfiles.txt file to get the list of locked file paths
    with open(lockfiles_path, 'r') as lockfile:
        locked_files = lockfile.read().splitlines()

    # Check if the accessed file path is in the locked files list
    if filepath in locked_files:
        # Perform actions for granted access (e.g., run the `grant.py` script)
        subprocess.call(['python3', 'grant.py', unlock_script_path])

# Set up audit rules to capture open system calls for file access
options = "-a exit,always -F arch=b64 -S open"
auditctl_command = f"auditctl {options}"

# Run the auditctl command to set up the audit rules
subprocess.call(auditctl_command, shell=True)

# Enter a loop to read auditd output and detect file access events
with subprocess.Popen(['auditd', '-f'], stdout=subprocess.PIPE, bufsize=1, universal_newlines=True) as proc:
    for line in proc.stdout:
        # Check if the line contains the 'file-access' keyword
        if 'file-access' in line:
            # Extract the file path from the line using regular expressions
            match = re.search(r"obj=(.*?)[\s|,]", line)
            if match:
                filepath = match.group(1)
                # Run the grant script for locked file paths
                run_grant_script(filepath)
