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


def get_sorted_dict(letter_counts):
    sorted_list = []
    for key in letter_counts:
        sorted_list.append({
            "value": key,
            "count": letter_counts[key]
        })
    sorted_list.sort(reverse=True, key=lambda x: x["count"])
    return sorted_list
