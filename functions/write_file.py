import os
from google import genai  # type: ignore
from google.genai import types  # type: ignore

schema_write_file = types.FunctionDeclaration(
    name="write_file",
    description="Writes content to a specified file relative to the working directory, creating parent directories as needed",
    parameters=types.Schema(
        type=types.Type.OBJECT,
        properties={
            "file_path": types.Schema(
                type=types.Type.STRING,
                description="Path to the file to write, relative to the working directory",
            ),
            "content": types.Schema(
                type=types.Type.STRING,
                description="Content to write to the file",
            ),
        },
        required=["file_path", "content"],
    ),
)

def write_file(working_directory, file_path, content):
    # if the file_path is outside the working_directory, return an error string  like the one below:
    # f'Error: Cannot write to "{file_path}" as it is outside the permitted working directory'
    working_dir_abs = os.path.abspath(working_directory)
    target_file = os.path.normpath(os.path.join(working_dir_abs, file_path))
    valid_target_file = os.path.commonpath([working_dir_abs, target_file]) == working_dir_abs
    if not valid_target_file:
        return f'Error: Cannot write to "{file_path}" as it is outside the permitted working directory'
    # if the file_path points to an existing directory (this is what os.path.isdir() checks for), 
    # return an error string:
    # f'Error: Cannot write to "{file_path}" as it is a directory'
    if os.path.isdir(target_file):
        return f'Error: Cannot write to "{file_path}" as it is a directory'
    # make sure that all parent directories of the file_path exist. You can use os.makedirs() with the
    # exists+ok=True argument to create any missing directories. If the necessary directory structure already exists,
    # this will do nothing - which is what we want.
    os.makedirs(os.path.dirname(target_file), exist_ok=True)
    # open the file at file_path in write mode ("w") and overwrite its contents with the content argument.
    # if everything succeeds return a string with the following message:
    # f'Successfully wrote to "{file_path}" ({len(content)} characters written)'
    try:
        with open(target_file, 'w') as f:
            f.write(content)
        return f'Successfully wrote to "{file_path}" ({len(content)} characters written)'
        
    except Exception as e:
        return f'Error: {str(e)}'
        
                               
