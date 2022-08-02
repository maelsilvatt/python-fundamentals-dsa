# To make it easier to add more words, I created a script that
# filters the selected string to find words and tips pairs
# Make sure to keep the following format
# word tip\n

# Importing 'findall' to filter strings into list of outputs
from re import findall

# Your word tips pair text goes here
text = """
abs()	Returns the absolute value of a number
all()	Returns True if all items in an iterable object are true
any()	Returns True if any item in an iterable object is true
"""

# Applies a filter on text to find all pairs
word_tip_pairs = findall(r'[^\(\)\n\t]+', text)

# Converts the filtered pairs into dictionary of strings
list = []
counter = 0
i = 0
for counter in range(len(word_tip_pairs) // 2):
    list.append('{' + f'"{word_tip_pairs[i]}"' + ':' + f'"{word_tip_pairs[i + 1]}"' + '}')
    i += 2


# Writes the resulting dictionary on 'words.txt'
with open('words.txt', 'a') as file:
    file.write(', '.join(list).replace(', ', '\n'))
