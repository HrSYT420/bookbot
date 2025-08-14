def get_num_words(text):
    return len(text.split(sep=None, maxsplit=-1))

def get_num_character(text):
    text = text.lower()
    char_count = {}
    for char in text:
        char_count[char] = char_count.get(char, 0) + 1
    return(char_count)