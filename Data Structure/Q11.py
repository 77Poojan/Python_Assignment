def count_occurance(str):
    counts = dict()
    words = str.split()

    for word in words:
        if word in counts:
            counts[word] += 1
        else:
            counts[word] = 1

    return counts

str = input("Enter your string: ")
print(count_occurance(str))