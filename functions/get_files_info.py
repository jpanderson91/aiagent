import os
def get_files_info(working_directory, directory="."):
    working_dir_abs = os.path.abspath(working_directory)
    target_dir = os.path.normpath(os.path.join(working_dir_abs, directory))
    # Will be True or False
    valid_target_dir = os.path.commonpath([working_dir_abs, target_dir]) == working_dir_abs
    if not valid_target_dir:
        return f'Error: Cannot list "{directory}" as it is outside the permitted working directory'
    if not directory:
        return f'Error: "{directory}" is not a directory'
    # iterate over the items in the target directory. For each of them, record the name, file size, and whether it's a directory itself.
    # Use this data to build and return a string representing the contents of the target directory. It should be in the following format:
    # - README.md: file_size=1032 bytes, is_dir=False
    # - src: file_size=128 bytes, is_dir=True
    # - package.json: file_size=1234 bytes, is_dir=False
    try:
        items = os.listdir(target_dir)
        info_lines = []
        for item in items:
            item_path = os.path.join(target_dir, item)
            file_size = os.path.getsize(item_path)
            is_dir = os.path.isdir(item_path)
            info_lines.append(f'- {item}: file_size={file_size} bytes, is_dir={is_dir}')
        return '\n'.join(info_lines)
    except Exception as e:
        return f'Error: {str(e)}'
    
    