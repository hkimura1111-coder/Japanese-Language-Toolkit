
    
vocabulary = {
"犬": "dog",
"猫": "cat",
"鳥": "bird"
}
score = 0
for word in vocabulary:
    answer = input(word + " = ? ")
    
    if answer == vocabulary[word]:
        score = score + 1
        print("Correct!")
        print("Answer:", answer)
        print("Correct answer:", vocabulary[word])
          
    else:
        print("Wrong!")
        print("Correct answer:", vocabulary[word])
        
print("Final Score:", score, "/", len(vocabulary))