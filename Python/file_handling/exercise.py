with open("student_marks.csv","r") as f:
    print(f.read())

    # creating dictionary
    f.seek(0)  # goto the start again
    # print(f.read())
    d={}
    keys=f.readline()
    print(keys)
    keys=keys.split(",")
    print(keys)

    # initializing the dictionary
    for key in keys:
        d[key]=[]
    print(d)

    # adding the data to the dictionary
    for line in f.readlines():
        data=line.split(",")
        j=0
        for i in d:
            d[i].append(data[j])
            j+=1
    print(d)

    import pprint
    pprint.pprint(d)
    print(d.values())

    # calculating the total marks
    d["Total Marks"] = [0]*5
    print(d["Total Marks"])
    
    for i in range(5):
        for key in d:
            try:
                d["Total Marks"][i] += int(d[key][i])
            except:
                pass
    print(d["Total Marks"])

# note
    print(int("76\n"))