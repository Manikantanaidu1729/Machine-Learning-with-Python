a=10  # global
def display():
    print(f"1 : {a}")  # local
display()

def display1():
    a=15 # local
    print(f"2 : {a}")
display1()

"""
def display2():
    a=a+1   # it produces error because here a is local variable, it doesn't have any value, but we have global variable outside a=10
              # here the solution is to make this local variable as global variable then this local variable a can have value 10, then it updates
              # the solution is next function follows 
    print(f"2 : {a}")
display2()
"""

def display2():
    global a
    a=a+1 # local
    print(f"2 : {a}")
display2()