class Solution:
    def getRow(self, rowIndex: int) -> List[int]:
        result = []
        if rowIndex == 0:
            result = [1]
        elif rowIndex == 1:
            result = [1, 1]
        elif rowIndex >= 2:
            result = [1, 2, 1]
            for row in range(2, rowIndex):
                result2 = [1]
                for col in range(len(result) - 1):
                    hap = result[col] + result[col + 1]
                    result2.append(hap)
                result2.append(1)
                result = result2
        return result
