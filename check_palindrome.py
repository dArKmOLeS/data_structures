def str_slice_check(string): #reverses the string using string slicing for comparison
    return string == string[::-1]

def comparison_check(string): #compares individual elements of the string 
    length = len(string)
    for i in range(length // 2): #matches half the string with the other half 
        if string[i] != string[length - i - 1]:
            return False
    return True
    
def list_reverse(string): #uses list() and reversed() functions for comparison
    return list(string) == list(reversed(string))
    
def starter_code():
    string = input("Enter string to check for palindrome : ")
    print(f"Is Palindrome : {str_slice_check(string)}")
    print(f"Is Palindrome : {comparison_check(string)}")
    print(f"Is Palindrome : {list_reverse(string)}")
    
starter_code()
