import datetime
class CricketPlayer:
    def __init__(self,fname,lname,team,birth_year):
        self.first_name=fname
        self.last_name=lname
        self.birth_year=birth_year
        self.team=team
        self.scores=[]

    def get_age(self):
        now=datetime.datetime.now()
        return now.year-self.birth_year

    def add_score(self,score):
        if type(score)!="int":
            for i in score:
                self.scores.append(i)
        else:
            self.scores.append(score)

    def get_score(self):
        return self.scores

    def get_average_score(self):
        return sum(self.scores)/len(self.scores)

    def __str__(self):
        return f"{self.first_name} {self.last_name} is the cricket player for {self.team}"

    def __lt__(self, other):
        my_score=self.get_average_score()
        other_score=other.get_average_score()
        return my_score<other_score


virat=CricketPlayer("virat","kohli","india",1988)
david=CricketPlayer("david","warner","austrlia",1986)

print(virat.first_name)
print(virat.get_age())
virat.add_score([30,40,50,60])
david.add_score([34,63,66,34])
print(virat.get_score())
print(david.get_score())
print(virat.get_average_score())
print(virat<david)
print(virat)

