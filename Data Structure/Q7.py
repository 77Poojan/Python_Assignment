words = ["red", "white", "black","red","green","black"]
longest_word = max(words, key=lambda s: (len(s), s))
print(longest_word)
print(len(longest_word))