with open("sample_txt") as sample_txt:
    contents = sample_txt.readlines()
    contents = str(contents)


contents = contents.lower().replace(".", " ").replace(",", " ").replace("!", " ").replace(";", " ")\
    .replace("'", " ").replace('"', ' ').replace("*", " ").replace("" " ", " ").replace("-", " ")\
    .replace("?", " ").replace(" ?", " ").replace("\\n", " ").replace("\\", " ")

contents = contents.split()

histogram = {}


for word in set(contents):
    histogram[word] = contents.count(word)

def value_sort(val):
    return val[1]

list_values_sorted = sorted(histogram.items(), key=value_sort, reverse=True)
list_values_sorted_20 = list_values_sorted[:20]
print(list_values_sorted_20)
