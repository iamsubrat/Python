def reverse_sentence(sentence):
    # Split the sentence into words
    words = sentence.split()

    # Reverse the order of words
    reversed_words = words[::-1]

    # Join the reversed words to form the reversed sentence
    reversed_sentence = ' '.join(reversed_words)

    return reversed_sentence


# Input sentence
input_sentence = input("Enter a sentence: ")

# Call the function to reverse the sentence
reversed_result = reverse_sentence(input_sentence)

# Print the reversed sentence
print("Reversed Sentence:", reversed_result)
