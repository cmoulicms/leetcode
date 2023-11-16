my_dictionary = {
    "name": "Alice",
    "age": 25,
    "grade": "A",
    "courses": ["Math", "Science", "History"],
}

# print(my_dictionary['name'])
# print(my_dictionary.keys())
# print(my_dictionary.items())
# for key,items in my_dictionary.items():
#     print(key)
#     print(items)

# print(my_dictionary.keys()) # get list of keys
# print("name" in my_dictionary.keys()) # or print("name" in my_dictionary) check key exists
# print("A" in my_dictionary.values()) # or check value exists
# print(my_dictionary['courses']) # get values from dictionary using key
# print(my_dictionary.values()) # get list of values
# print(my_dictionary.items()) # get list of tuples with key and value
x = "Alice"
if x in my_dictionary:
    print(my_dictionary[x])
text = "This is a sample text. This text is used for illustration."
# one pass hash table
word_count = {}
words = text.split()
for word in words:
    if word in word_count:
        word_count[word] = word_count[word] + 1
    else:
        word_count[word] = 1

print(word_count)
# two pass hash table
# most_common_word = max(word_count, key=word_count.get)

print("Most Common Word (Two-Pass):")
# print(f"{most_common_word}: {word_count[most_common_word]} times")
