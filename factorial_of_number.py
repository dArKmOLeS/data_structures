#--------------------------------------------------------------------------------------
#Code by :- Anmol Kumar Srivastava (dArKmOLeS)
#--------------------------------------------------------------------------------------
def is_valid_integer(number):
    try:
        int(number)
        return True
    except ValueError:
        return False
        
def factorial_using_loop(number):
    if number == 0:
        return 1
    factorial = 1
    for i in range(1, number + 1):
        factorial *= i
    return factorial

def factorial_using_recursion(number):
    if number == 0:
        return 1
    return number * factorial_using_recursion(number - 1)
    
def starter_code():
    while True:
        number = input("Enter number to check it's factorial : ")
        if is_valid_integer(number) and int(number) >= 0:
            number = int(number)
            print(f"Factorial using loop : {factorial_using_loop(number)}")
            print(f"factorial using recursion : {factorial_using_recursion(number)}")
            break
        else:
            print("Enter a valid choice [Integer].")
            
starter_code()
