import Ex25

sentence = "All good things come to those who wait" 
print(sentence)
words = Ex25.break_words(sentence)
print(words)
print("\n")

sorted_words = Ex25.sort_words(words) 
print(sorted_words)
print("\n")

Ex25.print_first_word(words)
Ex25.print_last_word(words)
print(words)
print("\n")

Ex25.print_first_word(sorted_words)
Ex25.print_last_word(sorted_words)
print(sorted_words)
print("\n")

sorted_words = Ex25.sort_sentence(sentence)
print(sorted_words)
print("\n")

Ex25.print_first_and_last(sentence)
Ex25.print_first_and_last_sorted(sentence)