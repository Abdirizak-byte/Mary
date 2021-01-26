
MaryFile = open("Mary.txt", "r")

Mary = MaryFile.readlines()
txt = Mary[2]
txt = txt.splitlines()
x = -1
for Mary in txt:
    for z in Mary.split():
        x = x + 1
        print(x, str(z))
MaryFile.close()
