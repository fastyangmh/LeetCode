from typing import List


class Solution:
    def fizzBuzz(self, n: int) -> List[str]:
        rets = []

        for i in range(1, n + 1):
            ret = ""

            if i % 3 == 0:
                ret += "Fizz"
            if i % 5 == 0:
                ret += "Buzz"
            if not ret:
                ret += str(i)

            rets.append(ret)

        return rets
