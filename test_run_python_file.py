from functions.run_python_file import run_python_file
def test_run_python_file():
    # Test case 1
    result1 = run_python_file("calculator", "main.py")
    print(result1)
    
    # Test case 2
    result2 = run_python_file("calculator", "main.py", ["3 + 5"])
    print(result2)
    
    # Test case 3
    result3 = run_python_file("calculator", "tests.py")
    print(result3)

    # Test case 4 should return error
    result4 = run_python_file("calculator", "../main.py")
    print(result4)
    
    # Test case 5 should return error
    result5 = run_python_file("calculator", "nonexistent.py")
    print(result5)
    
    # Test case 6 should return error
    result6 = run_python_file("calculator", "lorem.txt")
    print(result6)

test_run_python_file()
