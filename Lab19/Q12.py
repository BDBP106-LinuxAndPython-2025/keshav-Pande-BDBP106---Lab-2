string = "Hello, how are you?"
vowels = list(filter(lambda ch: ch.lower() in 'aeiou', string))
print(vowels)
