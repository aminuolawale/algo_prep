class Solution:
    def longestPalindrome(self, s: str) -> str:
        """ """
        index = 0
        longest = ""
        palindromes = {}
        while index < len(s):
            k = 1
            val = s[index]
            palindromes.update({val: 1})
            while index - k >= 0 and index + k < len(s):
                if s[index - k] == s[index + k] and palindromes[val]:
                    val = s[index - k] + val + s[index + k]
                    palindromes[val] = 1
                else:
                    break
                k += 1
            val1 = ""
            if index < len(s) - 1:
                left, right = s[index], s[index + 1]
                if left == right:
                    val1 = left + right
                    palindromes[val1] = 1
                    k = 1
                    while index - k >= 0 and index + 1 + k < len(s):
                        if s[index - k] == s[index + 1 + k] and palindromes.get(val1):
                            val1 = s[index - k] + val1 + s[index + k + 1]
                            palindromes[val1] = 1
                        else:
                            break
                        k += 1
            g = max(val, val1, key=len)
            longest = max(longest, g, key=len)
            index += 1
        return longest


print(Solution().longestPalindrome("aaaa"))
