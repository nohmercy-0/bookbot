
def count_words(text):
    words = text.split()
    return len(words)

def count_char(text):
    store = {}
    for char in text:
        lowered = char.lower()
        if lowered in store:
            store[lowered] += 1
        else:
            store[lowered] = 1
    return store

def sort_on(items):
    return items["num"]

def sort(dict):
    list_of_dicts = []
    for char in dict:
        list_of_dicts.append({"char": char, "num": dict[char]})
    list_of_dicts.sort(reverse=True, key=sort_on)
    return list_of_dicts
