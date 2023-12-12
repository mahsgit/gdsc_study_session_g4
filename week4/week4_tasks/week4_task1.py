'''Create a Python module (math_operations.py) with the following functionalities:

a. Basic Operations Function:

Create a function basic_operations that takes two numbers and performs basic arithmetic operations (addition, subtraction, multiplication, division). This function should return a dictionary with the results for each operation.

def basic_operations(a, b):
    # Perform basic arithmetic operations
    # Return results in a dictionary
'''



def basic_operations(a, b):
    try:
        add = a + b
        subtract= a - b
        multiply= a * b
        division = a / b
        return {'addition': add,'subtraction': subtract,'multiplication': multiply, 'division': division}
    except ZeroDivisionError:
        print("Error: Division by zero!")
    except Exception as e:
        print("Error:", str(e))
        
'''b. Power Operation Function:
Create a function power_operation that takes a base and an exponent and 
calculates the result of the power operation. Use the **kwargs feature to allow the user
to specify an optional modulo value. If the modulo value is provided, 
calculate the result modulo the specified value.

def power_operation(base, exponent, **kwargs):
    # Calculate power operation
    # If 'modulo' is provided in kwargs, calculate modulo
'''

def power_operation(base, exponent, **kwargs):
    try:
        result = base ** exponent
        if 'modulo' in kwargs:
            modulo = kwargs['modulo']
            result %= modulo
        return result
    except Exception as e:
        print("Error:", str(e))
        
'''c. Exception Handling:
Add appropriate exception handling in both functions to handle cases such as division by zero and invalid inputs.
In the same module, create a higher-order function apply_operations that takes a list of tuples, 
where each tuple contains a function and its corresponding arguments. Use map to apply each function
to its arguments and return a list of results.

def apply_operations(operation_list):
    # Use map to apply each function to its arguments
    # Return a list of results
'''       

def apply_operations(operation_list):
    try:
        results = list(map(lambda x: x[0](*x[1]), operation_list))
        return results
    except Exception as e:
        print("Error:", str(e))
    
    
    
