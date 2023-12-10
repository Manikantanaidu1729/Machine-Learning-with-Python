with open("scores.csv","r") as f:
    rohit_s=[]
    shakib_s=[]
    babar_s=[]
    for line in f:
        list=line.split(",")
        if list[0]=="rohit":
            rohit_s.append(int(list[1][:-1]))
        elif list[0]=="shakib":
            shakib_s.append(int(list[1][:-1]))
        elif list[0]=="babar":
            babar_s.append(int(list[1][:-1]))
        else:
            pass

def cal(lst):
    return min(lst),max(lst),sum(lst)/len(lst)

print(f"rohit min max avg score = {cal(rohit_s)}")

print(f"shakib min max avg score = {cal(shakib_s)}")

print(f"babar min max avg score = {cal(babar_s)}")




