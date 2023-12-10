expenses=[1200,1300,100,1700]
total_expenses=0
for i in expenses:
    total_expenses+=i
print(total_expenses)

for i in range(len(expenses)):
    print(f"Month {i+1} Expense = {expenses[i]}")

for i, expense in enumerate(expenses, start=0):
    print(f"Month {i+1} Expense = {expense}")


for i, expense in enumerate(expenses, start=0):
    if expense>2000:
        print(f"Month {i+1} has expense > 2000")
        break

locations = ["sofa","garage","chair","table","closet"]
key_location = "chair"
for location in locations:
    if location==key_location:
        print("Key is found at ",location)
        break
    else:
        print("Key is not found at ", location)


for i in range(11):
    if i % 2 ==0:
        continue
    print(i)

lst = range(11)
n=0
while n<len(lst):
    print(lst[n])
    n+=2


# exercise
# 1)
for i in range(5,0,-1):
    for j in range(1,i+1):
            print(j,end=" ")
    print()


# 2)
sum=0
n=1
while n<=20:
    if n%2==0:
        sum+=n
    n+=1
print(sum)

# 3)
dice_result  = [5,6,4,2,5,4,4,5,3,3,2,6,1,2,1,1,6,5]
count_6=0
count_1=0
for i in dice_result:
    if i==6:
        count_6+=1
    elif i==1:
        count_1+=1
print(f"count_6= {count_6}, count_1= {count_1}")

two_6s = 0
l = len(dice_result)
for i in range(l - 1):
    if dice_result[i] == 6 and dice_result[i+1] == 6:
        two_6s += 1
print(f"count_6_two_times= {two_6s}")