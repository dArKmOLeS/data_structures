#--------------------------------------------------------------------------------------
#Code by :- Anmol Kumar Srivastava (dArKmOLeS)
#--------------------------------------------------------------------------------------
def is_valid_integer(target): #checks if input is integer or not
    try:
        int(target) 
        return True
    except ValueError:
        return False

def is_empty(array): #checks if array is empty or not
    return len(array)==0

def first_occurrence(target, array): #finds the first occurance of target in the list
    for index, value in enumerate(array): #enumerate for handling index and value pair
        if value == target:
            return index
    return -1
        
def starter_code(): #the main starter code
    array = [1,2,3,7,5,2,9,47,5,9,11,1,11] #list declaration
    if is_empty(array):
        print("List is empty.")
    else:
        while True:
            target = input("Enter a value to check its first occurance : ")
            if is_valid_integer(target):
                index = first_occurrence(int(target), array)
                if index == -1:
                    print("Element not in list.")
                else:
                    print(f"The first occurance is at index : {index}")
                break
            else:
                print("Enter a valid number (INTEGER).")
        
starter_code()
