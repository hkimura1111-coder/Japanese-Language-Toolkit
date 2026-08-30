text = input("Enter Japanese text: ")

counts = {}

for character in text:
    if character not in counts:
        counts[character] = 1
    else:
        counts[character] = counts[character] + 1 
        
highest = 0
most_common = ""
        
print("Total characters:", len(text))
print("Unique characters:", len(counts))
print()

print("Character frequencies:")

for character in counts:
    print(character, ":", counts[character])
    
print()    

for character in counts:
     if counts[character] > highest:
         highest = counts[character]
         most_common = character

print()
print("Most common character:", most_common)
print("Frequency:", highest)