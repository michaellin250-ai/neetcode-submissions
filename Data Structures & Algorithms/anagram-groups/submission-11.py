class Solution:
    def groupAnagrams(self, strs: List[str]) -> List[List[str]]:
        result = {}

        for string in strs:
            s = tuple(sorted(string))
            if s not in result:
                result[s] = []
            result[s].append(string)
        return list(result.values())
