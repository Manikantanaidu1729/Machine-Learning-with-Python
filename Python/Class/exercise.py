class Avenger:

    def __init__(self,na,ag,ge,pow,wea):
        self.name=na
        self.age=ag
        self.gender=ge
        self.super_power=pow
        self.weapon=wea

    def get_information(self):
        return f"information is {self.name}, {self.age}, {self.gender}, {self.super_power}, {self.weapon}"

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


super_heroes=["captain America","Iron Man","Black Widow","Hulk","Thor","Hawkeye"]
Weapons=["Shield","Armor","Batons","NO weapon for hulk","Mjolnir","Bow and Arrows"]
super_power=["Super strength","Techonolgy","superhuman","unlimited strength","super energy","fighting skills"]
Age=[23,75,67,34,42,25]
genders = ['M', 'M', 'F', 'M', 'M', 'M']

for i in range(len(super_heroes)):
    super_heroes[i] = Avenger(super_heroes[i],Age[i],genders[i],super_power[i],Weapons[i])
    print(super_heroes[i].get_information())
    print(super_heroes[i])
    print()
