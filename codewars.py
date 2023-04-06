def spin_words(sentence):
    # Empty list created
    new_sentence = []
    # Split string that has been passed in as an argument into a list of stings.
    split_sentence = sentence.split()
    # Loop through list and reverse words that are over 4 characters in length. Push each word onto the new list.
    for word in split_sentence:
        if len(word)>4:
            reverse = word[::-1]
            new_sentence.append(reverse)
        else:
            new_sentence.append(word)
    # Join the list into a string separated by spaces.
    return ' '.join(new_sentence)

assert spin_words('Hello my name is Timothy') == 'olleH my name is yhtomiT'