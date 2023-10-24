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


# part_5
def dictionary_separator(**kwargs):
    keys = list(kwargs.keys())
    values = list(kwargs.values())
    return (keys, values)


user = {"name": "Naruto", "age": 16, "favorite word": "Ichiraku Ramen"}
items = dictionary_separator(**user)
# print(items[0])
# print(items[1])


# part_6
def dictionary_creator(*args, **kwargs):
    if len(args) < len(kwargs):
        return None
    else:
        result_dict = dict(zip(args, kwargs.values()))
        return result_dict


change_keys = ["username", "password", "address"]
user = {"name": "Williams", "some_key": "1234"}
modified_user = dictionary_creator(*change_keys, **user)
# print(modified_user)


# part_6
def purchase_logger(**kwargs):
    quantity = kwargs.get("quantity", "N/A")
    name = kwargs.get("name", "N/A")
    price = kwargs.get("price", "N/A")

    product_info = f"{quantity} {name} bought by {price}"
    return product_info


purchase = {"name": "bolacha trakinas", "price": 2.9, "quantity": 4}

purchase_log = purchase_logger(**purchase)
print(purchase_log)
