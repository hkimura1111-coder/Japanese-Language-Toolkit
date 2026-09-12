text = input("Enter text: ")
words = text.lower().split()
print(words)

positive_words = [
"love",
"great",
"good",
"excellent",
"happy"
]

negative_words = [
"hate",
"bad",
"terrible",
"awful",
"sad"
]

positive_score = 0
negative_score = 0

for word in words:
    if word in positive_words:
        positive_score = positive_score + 1
    if word in negative_words:
        negative_score = negative_score + 1

print("Positive score:", positive_score)
print("Negative score:", negative_score)

if positive_score > negative_score:
    print("Sentiment: Positive")

elif negative_score > positive_score:
    print("Sentiment: Negative")

else:
    print("Sentiment: Neutral")