"""
Create a dictionary with key value pairs to
represent words (key) and its definition (value)
"""
word_definitions = dict()

"""
Add several more words and their definitions
   Example: word_definitions["Awesome"] = "The feeling of students when they are learning Python"
"""
word_definitions["whaaaaaaatttttttt"] = "My reaction when reading about slice not needing slice"
word_definitions["quuuuuueeeeeeeeee"] = "My reaction when getting an explanation of slice"
word_definitions["Black Box"] = "where .slice() should be"
"""
Use square bracket lookup to get the definition of two
words and output them to the console with `print()`
"""
print(word_definitions["whaaaaaaatttttttt"])
print(word_definitions["quuuuuueeeeeeeeee"])

"""
Loop over the dictionary to get the following output:
    The definition of [WORD] is [DEFINITION]
    The definition of [WORD] is [DEFINITION]
    The definition of [WORD] is [DEFINITION]
"""
for (word, definition) in word_definitions.items():
    print(f"The definition of {word} is {definition}")
