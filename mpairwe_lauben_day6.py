# error handling
#Exception handling with try, except, else and finally
#custom exceptions
"""_summary_

    Error handling in python helps to handle unexpected situations and errors.
    Try contains code that might throw an exception
    if an exception occurs the rest of the code in the try block is skipped or ignored
    
    Except catches and handles exceptions
    You can specify different handlers to different exception types
    
    Else : the code runs if no exception occurs
    if no  exceptions are raised in try block it runs.
    finally: codes runs exclusively regardless of exception occurence or not . used 4 cleaning up actions
"""
# Handle exceptions with division by zero
try:
    number = int(input('Enter a number:'))
    result = 20 / number
except ValueError:
    print('Enter a valid number')
except ZeroDivisionError:
    print('Division by zero not allowed')
else:
    print(f'Result is {result}')
finally:
    print('Execution completed successfully')


def convert_to_integer():
    try:
        # Get input from the user
        value = input('Enter a value to convert to integer: ')
        # Attempt to convert the value to an integer
        result = int(value)
    except ValueError:
        # Handle the case where the string cannot be converted to an integer
        print('Error: The provided string cannot be converted to an integer.')
    except TypeError:
        # Handle the case where the input is not a string
        print('Error: The provided input is not a string.')
    else:
        # Execute this block if no exceptions are raised
        print(f'The converted integer is: {result}')
    finally:
        # This block will always execute
        print('Execution completed.')

# case usage
convert_to_integer()



#custom exception handling
class InsufficientFundsError(Exception):
    def __init__(self, balance, amount):
        self.balance = balance
        self.amount = amount
        self.message = f"Attempt to withdraw {self.amount} with only {self.balance} in account"
        super().__init__(self.message)

def withdraw(balance, amount):
    if amount > balance:
        raise InsufficientFundsError(balance, amount)
    return balance - amount

# Custom exception handling
try:
    balance = 20000
    amount_to_withdraw = 100000
    new_balance = withdraw(balance, amount_to_withdraw)
except InsufficientFundsError as e:
    print(f'Error: {e.message}. New balance: {balance}')
else:
    print('Withdrawal successful')
finally:
    print('Transaction completed')

    """_summary_
    class CustomError(Exception):
    def __init__(self, message)
       super().__init__message
       ### raising custom exception
       def check_value(value):
       if value is < 0
    """
# Exercise 2   create a custom exception InvalidAgeError and write a function that raises 
# this exception if the given age is negative. handle this custom exception when calling the function.    

class InvalidAgeError(Exception):
    def __init__(self, age):
        self.age = age
        self.message = f"Invalid age: {self.age}. Age cannot be negative."
        super().__init__(self.message)

def check_age(age):
    if age < 0:
        raise InvalidAgeError(age)
    print(f"Age is valid: {age}")

# Custom exception handling
try:
    age = int(input("Enter your age: "))
    check_age(age)
except InvalidAgeError as e:
    print(f"Error: {e.message}")
finally:
    print("Age validation completed!!")
