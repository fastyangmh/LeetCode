class Solution:
    def reverse(self, x: int) -> int:
        if x==0:
            return 0
        elif x<0:
            x=abs(x)
            signed=True
        else:
            signed=False
        n=0
        while x>0:
            n=n*10+x%10
            x//=10
        n=n*-1 if signed else n
        if -2**31<n<2**31-1:
            return n
        else:
            return 0

if __name__ == "__main__":
    x=123
    print(Solution().reverse(x))