class Solution:
    def groupAnagrams(self, strs: List[str]) -> List[List[str]]:
        groups = []
        hash = {}
        for word in strs:
            key = str(sorted(word))
            if key in hash:
                hash[key].append(word)
            else:
                hash[key] = [word]
        
        for key in hash:
            groups.append(hash[key])
        
        return groups