from typing import List


class Solution:
    def groupAnagrams(self, strs: List[str]) -> List[List[str]]:
        if not strs:
            return []
        ana_dict = {}

        for word in strs:
            sorted_word = "".join(sorted(word))
            if sorted_word not in ana_dict.keys():
                ana_dict[sorted_word] = [word]
            else:
                ana_dict[sorted_word].append(word)

        result_list = []
        for result in ana_dict.values():
            result_list.append(result)
        return result_list
