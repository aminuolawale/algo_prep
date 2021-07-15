class Solution:
    def convert1(self, s: str, numRows):
        """ """
        result = ""
        index = 0
        i = 1
        while index < len(s):
            result += s[index]
            index = (2 * numRows - 2) * i
            i += 1
        print(result)
        row = 1
        while row < numRows - 1:
            index = row
            i = 1
            flip = True
            while index < len(s):
                result += s[index]
                if flip:
                    index += (2 * numRows - 2) - 2 * row
                else:
                    index += 2 * row
            row += 1
        index = numRows - 1
        print(result)
        i = 0
        while index < len(s):
            result += s[index]
            i += 1
            index = numRows - 1 + i * (2 * numRows - 2)
        print(result)

        return result

    def convert(self, s: str, numRows):
        container_index = 0
        container = []
        string_index = 0
        while string_index < len(s):
            if len(s) - string_index - 1 >= numRows:
                current_row = self.split(s[string_index : string_index + numRows])
                string_index += numRows
            else:
                current_row = self.split(s[string_index:])
                current_row.extend([""] * (numRows - len(current_row)))
                container.append(current_row)

                return self.read_container(container)
            container.append(current_row)
            next_row_index = numRows - 2
            while next_row_index > 0:
                container.append([""] * numRows)
                container_index += 1
                container[container_index][next_row_index] = s[string_index]
                string_index += 1
                if string_index >= len(s):
                    break
                next_row_index -= 1
            container_index += 1
        return self.read_container(container)

    def split(self, s) -> list:
        result = []
        for l in s:
            result.append(l)
        return result

    def read_container(self, c) -> str:
        index = 0
        result = ""
        while index < len(c[0]):
            for row in c:
                result += row[index]
            index += 1
        return result


print(Solution().convert1("PAYPALISHIRING", 3) == "PAHNAPLSIIGYIR")
print(Solution().convert1("PAYPALISHIRING", 4) == "PINALSIGYAHRPI")
print(Solution().convert1("A", 1) == "A")
