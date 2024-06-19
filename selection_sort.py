#-------------------------------------------------------------------------------
# Anmol Kumar Srivastava (dArKmOLeS)
#-------------------------------------------------------------------------------
def selection_sort_asc(array):
    for i in range(len(array) - 1): # 0 - second last element (last element auto sorted)
        minimum = i # let first element of array be the smallest
        for j in range(i+1, len(array)): # i+1 to last element comparison (elements till i already sorted)
            if array[minimum] > array[j]:
                minimum = j 
        array[minimum], array[i] = array[i], array[minimum] # swap elements
    return array


def selection_sort_dsc(array):
    for i in range(len(array) - 1): # 0 - second last element (last element auto sorted)
        maximum = i # let first element of array be the largest
        for j in range(i+1, len(array)): # i+1 to last element comparison (elements till i already sorted)
            if array[maximum] < array[j]:
                maximum = j 
        array[maximum], array[i] = array[i], array[maximum] # swap elements
    return array
            
    
def starter_code():
    array = [6, 1, 4, 2, 7, 9, 5, 8]
    print(f"The guven array is : {array}")
    array1 = array.copy()
    print("The sorted array in ascending order is : ", selection_sort_asc(array1))
    array2 = array.copy()
    print("The sorted array in descending order is : ", selection_sort_dsc(array2))


starter_code()
