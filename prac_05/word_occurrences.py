"""
CP1404/CP5632 Practical
Count word occurrences in a string
"""

word_to_occurrence_count = {}
input_words = input('Text: ').split()

# Get occurrence counts for each word
for word in input_words:
    if word in word_to_occurrence_count:
        word_to_occurrence_count[word] += 1
    else:
        word_to_occurrence_count[word] = 1

# Display occurrence counts for each word
words = list(word_to_occurrence_count.keys())
words.sort()
max_word_length = max(len(word) for word in words)
max_number_length = len(str(max(word_to_occurrence_count.values())))
for word in words:
    print(f'{word} : {word_to_occurrence_count[word]:{max_word_length + max_number_length - len(word)}}')
