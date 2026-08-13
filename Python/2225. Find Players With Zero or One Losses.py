class Solution:
    def findWinners(self, matches: List[List[int]]) -> List[List[int]]:
        losses = {}

        for winner, loser in matches:
            if winner not in losses:
                losses[winner] = 0

            losses[loser] = losses.get(loser, 0) + 1

        zero = []
        one = []

        for player, cnt in losses.items():
            if cnt == 0:
                zero.append(player)
            elif cnt == 1:
                one.append(player)

        zero.sort()
        one.sort()

        return [zero, one]
