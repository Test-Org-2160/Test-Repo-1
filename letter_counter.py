def count_letters(word):
    if word.isalpha():
        letter_count = 0
        for letter in word:
            letter_count += 1
        return(letter_count)
    else:
        raise ValueError("You didn't enter a word :/")
