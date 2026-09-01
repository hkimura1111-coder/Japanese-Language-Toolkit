text = input("Enter words separated by spaces: ")
words = text.split()
counts = {}

for word in words:
    if word not in counts:
        counts[word] = 1
    else:
        counts[word] = counts[word] + 1

print("Word frequencies:")

for word in counts:
    print(word, ":", counts[word])
    
    highest = 0
most_common = ""

for word in counts:
    if counts[word] > highest:
        highest = counts[word]
        most_common = word
print()
print("Most common word:", most_common)
print("Frequency:", highest)

