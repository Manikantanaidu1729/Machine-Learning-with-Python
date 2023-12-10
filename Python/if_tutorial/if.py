indian = ["samosa", "daal", "naan"]
chinese = ["egg role", "pot sticker", "fried rice"]
italian = ["pizza", "pasta", "risotto"]
dish = input("Enter the dish name: ")
if dish in indian:
    print(f"{dish} is indian")
elif dish in chinese:
    print(f"{dish} is chinese")
elif dish in italian:
    print(f"{dish} is italian")
else:
    print("I don't know which cuisine is this!")


n = input("Enter a number: ")
n = int(n)
message = "Number is Even" if n % 2 == 0 else "Number is odd"
print(message)


# exercise
# 1).
height = int(input("Enter height: "))
weight = int(input("Enter weight: "))
BMI= weight/height
if BMI>=30:
    print("Obesity")
elif BMI>25 and BMI<29:
    print("Overweight")
elif BMI>18.5 and BMI<25:
    print("Normal")
elif BMI<18.5:
    print("Underweight")
else:
    print("NO category")

# 2).
India = ["Mumbai", "Bangalore", "Chennai", "Delhi"]
USA = ["New York","Chicago","Las Vegas", "San Francisco"]
UK = ["London", "Manchester", "Liverpool", "Nottingham"]
city_name=input("enter city name: ")
if city_name in India:
    print(f"{city_name} belongs to India")
elif city_name in USA:
    print(f"{city_name} belongs to USA")
elif city_name in UK:
    print(f"{city_name} belongs to UK")
else:
    print(f"{city_name} doesn't belongs to any country in my list")

# 3).

list = input("Enter two city names seperated by comma: ").split(",")
if list[0] in India and list[1] in India:
    print("Both cities are in India")
if list[0] in USA and list[1] in USA:
    print("Both cities are in USA")
if list[0] in UK and list[1] in UK:
    print("Both cities are in UK")
else:
    print("They don't belong to the same country")