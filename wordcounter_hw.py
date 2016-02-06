from collections import Counter

with open("sample_txt") as sample_txt:
        contents = sample_txt.readline().lower().replace(".", " ").replace(","," ").replace("!"," ").replace(";"," ")\
        .replace("'", " ").replace("" " ", " ").replace("-", " ").replace("?", " ").replace(" ?" , " ").split(" ")

        unique_characters = set(contents)


histogram = {}

for word in unique_words:


unique_words =


word = {}
word_dict= Counter(word)

print(word_dict)




    #print(character, contents.count(character))





