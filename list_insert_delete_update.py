#------------------------------------------------------------------------------------------
#Anmol Kumar Srivastava (dArKmOLeS)
#------------------------------------------------------------------------------------------
def is_valid_integer(value): #checks if input is integer or not 
    try:
        int(value)
        return True
    except ValueError:
        return False

def print_array(array): #prints array 
    if is_empty(array): #condition for empty array
        print("Empty array.")
    else:
        for index, value in enumerate(array):
            print(value, end = "-") #prints hypen separated array
        print("End")
    
def is_empty(array): #checks if array is empty
    return len(array) == 0

def clean_up_code(): #has the exiting code 
    print("Exiting Program.\nHave a good day.")

def insert(array, value, index): #inserts element at the given position in the array
    if len(array) == 0 or index == len(array): #first or last position
        array.append(value)
    else: #insert in middle
        i = len(array)
        array.append(0) #add extra element
        while i > index:
            array[i] = array[i-1] #from position, update all elements by shifting them
            i-=1
        array[index] = value #insert final value
        
def insert_in_array(array):
    value = input("Enter the value to be inserted : ")
    print("length of array is : ", len(array))
    while True:
        index = input("Enter the index for the element : ")
        if is_valid_integer(index):
            index = int(index)
            if index in range(len(array)+1): #insertion only at available places
                insert(array, value, index)
                break
            else:
                print("Index out of array range.")
        else:
            print("enter a valid choice (INTEGER).")          

def update_in_array(array): #update a element in array
    while True:
        index = input("Enter the index to update it's value : ")
        if is_valid_integer(index):
            index = int(index)
            if index < len(array): #validation index to be in list
                value = input("Enter value to be updated : ")
                array[index] = value
                break
            else:
                print("Array index out of range.")
        else:
            print("enter a valid choice (INTEGER).")  

def delete_from_array(array): #deleting from array
    value = input("Enter element to be deleted : ")
    if value not in array: #element not found
        print("Element not present in array.")
    else: #element found
        index = array.index(value) #accessing its index
        for i in range(index, len(array)-1):
            array[i] = array[i+1] #shift all non-deleted elements
        array.pop() #remove on element from the last
    
def starter_code(): #start up code
    array = []
    while True:
        print("Press 1 to insert in array.\nPress 2 to delete from array.\nPress 3 to update a value.\nPress 4 to print the array.\nPress 5 to exit.")
        choice  = input("Enter your choice : ")
        if is_valid_integer(choice) and choice in ["1", "2", "3", "4", "5"]:
            if choice == "1":
                insert_in_array(array)
                print_array(array)
            elif choice == "2":
                delete_from_array(array)
                print_array(array)
            elif choice == "3":
                update_in_array(array)
                print_array(array)
            elif choice == "4":
                print("The array is : ", end=" ")
                print_array(array)
            else:
                clean_up_code()
                break
        else:
            print("Enter a valid choice (INTEGER).")
        
starter_code()
                   
