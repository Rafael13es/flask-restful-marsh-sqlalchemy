##############################
# --- Directions
# Given a string, return the character that is most
# commonly used in the string.
# --- Examples
# max_char("abcccccccd") === "c"
# max_char("apple 1231111") === "1"

def max_char(string):
    char_dict = {}
    max_v = 0
    max_k = ""

    for char in string:
        char_dict[char] = char_dict[char] + 1 if char in char_dict else 1
        print(max_v)
        print(max_k)
        print(char_dict.get(char, 0), char)
        if char_dict[char] > max_v:
            max_v = char_dict[char]
            max_k = char

    return None

    # max_v = 0
    # max_k = ""
    # for k, v in char_dict.items():
    #     if v > max_v:
    #         max_k, max_v = k, v


print(max_char("apple 1231111"))
print(max_char("abcbcbbcbccccd"))

num1: int = 2
print(id(num1))
num2: int = 2
print(id(num2))
