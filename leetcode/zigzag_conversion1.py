class Solution:
    def convert(self, s: str, numRows):
        if numRows == 1:
            return s
        result = ""
        # append the top row
        index = 0
        while index < len(s):
            result += s[index]
            index += 2 * numRows - 2
        # append the middle row
        row = 1
        while row < numRows - 1:
            row_index = row
            zag_index = 2 * numRows - 2 - row
            is_row = True
            while True:
                if is_row and row_index < len(s):
                    result += s[row_index]
                    row_index += 2 * numRows - 2
                    is_row = False
                elif not is_row and zag_index < len(s):
                    result += s[zag_index]
                    zag_index += 2 * numRows - 2
                    is_row = True
                else:
                    break
            row += 1
        # append the bottom row
        index = numRows - 1
        while index < len(s):
            result += s[index]
            index += 2 * numRows - 2
        return result


print(Solution().convert("PAYPALISHIRING", 3) == "PAHNAPLSIIGYIR")
print(Solution().convert("PAYPALISHIRING", 4) == "PINALSIGYAHRPI")
print(Solution().convert("A", 1) == "A")
