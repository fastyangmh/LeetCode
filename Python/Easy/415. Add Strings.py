class Solution:
    def addStrings(self, num1: str, num2: str) -> str:
        len_n1 = len(num1)
        len_n2 = len(num2)
        diff = len_n1-len_n2
        if diff >= 0:
            num2 = '0'*diff+num2
            maximum_len = len_n1
        else:
            num1 = '0'*abs(diff)+num1
            maximum_len = len_n2
        result = []
        carry = 0
        for idx in range(maximum_len-1, -1, -1):
            val = ord(num1[idx])+ord(num2[idx])-2*ord('0')
            val += carry
            carry = val//10
            val = val % 10
            result.append(str(val))
        if carry != 0:
            result.append(str(carry))
        return ''.join(reversed(result))


if __name__ == '__main__':
    # ex1   ans "134"
    num1 = "11"
    num2 = "123"
    print(Solution().addStrings(num1=num1, num2=num2))

    # ex2    ans "533"
    num1 = "456"
    num2 = "77"
    print(Solution().addStrings(num1=num1, num2=num2))

    # ex3    ans "0"
    num1 = "0"
    num2 = "0"
    print(Solution().addStrings(num1=num1, num2=num2))

    # 291 / 317  ans 10
    num1 = "1"
    num2 = "9"
    print(Solution().addStrings(num1=num1, num2=num2))
