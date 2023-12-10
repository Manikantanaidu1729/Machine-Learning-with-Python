import math

# If no return statement is used inside the function,
# the function will always return the value: "None"

expenses_sergey=[30,45,70,90]
expenses_sundar=[40,23,10,85]

total=0
i=0
j=0
while i<len(expenses_sergey):
    while j<len(expenses_sundar):
        total=total+expenses_sundar[j]+expenses_sergey[i]
        i+=1
        j+=1
    break
print(f"total = {total}")

total=0
def find_total(expenses):
    '''
    This function takes expenses list as an input and return a total sum of that list
    :param expenses: list of input expenses
    :return: total expense
    '''
    total=0
    for expense in expenses:
        total+=expense
    return total

total=find_total(expenses_sergey)
print(f"expenses_surgery total= {total}")
total=find_total(expenses_sundar)
print(f"expenses_sundar total= {total}")

print(help(find_total))





#volume of the cylinder
r=5
h=10

def find_cylinder_volume(radius,height):
    print("radius: ",radius)
    print("height: ",height)
    volume = math.pi*(radius**2)*height
    return round(volume)

def find_cylinder_volume(radius,height=7):
    print("radius: ",radius)
    print("height: ",height)
    volume = math.pi*(radius**2)*height
    return round(volume)

volume = find_cylinder_volume(r,h)
print("volume: ",volume)


volume = find_cylinder_volume(height=h,radius=r)
print("volume: ",volume)

volume = find_cylinder_volume(r)
print("volume: ",volume)


# exercise
#1).
def to_check_prime_and_odd(number):
    prime=1
    prime_and_odd = 0
    for i in range(2,number):
        if number%i==0:
            prime=0
            break
    if prime==1 and number%2==1:
        prime_and_odd=1
    return prime_and_odd
print("it is prime and odd" if to_check_prime_and_odd(5)==1 else "nothing")

#2).
def pattern(n):
    if n%2==0:
        for i in range(n,0,-1):
            for j in range(i):
                print("*",end=" ")
            print()
    else:
        for i in range(n+1):
            for j in range(i):
                print("*",end=" ")
            print()

pattern(4)
pattern(3)

#3).
def master_yoda(string):
    list=string.split(" ")
    terminator = list[-1][-1]
    list[-1]=list[-1][:-1]
    list.reverse()
    joining = " ".join(list)
    master_yoda_string=joining+terminator
    return master_yoda_string

print(master_yoda("i am manikantanaidu."))

#4).
def pay_bill(expenses, offer_amount=None, percent_commission=0.098):
    # calculating the total bill amount
    total_bill_amount = 0
    for amount in expenses:
        total_bill_amount += amount

    # calculate extra commission percentage
    extra_commission = 0
    if offer_amount:
        if total_bill_amount >= offer_amount:
            extra_commission = 0.012
            print(f"Congratulations! You earned 1.2% extra commission.")

    # Calculate final payable amount
    commission_amount = total_bill_amount * (percent_commission + extra_commission)
    final_amount = total_bill_amount - commission_amount
    return final_amount


print(pay_bill([100,200,300,400,500]))
