import random
"open shuffled.csv which is the iris data and loop trough and shuffle the hole set 10 times "

for _ in range(10):
    fid = open("shuffled.csv", "r")
    li = fid.readlines()
    fid.close()
    print(li)

    random.shuffle(li)
    print(li)

    fid = open("shuffled.csv", "w")
    fid.writelines(li)
    fid.close()
