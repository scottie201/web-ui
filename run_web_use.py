import os
import subprocess

# Define the path to the script to be run
script_path = "/workspaces/assistant_container_dev/web-ui/tests/test_browser_use.py"

# Ensure the script exists
if os.path.exists(script_path):
    # Run the script
    subprocess.run(["python", script_path])
else:
    print(f"Error: The script at {script_path} does not exist.")
