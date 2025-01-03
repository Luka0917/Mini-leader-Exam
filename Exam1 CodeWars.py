# 6kyu

# Stop gninnipS My sdroW!

def spin_words(sentence):
    result = []
    sentence = sentence.split()
    for i in sentence:
        if len(i) >= 5:
            result.append(i[::-1])
        else:
            result.append(i)
    return " ".join(result)