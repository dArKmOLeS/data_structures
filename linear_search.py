def linear_search(array, target): #function defination of linear search
    index = -1 #setting -1 index as element not found
    for i in range(len(array)): #for loop to check each element
        if array[i] == target: #comparing list element with target value
            index = i #setting index value
            break #exit loop when element found
    return index #return index
        
    
def is_integer(target): #function defination of is_integer function
    try: #try block for exception handling
        int(target) #explicitly changing target to integer for validation
        return True #if integer, return True
    except ValueError: #condition of exception occurs
        return False #return False
    


array = [1, 2, 3, 4, 5, 6, 7, 8, 9, 10, 20, 30, 40, 50, 60, 70, 80, 90, 100] #list 
while True: #loop for getting valid integer input from user
    target = input("Enter the element to search : ") #target value for searching in list
    if is_integer(target): #condition for valid integer input
        index = linear_search(array, int(target)) #calling linear search function
        if index != -1: #condition for element found
            print("The element is present at index : ", index) #printing output
        else: #condition for element not found
            print("The element not found in list.") #printing output
        break #leaving the while loop
    else: #condition for invalid input
        print("Only integers allowed.") #printing error
