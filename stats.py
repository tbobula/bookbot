def get_num_words(content):
    return len(content.split())

def get_characters(content):
    characters = {}
    for c in content:
        c = c.lower()
        if c in characters:
            characters[c] += 1
        else:
            characters[c] = 1
    return characters

def sort_dictionary(dictionary):
   sorted_dictionary = sorted(dictionary.items(), key=lambda x: x[1], reverse=True)
   return dict(sorted_dictionary)