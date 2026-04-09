import os
import subprocess
from google import genai  # type: ignore
from google.genai import types  # type: ignore

schema_run_python_file = types.FunctionDeclaration(
    name="run_python_file",
    description="Executes a Python file as a subprocess and returns its output. Use this when the user asks to run, execute, or test a Python script",
    parameters=types.Schema(
        type=types.Type.OBJECT,
        properties={
            "file_path": types.Schema(
                type=types.Type.STRING,
                description="Path to the Python file to execute, relative to the working directory",
            ),
            "args": types.Schema(
                type=types.Type.ARRAY,
                items=types.Schema(type=types.Type.STRING),
                description="Optional list of command-line arguments to pass to the script",
            ),
        },
        required=["file_path"],
    ),
)

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

    
