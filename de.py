class Solution1(object):
    def uniquePaths(self, m, n):
        def solve(m,n):
            if m == 0 or n == 0:
                return 0
            if m == 1 and n == 1:
                return 1
            return solve(m-1,n)+solve(m,n-1)
        ans = solve(m,n)
        print(ans)
        return ans


m = 3
n = 7
ob=Solution1()
ob.uniquePaths(3,7)