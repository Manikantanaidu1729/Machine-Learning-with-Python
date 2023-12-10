def display():
    a=20 # local and global to the inner function
    def show():
        print(f"1 : {a}")
    show()
display()
def display1():
    a=20 # local and global to the inner function
    def show():
        global a  # this keyword is used for only to convert local variable to global variable
                  # global variable means out of the upper function variables
        a=a+1 # local
        print(f"2 : {a}")  # it produces error because there is no global variable "a", so we can't access that variable
    show()
display1()

# we can access global variable in a function, but we can't modify it until we can change this variable to global variable like by adding global keyword