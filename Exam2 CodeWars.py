# 8kyu

# Century From Year

def century(year):
    return (year + 99) // 100

# Quarter of the year

def quarter_of(month):
    if month == 1 or month == 2 or month == 3:
        return 1
    elif month == 4 or month == 5 or month == 6:
        return 2
    elif month == 7 or month == 8 or month == 9:
        return 3
    elif month == 10 or month == 11 or month == 12:
        return 4
    
# 7kyu

# Number of People in the Bus

def number(bus_stops):
    get_on = []
    get_off = []
    for i in bus_stops:
        get_on.append(i[0])
        get_off.append(i[1])
    return sum(get_on) - sum(get_off)

# Alphabet war

def alphabet_war(fight):
    left_side = []
    right_side = []
    for i in range(fight.count("w")):
        left_side.append(4)
    for i in range(fight.count("p")):
        left_side.append(3)
    for i in range(fight.count("b")):
        left_side.append(2)
    for i in range(fight.count("s")):
        left_side.append(1)
            
    for i in range(fight.count("m")):
        right_side.append(4)
    for i in range(fight.count("q")):
        right_side.append(3)
    for i in range(fight.count("d")):
        right_side.append(2)
    for i in range(fight.count("z")):
        right_side.append(1)
    
    if sum(left_side) > sum(right_side):
        return "Left side wins!"
    elif sum(right_side) > sum(left_side):
        return "Right side wins!"
    else:
        return "Let's fight again!"