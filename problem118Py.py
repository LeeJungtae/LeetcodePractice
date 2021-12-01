class Solution:
    def generate(self, numRows: int) -> List[List[int]]:
        result = []
        if numRows >= 1:
            arr = [1]
            result.append(arr)
        if numRows >= 2:
            arr = [1, 1]
            result.append(arr)
        if numRows >= 3:
            for row in range(2, numRows, 1):
                arr = [1]
                for col in range(len(result[row - 1]) - 1):
                    hap = result[row - 1][col] + result[row - 1][col + 1]
                    arr.append(hap)
                arr.append(1)
                result.append(arr)
        return result
