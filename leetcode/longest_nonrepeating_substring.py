from string import ascii_lowercase


class Solution:
    def lengthOfLongestSubstring(self, s: str) -> int:
        start_pointer = 0
        end_pointer = start_pointer
        longest = 0
        character_map = {}
        while end_pointer < len(s) and start_pointer < len(s):
            print(character_map, s[end_pointer])
            if not character_map.get(s[end_pointer]):
                current_string = s[start_pointer : end_pointer + 1]
                longest = (
                    len(current_string) if len(current_string) > longest else longest
                )
                character_map.update({s[end_pointer]: 1})
                end_pointer += 1
            else:
                if character_map[s[start_pointer]] == 0:
                    start_pointer = end_pointer
                    character_map = {}
                else:
                    character_map[s[start_pointer]] -= 1
                    start_pointer += 1
        return longest


print(Solution().lengthOfLongestSubstring("dvdf"))