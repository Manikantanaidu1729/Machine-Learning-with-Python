a,b=5,6
if a<b:
    c=a+b # here variable "c" acts like global variable
    # so we can access it out of the if statement
    # not only if. for,while these also
print(c)

def display():
    if a < b:
        d = a + b # here variable "d" acts like local variable because it is inside the funtion
print(d)