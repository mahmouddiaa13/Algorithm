def find_characters_frequencies(text: str):
    """
        find characters frequencies in a string.
    """
    result = dict()
    for item in text:
        if result.get(item):
            result[item] += 1
        else:
            result[item] = 1
    return result


if __name__ == "__main__":
    print(find_characters_frequencies("hello world"))
