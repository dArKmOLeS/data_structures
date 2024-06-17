#--------------------------------------------------------------------------------------
#Code by :- Anmol Kumar Srivastava (dArKmOLeS)
#--------------------------------------------------------------------------------------
def bubble_sort_asc(array):
    length = len(array)
    for i in range(length):
        swapped = False #variable to maintain if swapping occured in iteration
        for j in range(length - i - 1):
            if array[j] > array[j+1]: #comparison 
                array[j], array[j+1] = array[j+1], array[j] #swapping
                swapped = True
        if not swapped: #if no swapping happened in entire iteration
            break #array sorted [early exit]

def bubble_sort_dsc(array):
    length = len(array)
    for i in range(length):
        swapped = False #variable to maintain if swapping occured in iteration
        for j in range(length - i - 1):
            if array[j] < array[j+1]: #comparison 
                array[j], array[j+1] = array[j+1], array[j]#swapping
                swapped = True
        if not swapped: #if no swapping happened in entire iteration
            break #array sorted [early exit]

def starter_code(): #starter code for calling all functions and printing result
    array = [1, 4, 2, 7, 5, 9, 3] #the array to be worked on
    print(f"The entered array is : {array}")
    array1 = array.copy() #copy of array to keep the array intact
    bubble_sort_asc(array1) #calling bubble_sort_asc() [in-place sorting is performed]
    print(f"The sorted array is [Ascending order]: {array1}")
    array2 = array.copy()#copy of array to keep the array intact
    bubble_sort_dsc(array2) #calling bubble_sort_dsc() [in-place sorting is performed]
    print(f"The sorted array is [Descending order]: {array2}")

starter_code() #calling starter_code() function
