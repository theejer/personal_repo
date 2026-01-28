tilesheet = []

for x in range(128):
    tilesheet.append([])
    for y in range(128):
        if x == 120:
            tilesheet[x].append("X")
        elif y == 20 and x < 120:
            tilesheet[x].append("X")
        elif x == 110 and y == 40:
            tilesheet[x].append("S")
        elif x == 115 and y > 20 and y < 60:
            tilesheet[x].append("P")
        else:
            tilesheet[x].append("")
print(tilesheet)