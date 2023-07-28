from collections import Counter
def minimumCharactersForWords(words):
    char_frequencies = [Counter(word) for word in words]
    print(char_frequencies)
    # Create counter of the maximum characters required
    max_frequencies = Counter()
    for frequency in char_frequencies:
        for char in frequency:
            max_frequencies[char] = max(max_frequencies[char], frequency[char])
    print(max_frequencies)

    # Generate a list of each char repeated x times, based on max_counts
    results = [letter for letter in max_frequencies for _ in range(0, max_frequencies[letter])]
    return results
    