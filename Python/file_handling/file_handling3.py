
# w+ is open for both reading and writing
# wb+ is open for both reading and writing in binary mode
# a+ is open for both reading and appending
# ab+ is open for both reading and appending in binary mode

player_scores={}

with open("scores.csv","r") as f:
    for line in f:
        player, score = line.split(",")
        score=int(score)
        if player in player_scores:
            player_scores[player].append(score)
        else:
            player_scores[player]=list()
            player_scores[player].append(score)
print(player_scores)

for player, score_list in player_scores.items():
    min_score=min(score_list)
    max_score=max(score_list)
    avg_score=sum(score_list)/len(score_list)

    print(f"{player} ==> min: {min_score}, max: {max_score}, avg: {avg_score}")

di={"m":3}
print(di)



with open("funny.txt","r") as f:
    for line in f:
        print(f"1... {f.readlines()}")

with open("funny.txt","r") as f:
    print(f"2... {f.readlines()}")

with open("funny.txt","r") as f:
    for line in f:
        print(f"3... {f.readline()}")

with open("funny.txt","r") as f:
    print(f"4... {f.readline()}")


with open("funny.txt","r") as f:
    for line in f:
        print(f"5... {f.read()}")

with open("funny.txt","r") as f:
    print(f"6... {f.read()}")


with open("funny.txt","r") as f:
    for line in f:
        print(line)

# f.read() will print the all data at a time
# f.readline() will print the one line at a time
# f.readlines() will print the all lines one by one