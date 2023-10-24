# part_1
def sum_numbers(*args):
    num = sum(args)
    return num


numbers = [1, 2, 3, 4, 5, 6]
result = sum_numbers(*numbers)
# print(result)


# part_2
def get_multiplied_amount(multiplier, *args):
    num = sum(args)
    return multiplier * num


numbers = [1, 2, 3]
multiplier = 2
result = get_multiplied_amount(multiplier, *numbers)
# print(result)


# part_3
def word_concatenator(*args):
    concatenated_string = " ".join(args)
    return concatenated_string


words = ["Tá", "pegando", "fogo", "bicho!!!"]
concatenated_words = word_concatenator(*words)
# print(concatenated_words)


# part_4
def inverted_word_factory(*args):
    concatenated_string = " ".join(args)
    inverted_string = concatenated_string[::-1]
    return inverted_string


words = ["eae", "amigão", "belezinha?"]
inverted_words = inverted_word_factory(*words)
# print(inverted_words)
