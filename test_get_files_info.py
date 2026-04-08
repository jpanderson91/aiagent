# We need a way to manually debug our new get_files_info function. when test_get_files_info.py is executed directly (uv run test_get_files_info.py)
# it should run the following function calls and print the results matching the formatting below (not necessarily the exact numbers).
# get_files_info("calculator", "."):
# Result for current directoyr:
# - main.py: file_size=719 bytes, is_dir=False
# - tests.py: file_size=1331 bytes, is_dir=False
# - pkg: file_size=44 bytes, is_dir=True
# get_files_info("caculator", "pkg"):
# Results for 'pkg' directory:
# - calculator.py: file_size=1721 bytes, is_dir=False
# - render.py: file_size=376 bytes, is_dir=False
# get_files_info("calculator", "/bin"):
# Results for '/bin' directory:
# Error: Cannot list "/bin" as it is outside the permitted working directory
# get_files_info("calculator", "../"):
# Result for '../' directory:
# Error Cannot list "../" as it is outside the permitted working directory
import os
from get_files_info import get_files_info
current_dir_result = get_files_info("calculator", ".")
print(f"Results for current directory:\n{current_dir_result}")
pkg_dir_result = get_files_info("calculator", "pkg")
print(f"Results for 'pkg' directory:\n{pkg_dir_result}")    
bin_result = get_files_info("calculator", "/bin")
print(f"Results for '/bin' directory:\n{bin_result}")   
sub_dir_result = get_files_info("calculator", "../")
print(f"Results for '../' directory:\n{sub_dir_result}")


