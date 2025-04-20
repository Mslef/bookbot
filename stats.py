def get_num_words(text):
    return len(text.split())


def get_letter_count(text):
    counts = {}
    for char in text.lower():
        if char in counts:
            counts[char] += 1
        else:
            counts[char] = 1
    return counts
