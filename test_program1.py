word = input("Enter a word to count it's letters: ")
if word.isalpha():
    letter_count_dict = dict()
    for letter in word:
        if letter not in letter_count_dict:
            letter_count_dict[letter] = 1
        else: 
            letter_count_dict[letter] += 1
    print(letter_count_dict)
else:
    raise ValueError("You didn't enter a word :/")
