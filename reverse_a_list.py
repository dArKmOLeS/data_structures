def reversed_keyword(array):
    array = list(reversed(array))
    print(f"Using reversed() function : {array}")

def reverse_keyword(array):
    array.reverse()
    print(f"Using reverse() function : {array}")
       
def reverse_using_double_pointer_approach(array):
    length = len(array)
    for i in range(length // 2):
        temp = array[i]
        array[i] = array[length - i - 1]
        array[length - i - 1] = temp
    print(f"Using 2-pointer approach : {array}")
    
def reverse_by_new_list(array):
    reverse_list = []
    length = len(array)
    for i in range(-1, -length - 1, -1):
        reverse_list.append(array[i])
    array = reverse_list.copy()
    print(f"Using another list : {array}")
    
def starter_code():
    array = [1, 2, 3, 4, 5, 6, 7, 8, 9, 0]
    array1 = array.copy()
    array2 = array.copy()
    array3 = array.copy()
    array4 = array.copy()
    reversed_keyword(array1)
    reverse_keyword(array2)
    reverse_using_double_pointer_approach(array3)
    reverse_by_new_list(array4)
    
starter_code()
