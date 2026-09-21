"""
Problem:
Implement a mini language that can parse a program and perform the appropriate
actions on a stack and register.

Input: program as a string
Output: print result of the program

Requirements:
- support the commands:
n: Place an integer value, n, in the register. Do not modify the stack.
PUSH : Push the current register value onto the stack. Leave the value in the register.
ADD : Pop a value from the stack and add it to the register value, storing the result in the register.
SUB : Pop a value from the stack and subtract it from the register value, storing the result in the register.
MULT : Pop a value from the stack and multiply it by the register value, storing the result in the register.
DIV : Pop a value from the stack and divide the register value by the popped stack value, storing the integer result back in the register.
REMAINDER : Pop a value from the stack and divide the register value by the popped stack value, storing the integer remainder of the division back in the register.
POP : Remove the topmost item from the stack and place it in the register.
PRINT : Print the register value.
- all operations are integer operations
- assume all programs are valid
- initialise the stack to `[]` and register to `0`

1. Initialise stack and register
2. Convert the program to a list
3. loop over the list and perform the function on the stack and register
    a. match the operation using match/case
    b. perform the op and assign the result to the register
    c. return the register (stack will be mutated)
"""

def minilang(program):
    stack = []
    register = 0

    operations = program.split()

    for op in operations:
        register = do_operation(op, stack, register)

def do_operation(op, stack, register):
    match op:
        case 'PUSH':
            do_push(stack, register)
        case 'ADD':
            register = do_add(stack, register)
        case 'SUB':
            register = do_sub(stack, register)
        case 'MULT':
            register = do_mult(stack, register)
        case 'DIV':
            register = do_div(stack, register)
        case 'REMAINDER':
            register = do_remainder(stack, register)
        case 'POP':
            register = do_pop(stack)
        case 'PRINT':
            do_print(register)
        case _:
            try:
                register = int(op)
            except ValueError:
                print(f"Invalid operation: {op}")

    return register

def do_push(stack, register):
    stack.append(register)

def do_add(stack, register):
    try:
        value = stack.pop()
        return value + register
    except IndexError:
        print("Error during ADD: stack empty")

def do_sub(stack, register):
    try:
        value = stack.pop()
        return register - value
    except IndexError:
        print("Error during SUB: stack empty")
    
def do_mult(stack, register):
    try:
        value = stack.pop()
        return register * value
    except IndexError:
        print("Error during MULT: stack empty")

def do_div(stack, register):
    try:
        value = stack.pop()
        return register // value
    except IndexError:
        print("Error during DIV: stack empty")

def do_remainder(stack, register):
    try:
        value = stack.pop()
        return register % value
    except IndexError:
        print("Error during REMAINDER: stack empty")

def do_pop(stack):
    try:
        return stack.pop()
    except IndexError:
        print("Error during POP: stack empty")

def do_print(value):
    print(value)

minilang('PRINT')
# 0

minilang('5 PUSH 3 MULT PRINT')
# 15

minilang('5 PRINT PUSH 3 PRINT ADD PRINT')
# 5
# 3
# 8

minilang('5 PUSH POP PRINT')
# 5

minilang('3 PUSH 4 PUSH 5 PUSH PRINT ADD PRINT POP PRINT ADD PRINT')
# 5
# 10
# 4
# 7

minilang('3 PUSH PUSH 7 DIV MULT PRINT')
# 6

minilang('4 PUSH PUSH 7 REMAINDER MULT PRINT')
# 12

minilang('-3 PUSH 5 SUB PRINT')
# 8

minilang('6 PUSH')
# (nothing is printed)

minilang('ADD')
# Error during ADD: stack empty

minilang('SUB')
# Error during SUB: stack empty

minilang('MULT')
# Error during MULT: stack empty

minilang('DIV')
# Error during DIV: stack empty

minilang('REMAINDER')
# Error during REMAINDER: stack empty

minilang('POP')
# Error during POP: stack empty

minilang('!@£')
# Invalid operation: !@£