class Solution:
    def rotate(self, matrix: List[List[int]]) -> None:
        """
        Do not return anything, modify matrix in-place instead.
        """
        n = len(matrix)
#swapping rows and columns
        for i in range(n):
            for j in range(i+1, n):
                matrix[i][j], matrix[j][i] = matrix[j][i], matrix[i][j] #swapping row(i) with column(j)
#reversing every row
        for i in range(n):
            matrix[i].reverse()

        #O(n^2)