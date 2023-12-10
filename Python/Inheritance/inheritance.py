import datetime


class Player:
    def __init__(self, fname, lname, birth_year):
        self.first_name = fname
        self.last_name = lname
        self.birthyear = birth_year

    def get_age(self):
        now = datetime.datetime.now()
        return now.year - self.birthyear


class CricketPlayer(Player):
    def __init__(self, fname, lname, birth_year, team):
        Player.__init__(self,fname, lname, birth_year)
        self.team = team
        self.scores = []

    def add_scores(self, score):
        self.scores.append((score))

    def get_average_score(self):
        return sum(self.scores) / len(self.scores)


virat = CricketPlayer("virat", "kohli", 1988, "india")
virat.add_scores(37)
virat.add_scores(23)
virat.add_scores(85)

print(virat.get_age())
print(virat.get_average_score())