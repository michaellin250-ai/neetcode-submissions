class Solution:
    def groupAnagrams(self, strs: List[str]) -> List[List[str]]:
        result = defaultdict(list)

        for string in strs:
            s = tuple(sorted(string))
            result[s].append(string)
        return list(result.values())
