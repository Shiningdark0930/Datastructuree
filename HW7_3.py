input_string = "This is a more advanced comprehension exercise to practice"

reversed_words = [word[::-1] for word in input_string.split() if len(word) > 5]

print(reversed_words)