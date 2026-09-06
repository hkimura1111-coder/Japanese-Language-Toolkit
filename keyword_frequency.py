text = input("Enter keywords separated by spaces: ")
keywords = text.split()
counts = {}

for keyword in keywords:
    if keyword not in counts:
        counts[keyword] = 1
    else:
        counts[keyword] += 1

print("Keyword frequencies:")
for keyword in counts:
    print(keyword, ":", counts[keyword])
    
highest = 0
top_keyword = ""

for keyword in counts:
    if counts[keyword] > highest:
        highest = counts[keyword]
        top_keyword = keyword
print()
print("Top keyword:", top_keyword)
print("Frequency:", highest)

highest = 0
top_keyword = ""

for keyword in counts:
    if counts[keyword] > highest:
        highest = counts[keyword]
        top_keyword = keyword

print()
print("Most common keyword:", top_keyword)
print("Frequency:", highest)