print("==========================")
print("Japanese Language Toolkit")
print("==========================")


hiragana = "あいうえおかきくけこがぎぐげごさしすせそざじずぜぞたちつてとだぢづでどなにぬねのはひふへほばびぶべぼぱぴぷぺぽまみむめもやゆよらりるれろわをん"
kanji = "今日天気私"
katakana = "アイウエオカキクケコサシスセソタチツテトナニヌネノハヒフヘホマミムメモヤユヨラリルレロワヲン"
latin = "abcdefghijklmnopqrstuvwxyzABCDEFGHIJKLMNOPQRSTUVWXYZ"
numbers = "0123456789"

def analyze_text(text):
    print("\n===== Analysis =====\n")
    hiragana_count = 0
    kanji_count = 0
    katakana_count = 0
    latin_count = 0
    number_count = 0
    other_count = 0
    
    for character in text:
        if character in hiragana:
            print(character, "is Hiragana")
            hiragana_count = hiragana_count + 1
        elif character in katakana:
            print(character, "is Katakana")
            katakana_count = katakana_count + 1
        elif character in kanji:
            print(character, "is Kanji")
            kanji_count = kanji_count + 1
        elif character in latin:
            print(character, "is Latin Letter")
            latin_count = latin_count + 1
        elif character in numbers:
            print(character, "is Number")
            number_count = number_count + 1
        else:
            other_count = other_count + 1
    print("Hiragana count:", hiragana_count)
    print("Katakana count:", katakana_count)
    print("Kanji count:", kanji_count)
    print("latin count:", latin_count)
    print("number count:", number_count)
    print("other count:", other_count)
    print("Total characters:", len(text))
    
text = input("Enter Japanese text: ")
analyze_text(text)



