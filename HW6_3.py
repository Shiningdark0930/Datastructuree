text = "This is a more advanced comprehension exercise to practice"

print([word[::-1] for word in text.split() if len(word) >= 5])