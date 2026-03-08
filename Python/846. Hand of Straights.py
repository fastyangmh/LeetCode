from collections import Counter


class Solution:
    def isNStraightHand(self, hand: List[int], groupSize: int) -> bool:
        if len(hand) % groupSize != 0:
            return False

        hand.sort()
        counter = Counter(hand)

        for num in hand:
            if counter[num] == 0:
                continue

            for i in range(groupSize):
                if counter[num + i] == 0:
                    return False

                counter[num + i] -= 1
        return True
