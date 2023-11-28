def boyer_moore_search(haystack, needle):
    if not haystack or not needle:
        print("Both haystack and needle must be non-empty")
        return []

    haystack_len = len(haystack)
    needle_len = len(needle)

    shift_table = {char: needle_len - index - 1 for index, char in enumerate(needle[:-1])}
    shift_table[needle[-1]] = needle_len if needle[-1] not in needle[:-1] else 1

    index_list = []

    i = needle_len - 1
    while i < haystack_len:
        j = needle_len - 1

        while j >= 0 and haystack[i] == needle[j]:
            i -= 1
            j -= 1

        if j == -1:
            index_list.append(i + 1)

        i += max(shift_table.get(haystack[i], needle_len), needle_len - j)

    return index_list


haystack = "ababcababcabcabc"
needle = "abc"
result = boyer_moore_search(haystack, needle)
print(f"Знайдені індекси входжень '{needle}' в '{haystack}': {result}")
