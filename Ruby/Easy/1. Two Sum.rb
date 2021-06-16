# @param {Integer[]} nums
# @param {Integer} target
# @return {Integer[]}
def two_sum(nums, target)
    hash={}
    for idx in 0...nums.length() do
        diff=target-nums[idx]
        if hash.include? diff
            return [hash[diff],idx]
        end
        hash[nums[idx]]=idx
    end
end