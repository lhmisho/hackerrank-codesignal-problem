def anagram_checker(arr1, arr2):
    sorted_dict = {}
    for word in  range(0, len(arr1)):
        sorted_word = "".join(sorted(arr1[word]))
        sorted_dict.update({sorted_word: sorted_dict.get(sorted_word, 0) + 1})

    for i in range(0, len(arr2)):
        arr2[i] = sorted_dict.get("".join(sorted(arr2[i])), 0)
    

    return arr2

if __name__ == '__main__':
    word_arr1 = ["abc", "bac", "cab", "rank", "kran", "a", "b"]
    word_arr2 = ["abc", "rank", "a", "c"]

    print(anagram_checker(word_arr1, word_arr2))
    
