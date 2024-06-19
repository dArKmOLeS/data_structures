#-------------------------------------------------------------------------------------------------------------
# Anmol Kumar Srivastava (dArKmOLeS)
#-------------------------------------------------------------------------------------------------------------
def reverse_string_iteration(string):
    reverse_string = "" # empty string
    for i in string:
        reverse_string = i + reverse_string # adding each element in front 
    return reverse_string


def reverse_string_slicing(string):
    reverse_string = string[::-1] # using string slicing to reverse the string
    return reverse_string
    
 
def reverse_string_list(string):
    string_list = [char for char in string] # changing the string to a list 
    string_list.reverse() # reverse() on list 
    return "".join(string_list) # list to string
     
  
def reverse_string_reversed(string):
    reverse_string = "".join(reversed(string)) # reversed() can be used to reverse any sequence 
    return reverse_string # then changing it to string (reversed() returns an iterator over the elements)


def starter_code():
    string = "12345678" # declare string
    print("string :", string)
    reverse_string0 = reverse_string_iteration(string) # function call
    print("Reverse of the string is :", reverse_string0)
    reverse_string1 = reverse_string_slicing(string) # function call
    print("Reverse of the string is :", reverse_string1)
    reverse_string2 = reverse_string_list(string) # function call
    print("Reverse of the string is :", reverse_string2)
    reverse_string3 = reverse_string_reversed(string) # function call
    print("Reverse of the string is :", reverse_string3)
   
    
starter_code()
