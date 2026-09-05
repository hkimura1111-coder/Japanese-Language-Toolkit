files = ["file1.txt", "file2.txt", "file3.txt"]

    
for filename in files:
    with open(filename, "r", encoding="utf-8") as file:
        text = file.read().strip()
        
        counts = {}

    for character in text:
        if character not in counts:
            counts[character] = 1
        else:
            counts[character] = counts[character] + 1
        
        highest = 0
        most_common = ""

    for character in counts:
        if counts[character] > highest:
            highest = counts[character]
            most_common = character
            
    print(filename)
    print("Total characters:", len(text))
    print("Unique characters:", len(counts))
    print("Most common character:", most_common)
    print("Frequency:", highest)
    print("--------------------")
    print()