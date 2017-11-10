# Solution for two sum problem.
# Given an array of integers, return indices of the two numbers such that they add up to a specific target.
# You may assume that each input would have exactly one solution, and you may not use the same element twice.
# The solution makes use of an key-value pairs, and the properties of addition and division.

#! /usr/bin/python

class Solution(object):
    def twoSum(self, nums, target):
        set = {};
        for i in range(len(nums)):
            if nums[i] in set:
                return [set[nums[i]],i];
            else:
                set[target - nums[i]] = i;
