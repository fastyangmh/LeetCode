from typing import List


class Solution:
    def diStringMatch(self, s: str) -> List[int]:
        # time O(n) space(2*n)
        l = 0
        r = len(s)
        array = list(range(len(s)+1))
        ans = []
        if s[0] == 'I':
            ans.append(array[l])
            l += 1
        else:
            ans.append(array[r])
            r -= 1

        for idx in range(1, len(s)):
            if s[idx] == 'I':
                ans.append(array[l])
                l += 1
            else:
                ans.append(array[r])
                r -= 1
        if l < r:
            ans.append(array[l])
        else:
            ans.append(array[r])
        return ans

        '''
        ans = []
        l = 0
        r = len(s)
        for idx in range(len(s)):
            if s[idx] == 'I':
                ans.append(l)
                l += 1
            else:
                ans.append(r)
                r -= 1
        ans.append(l)
        return ans
        '''


if __name__ == '__main__':
    # ex1    ans [0,4,1,3,2]
    s = "IDID"
    print(Solution().diStringMatch(s=s))

    # ex2    ans [0,1,2,3]
    s = "III"
    print(Solution().diStringMatch(s=s))

    # ex3    ans [3,2,0,1]
    s = "DDI"
    print(Solution().diStringMatch(s=s))
