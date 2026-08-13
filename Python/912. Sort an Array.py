class Solution:
    def sortArray(self, nums: List[int]) -> List[int]:
        # # method1
        # temp = [0] * len(nums)

        # def merge_sort(left, right):
        #     if left >= right:
        #         return

        #     mid = (left + right) // 2

        #     merge_sort(left, mid)
        #     merge_sort(mid + 1, right)

        #     merge(left, mid, right)

        # def merge(left, mid, right):
        #     i = left
        #     j = mid + 1
        #     k = left

        #     while i <= mid and j <= right:
        #         if nums[i] <= nums[j]:
        #             temp[k] = nums[i]
        #             i += 1
        #         else:
        #             temp[k] = nums[j]
        #             j += 1
        #         k += 1

        #     while i <= mid:
        #         temp[k] = nums[i]
        #         i += 1
        #         k += 1

        #     while j <= right:
        #         temp[k] = nums[j]
        #         j += 1
        #         k += 1

        #     for idx in range(left, right + 1):
        #         nums[idx] = temp[idx]

        # merge_sort(0, len(nums) - 1)

        # return nums

        # method2
        n = len(nums)

        def heapify(i, heap_size):
            largest = i
            left = 2 * i + 1
            right = 2 * i + 2

            if left < heap_size and nums[left] > nums[largest]:
                largest = left

            if right < heap_size and nums[right] > nums[largest]:
                largest = right

            if largest != i:
                nums[i], nums[largest] = nums[largest], nums[i]
                heapify(largest, heap_size)

        for i in range(n // 2 - 1, -1, -1):
            heapify(i, n)

        for end in range(n - 1, 0, -1):
            nums[0], nums[end] = nums[end], nums[0]
            heapify(0, end)

        return nums
