from itertools import permutations

def groupAnagrams(strs):
    # strs is a list holding words. Some could be anagrams of each other
    # if anagrams, store together in a list within the list

    copy = strs
    result = []

    # if '' in copy:
    #     case = []
    #     counter = 0
    #     for step in copy:
    #         if step == '':
    #             counter += 1
    #     j = 0
    #     while j < counter:
    #         case.append("")
    #         j += 1
    #     result.append(case)
    #     copy = [value for value in copy if value != '']

    for word in copy:
        temp = []
        perm = [''.join(p) for p in permutations(word)]
        for i in perm:
            if i in copy:
                temp.append(i)
                copy.remove(i)
        result.append(temp)

    for remaining in copy:
        if remaining not in result:
            print(remaining)
            result.append([remaining])
    return result

strs = ["eat","tea","tan","ate","nat","bat"]

print(groupAnagrams(strs))