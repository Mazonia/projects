def pig_latin(text):
    pig_latin_text = ""
    # Separate the text into words
    words = text.split()
    for word in words:
        # Create the pig latin word and add it to the list
        if word.isalpha():  # Check if word only contains letters
            first_letter = word[0]
            pig_latin_word = word[1:] + first_letter + "ay"
        else:
            pig_latin_word = word  # Keep non-alphabetic words unchanged
        # Add the pig latin word to the string
        pig_latin_text += pig_latin_word + " "
        # Turn the list back into a phrase
    return pig_latin_text[:-1]


print(pig_latin("hello how are you"))  # Should be "ellohay owhay reaay ouyay"
print(pig_latin("programming in python is fun"))  # Should be "rogrammingpay niay ythonpay siay unfay"