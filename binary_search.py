#--------------------------------------------------------------------------------------
#Code by :- Anmol Kumar Srivastava (dArKmOLeS)
#--------------------------------------------------------------------------------------
def valid_integer(target): #checks for valid integer input
    try:
        int(target)
        return True
    except ValueError:
        return False

def binary_search(min, max, target, array): #binary search
    if min <= max: 
        mid = min//2 + (max - max//2) #calculating mid in this way so that min+max doesn't overflow the memory
        if array[mid] > target:
            return binary_search(min, mid-1, target, array)
        elif array[mid] < target:
            return binary_search(mid+1, max, target, array)
        else:
            return mid #element found
    else:
        return -1 #element not found
    
def starter_code(): #start_up code
    array = [2,4,5,6,7,9,10] #array declaration
    while True: #infinite loop for valid inputs
        target = input("Enter the target value : ")
        if valid_integer(target):
            index = binary_search(0, len(array) - 1, int(target), array) #calling the binary search fucr
            if index == -1:
                print("Element not found in array.") #result printing
            else:
                print(f"Element found at index number {index}") #result printing
            break
        else:
            print("Invalid input, Only integer values.") #invalid type message

starter_code()
