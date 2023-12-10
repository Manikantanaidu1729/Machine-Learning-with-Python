
contacts = [("mani",352383767556),("kanta",246462624625),("naidu",8567489678783)]
for contact in contacts:
    if contact[0]=="naidu":
        print(contact[1])

# dictionary is a key-value pair
dict = {
    "mani":352383767556,
    "kanta":246462624625,
    "naidu":8567489678783
}

print(dict)
print(dict.values())  # output is list
print(dict.keys())   # output is list
print(dict.get("mani"))
print(dict["mani"])

print(dict.get("mani",465873))

print(dict.get("mohan",465873))

print(dict)
dict["mani"]=9381498272


dict["bujji"]="845"
print(dict)

print("mani" in dict)


dict1 = {
    "mani":{"phone no":43543653463,"address":"hyd"},
    "kanta":{"phone no":5464684564,"address":"dr valasa"}
}

print(dict1["mani"]["address"])

for name in dict:
    print(name,end=" ")
    print(dict[name],end=" ")
    print()

print(dict)
print(dict.items())

for name, phone_no in dict.items():
    print(name, end=" ")
    print(phone_no, end=" ")
    print()



# exercise
#1).
d = {
  "Luke": 1994,
  "Boba": 1989,
  "Kyle": 1998,
  "Hann": 1993
}
# print(d["Boba": "Kyle"])  # it raises an error

#2).
my_expenses = {}
wife_expenses = {}

# adding data to the dictionaries
my_expenses['Clothes'] = 100
my_expenses['Shoes'] = 1000
my_expenses['Watch'] = 900
my_expenses['Mobile Recharge'] = 699
my_expenses['Petrol'] = 1980

wife_expenses.update({
    "Mobile Recharge" : 799,
    "DTH recharge" : 999,
    "Clothes" : 2310,
    "Makeup" : 3670,
    "Shoes" : 999
})

my_amount=0
my_wife_amount=0
for thing, amount in my_expenses.items():
    my_amount+=amount

for thing, amount in wife_expenses.items():
    my_wife_amount+=amount

print(f"my amount is {my_amount} and my wife amount is {my_wife_amount}")

if my_amount>my_wife_amount:
    print("I am spending more")
elif my_amount<my_wife_amount:
    print("my wife spending more")
else:
    print("together spending same amount")

item = " "
money = 0
def my_exp(my):
    global item, money
    for thing, amount in my.items():
        if amount > money:
            money = amount
            item = thing
    return item

def my_wife_exp(my_wife):
    global money, item
    for thing, amount in my_wife.items():
        if amount > money:
            money = amount
            item = thing
    return item

print(f"my expensive thing is {my_exp(my_expenses)}")
print(f"my wife expensive thing is {my_wife_exp(wife_expenses)}")

#3).

def tuple(list):
    list1=[]
    for friend in list:
        new_tupel=(friend,len(friend))
        list1.append(new_tupel)
    return list1

list=["mani","ramu","r.k.","tadella","sesikala","guna"]
print(tuple(list))