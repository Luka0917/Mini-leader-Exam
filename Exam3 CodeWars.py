# 8kyu

# Reversed Words

def reverse_words(s):
    s = s.split(" ")
    return " ".join(s[::-1])

# Total amount of points

def points(games):
    result = 0
    for i in games:
        if i[0] > i[2]:
            result += 3
        elif i[0] == i[2]:
            result += 1
        else:
            result += 0
    return result