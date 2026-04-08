# It should be similar in structure to the test modules that you've written for other functions. Include the following three test cases; as always, print the results of each:
# write_file("calculator", "lorem.txt", "wait, this isn't lorem ipsum")
# write_file("calculator", "pkg/morelorem.txt", "lorem ipsum dolor sit amet")
# write_file("calculator", "/tmp/temp.txt", "this should not be allowed")
from functions.write_file import write_file
def test_write_file():
    # Test case 1
    result1 = write_file("calculator", "lorem.txt", "wait, this isn't lorem ipsum")
    print(result1)
    
    # Test case 2
    result2 = write_file("calculator", "pkg/morelorem.txt", "lorem ipsum dolor sit amet")
    print(result2)
    
    # Test case 3
    result3 = write_file("calculator", "/tmp/temp.txt", "this should not be allowed")
    print(result3)


test_write_file()
