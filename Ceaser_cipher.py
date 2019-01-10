import string

def string_to_list(string):
    list = []
    for letter in string:
        list.append(letter)
    return list

def list_to_string(list):
    string = ""
    for letters in list:
        string += letters
    return string

list_letters = string_to_list(string.ascii_letters)
list_letters.append(' ')


word = input("Enter a word to encrypt: ")
word_list = string_to_list(word)
print(word_list)

# converts characters in word_list to their index numbers
index_letters = []
for a in word_list:
    b = list_letters.index(a)
    index_letters.append(b)
print(index_letters)

key = input("enter a number for an encryption key: ")

'''
creates new index numbers by adding a key number to each of the original index
numbers
'''
new_index_numbers = []
for d in index_letters:
    d += int(key)
    new_index_numbers.append(d)

# corrects for letters that are at the end of the list
a_new_index = []
for y in new_index_numbers:
  if y > len(list_letters):
    y -= 53
    a_new_index.append(y)
  else:
    a_new_index.append(y)

new_message = []
for number in a_new_index:
    b = list_letters[number]
    new_message.append(b)

encrypted_message = list_to_string(new_message)
print("Your encrypted message is: " + encrypted_message)
