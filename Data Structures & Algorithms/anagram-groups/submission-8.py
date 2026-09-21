from collections import defaultdict

class Solution:
    def groupAnagrams(self, strs: List[str]) -> List[List[str]]:
        hash = defaultdict(list)
        for word in strs:
            key = [0] * 26
            for char in word:
                key[ord(char)-ord('a')] += 1
            hash[tuple(key)].append(word)
        return list(hash.values())