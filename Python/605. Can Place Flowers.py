class Solution:
    def canPlaceFlowers(self, flowerbed: List[int], n: int) -> bool:
        if n == 0:
            return True

        remaining = n
        l = len(flowerbed)

        for i in range(l):
            left = flowerbed[i - 1] == 0 if i > 0 else True
            right = flowerbed[i + 1] == 0 if i + 1 < l else True
            curr = flowerbed[i] == 0

            if left and right and curr:
                remaining -= 1
                flowerbed[i] = 1

            if remaining == 0:
                return True

        return False
