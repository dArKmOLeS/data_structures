#--------------------------------------------------------------------------------------
#Code by :- Anmol Kumar Srivastava (dArKmOLeS)
#--------------------------------------------------------------------------------------
def find_max(array): #finds the largest number
    max_number = array[0] #let first element be the largest
    for i in array[1:]: #traverse array from 2nd element
        if i > max_number: #if current element is greater than supposed largest
            max_number = i #update largest
    return max_number


def find_min(array): #finds the smallest number
    min_number = array[0] #let first element be the smallest
    for i in array[1:]: #traverse array from 2nd element
        if i < min_number: #if current element is lower than supposed smallest
            min_number = i #update smallest
    return min_number


def check_empty(array): #check if array is empty or not 
    return len(array)==0 #if array length is 0, returns True, otherwise False
    
    
def starter_code():
    array = [11,23,34,1,45,22,13,50,45,3,46] #array declaration
    if check_empty(array):
        print("The given array is empty.") #array is empty
    else:
        max_number = find_max(array) #find_max() call
        min_number = find_min(array) #find_min() call
        print(f"The largest number in the array is : {max_number}") #print result
        print(f"The smallest number in the array is : {min_number}") #print result
 

starter_code() #start the code
