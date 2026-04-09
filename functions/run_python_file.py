import os
import subprocess
def run_python_file(working_directory, file_path, args=None):
    working_dir_abs = os.path.abspath(working_directory)
    target_file = os.path.normpath(os.path.join(working_dir_abs, file_path))
    # Will be True or False
    valid_file_path = os.path.commonpath([working_dir_abs, target_file]) == working_dir_abs
    if not valid_file_path:
        return f'Error: Cannot execute "{file_path}" as it is outside the permitted working directory'
    if not os.path.isfile(target_file):
        return f'Error: "{file_path}" does not exist or is not a regular file'
    if not file_path.endswith(".py"):
        return f'Error: "{file_path}" is not a Python file'
    # Assuming all those checks passed, we're going to use a subprocess to run the file. But first we need to build the command to run - in the form
    # of a list of strings. Start with something like this:
    # command = ["python", absolute_file_path]
    command = ["python", target_file]
    try:
        # If there are any args, we need to add those to the command list as well
        if args:
            command.extend(args)
        result = subprocess.run(command, cwd=working_dir_abs, capture_output=True, text=True, timeout=30)
        if result.returncode != 0:
            return f"Error: process exited with code {result.returncode}"
        if not result.stdout and not result.stderr:
            return "No output produced"
        else:
            return f"STDOUT: {result.stdout} STDERR: {result.stderr}"
    except Exception as e:
        return f'Error: {str(e)}'
    # Build an output string based on the CompletedProcess object:
    # if the process exited with a non-zero returncode, include "Process exited with coded X"
    # if both stdout and stderr contained no output (both of which are attributes of CompletedProcess), add "No output produced"
    # otherwise, include any text in stdout prefixed with STDOUT:, and any text in stderr prefixed with STDERR:

    
