def naive_string_matching(pattern, text):
    m = len(pattern)
    n = len(text)

    matches = []

    for i in range(n - m + 1):
        j = 0
        while j < m and text[i + j] == pattern[j]:
            j += 1

        if j == m:
            matches.append(i)

    return matches

def compute_lps(pattern):
    m = len(pattern)
    lps = [0] * m

    length = 0
    i = 1

    while i < m:
        if pattern[i] == pattern[length]:
            length += 1
            lps[i] = length
            i += 1
        else:
            if length != 0:
                length = lps[length - 1]
            else:
                lps[i] = 0
                i += 1

    return lps

def kmp_string_matching(pattern, text):
    m = len(pattern)
    n = len(text)

    matches = []

    lps = compute_lps(pattern)

    i = j = 0
    while i < n:
        if pattern[j] == text[i]:
            i += 1
            j += 1

            if j == m:
                matches.append(i - j)
                j = lps[j - 1]
        else:
            if j != 0:
                j = lps[j - 1]
            else:
                i += 1

    return matches

# Example usage
text = "ABABDABACDABABCABAB"
pattern = "ABABCABAB"

print("Naive String Matching:")
matches_naive = naive_string_matching(pattern, text)
print("Pattern matches found at indices:", matches_naive)

print("\nKMP String Matching:")
matches_kmp = kmp_string_matching(pattern, text)
print("Pattern matches found at indices:", matches_kmp)
