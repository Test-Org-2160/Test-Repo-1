def count_letters():
    word = input("Enter a word to count it's letters: ")
    if word.isalpha():
        letter_count = 0
        for letter in word:
            letter_count += 1
        return(letter_count)
    else:
        raise ValueError("You didn't enter a word :/")
