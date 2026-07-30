import difflib


# Loading word database

with open("words.txt", "r") as file:
    words = file.read().splitlines()


# Autocomplete function

def autocomplete(word):

    suggestions = []

    for w in words:
        if w.startswith(word.lower()):
            suggestions.append(w)

    return suggestions[:5]


# Autocorrect function

def autocorrect(word):

    matches = difflib.get_close_matches(
        word,
        words,
        n=3,
        cutoff=0.6
    )

    return matches



# User Input

text = input("Enter a word: ")


print("\nAutocomplete Suggestions:")

result = autocomplete(text)

if result:
    for word in result:
        print(word)
else:
    print("No suggestions found")



print("\nAutocorrect Suggestions:")

corrected = autocorrect(text)

if corrected:
    for word in corrected:
        print(word)
else:
    print("No corrections found")



# Save Output

with open("output.txt","w") as file:

    file.write("Autocomplete and Autocorrect System\n")
    file.write("--------------------------------\n\n")

    file.write("Input Word: " + text + "\n\n")

    file.write("Autocomplete Suggestions:\n")

    for item in result:
        file.write(item + "\n")


    file.write("\nAutocorrect Suggestions:\n")

    for item in corrected:
        file.write(item + "\n")


print("\nProcess Completed Successfully!")
