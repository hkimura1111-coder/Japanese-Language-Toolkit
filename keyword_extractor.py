text = input("Enter text: ")
stop_words = [
"the",
"is",
"a",
"and",
"for",
"with"
]
words = text.split()
counts = {}

for word in words:
    if word not in stop_words:
        if word not in counts:
            counts[word] = 1
        else:
            counts[word] = counts[word] + 1
print("Keywords:")

for word in counts:
    print(word, ":", counts[word])

highest = 0
top_keyword = ""
for word in counts:
    if counts[word] > highest:
        highest = counts[word]
        top_keyword = word
print()
print("Top keyword:", top_keyword)
print("Frequency:", highest)
