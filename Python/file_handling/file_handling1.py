f=open("funny.txt","r")
for line in f:
    print(line)
f.close()

with open("love.txt","r") as f:
    for line in f:
        print(line)

with open("love.txt","r") as f:
    lines = f.readlines()
    print(lines)

with open("love.txt","w") as f:
    f.writelines(["i love cake \n ","i love coke"])
    f.write("dskhbsdbf")

with open("love.txt","a") as f:
    f.write("\n dshfbdsjfd")