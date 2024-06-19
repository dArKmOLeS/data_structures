#-------------------------------------------------------------------------------
# Anmol Kumar Srivastava (dArKmOLeS)
#-------------------------------------------------------------------------------
def reverse_string_recursion(string):
    if len(string) == 1: # base case
        return string
    return string[-1] + reverse_string_recursion(string[:-1]) # last of string plus function call for rest of string


def starter_code():
    string = "12345678" # declare string
    print("string :", string)
    reverse_string = reverse_string_recursion(string) # function call
    print("Reverse of the string is :", reverse_string)
   
    
starter_code()
