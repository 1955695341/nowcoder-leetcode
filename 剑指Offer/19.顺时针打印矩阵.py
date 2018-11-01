class Solution:
    # matrix类型为二维列表，需要返回列表
    def printMatrix(self, matrix):
        if not matrix:
            return []
        rows = len(matrix)
        cols = len(matrix[0])
        start = 0 # 代表循环次数，也可代表每一圈的起点
        result = []
        while rows > 2*start and cols > 2*start: # 循环次数为行列的最大值除以2取整
            endx = rows - 1 - start # 行数
            endy = cols - 1 - start # 列数
            for i in range(start, endy+1): # 第一行
                result.append(matrix[start][i])
            if start < endx: # 判断下面是否还有行
                for i in range(start+1,endx+1): # 最右列
                    result.append(matrix[i][endy])
            if start < endx and start < endy: # 判断下面是否还有行，右面是否还有列
                for i in range(endy-1, start-1, -1): # 最下行
                    result.append(matrix[endx][i])
            if start < endx-1 and start < endy:  # 判断下面是否还有行，判断该列是否重复
                for i in range(endx-1, start, -1): # 最左列
                    result.append(matrix[i][start])
            start += 1
        return result