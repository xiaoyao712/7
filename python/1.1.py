class Solution:
    def longestCommonPrefix(self, strs):
        """
        :type strs: List[str]
        :rtype: str
        """
        res = ""
        print(f"Initial strs: {strs}")
        for tmp in zip(*strs):
            tmp_set = set(tmp)
            if len(tmp_set) == 1:
                res += tmp[0]
            else:
                break
        return res


strs = ["flower", "flow", "flight"]
solution = Solution()
print(f"{solution.longestCommonPrefix(strs)}")
