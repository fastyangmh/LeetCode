class Solution:
    def mergeTriplets(self, triplets: List[List[int]], target: List[int]) -> bool:
        tx, ty, tz = target
        has_x = has_y = has_z = False

        for x, y, z in triplets:
            if not (x <= tx and y <= ty and z <= tz):
                continue

            if x == tx:
                has_x = True
            if y == ty:
                has_y = True
            if z == tz:
                has_z = True
            if has_x and has_y and has_z:
                return True

        return has_x and has_y and has_z
