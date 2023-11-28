# Import the os module to access environment variables
import os

# Set the environment variables using os.environ
os.environ["PATH"] = "C:\\Python\\Scripts"
os.environ["PYTHONPATH"] = "C:\\Python\\Lib"

# Import the subprocess module to run commands
import subprocess

# Run the pip install command to install the dependencies
subprocess.run(["pip", "install", "-r", "requirements.txt"])
