def longestUniqueSubsttr(string):
    seen = {}
    maximum_length = 0

    start = 0

    for end in range(len(string)):

        if string[end] in seen:
            start = max(start, seen[string[end]] + 1)

        seen[string[end]] = end
        maximum_length = max(maximum_length, end - start + 1)
    return maximum_length


string = input("Enter a String")
max_length = longestUniqueSubsttr(string)
print("The length of the longest non-repeating character substring is", max_length)

