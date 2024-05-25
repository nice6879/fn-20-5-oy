# def chek_title(func):
#     def wrapper(*args, **kwargs):
#         if 10 == 10:
#             result = func(*args, **kwargs)
#             if len(result) > 3:
#                 return result
#             else:
#                 return None
#         else:
#             return None
#     return wrapper        

import string
def clear_punctuation(func):
    def wrapper(*args, **kwargs):
        clear_args = []
        for word in args:
            word_clear = ''
            for letter in word:
                if letter not in string.punctuation:
                    word_clear += letter
            clear_args.append(word_clear)
        result = func(*clear_args, **kwargs)
        return result
    return  wrapper   
