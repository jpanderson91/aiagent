import os
from functions.get_file_content import get_file_content
file_content = get_file_content("calculator", "lorem.txt")
#ensure that it truncates properly. don't need to print the entire content; just check the length and the truncation message at the end.
print(f"Length of content: {len(file_content)}")
main_content = get_file_content("calculator", "main.py")
print(main_content)
calc_content = get_file_content("calculator", "pkg/calculator.py")
print (calc_content)
bin_content = get_file_content("calculator", "/bin/cat")
print(bin_content)
error_test = get_file_content("calculator", "does_not_exist.py")
print(error_test)


