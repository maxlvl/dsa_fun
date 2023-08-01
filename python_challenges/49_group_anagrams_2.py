from typing import List
from collections import defaultdict


class Solution:
    def groupAnagrams(self, strs: List[str]) -> List[List[str]]:
        ans_dict = defaultdict(list)

        for word in strs:
            count_list = [0] * 26
            for char in word:
                count_list[ord(char) - ord("a")] += 1

            ans_dict[count_list].append(word)

        return ans_dict.values()
