import os

# List of scripts to run in order
scripts = ["FirstScript.py", "SecondScript.py", "ForthScript.py", "ThirdScript.py"]

# Get the directory where this script is located
current_directory = os.path.dirname(os.path.abspath(__file__))

# Run each script in order
for script in scripts:
    script_path = os.path.join(current_directory, script)
    os.system(f"python {script_path}")
