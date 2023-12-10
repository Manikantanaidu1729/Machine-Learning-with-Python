# creating the Avenger class
class Avenger:
    """Class to represent an Avenger"""

    def __init__(self, name, age, gender, superPower, weapon):
        self.name = name
        self.age = age
        self.gender = gender
        self.superPower = superPower
        self.weapon = weapon

        # is Leader
        self.isLeader = False

    def get_name(self):
        return self.name

    def get_age(self):
        return self.age

    def get_superpower(self):
        return self.superPower

    def get_info(self):
        return f"""
        Avenger Profile:

        Name:   {self.name}
        Age:    {self.age}
        Gender: {self.gender}

        Has {self.weapon} weapon and {self.superPower} super Power. 
        """

        # is leader function

    def is_leader(self):
        return self.isLeader

    def make_leader(self):
        self.isLeader = True
        return f"{self.name} is the new leader of the Avengers"

    def remove_leader(self):
        self.isLeader = False
        return f"{self.name} is removed from the leader"

    def __str__(self):
        return f"Avenger({self.name}, {self.age}, ...)"

Super_heroes = ['Captain America', 'Iron Man', 'Black Widow', 'Hulk', 'Thor', 'Hawkeye']
super_powers = ['Super strength', 'Technology', 'superhuman', 'Unlimited Strength', 'super Energy', 'fighting skills'] # from question
weapons = ["Shield", "Armor", "Batons", "No Weapon", "Mjölnir", "Bow and Arrows"]    #from question

# let's create a ages and gender list randomly
ages = [110, 40, 35, 34, 10000, 30]
genders = ['M', 'M', 'F', 'M', 'M', 'M']

# now create our avengers team using the data
avengers = []
for name, age, gender, power, weapon in zip(Super_heroes, ages, genders, super_powers, weapons):
    avengers.append(
        Avenger(name, age, gender, power, weapon)
    )


# print information
print(avengers[2].get_info())

# printing the information of Iron Man
for avenger in avengers:
    if avenger.get_name() == 'Iron Man':
        print(avenger.get_info())

avengers[5].get_superpower()
