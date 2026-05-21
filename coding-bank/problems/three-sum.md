---
slug: three-sum
title: 3Sum
difficulty: medium
source: leetcode
url: https://leetcode.com/problems/3sum/
tags: [array, two-pointers, sorting]
added: 2026-05-17
---

## Description

Given an integer array `nums`, return all the triplets `[nums[i], nums[j], nums[k]]` such that `i != j`, `i != k`, and `j != k`, and `nums[i] + nums[j] + nums[k] == 0`.

Notice that the solution set must not contain duplicate triplets.

## Examples

1. **Input:** `nums = [-1,0,1,2,-1,-4]`
   **Output:** `[[-1,-1,2],[-1,0,1]]`
   **Explanation:** The distinct triplets are `[-1,0,1]` and `[-1,-1,2]`. Notice that the order of the output and the order of the triplets does not matter.

2. **Input:** `nums = [0,1,1]`
   **Output:** `[]`
   **Explanation:** The only possible triplet does not sum up to 0.

3. **Input:** `nums = [0,0,0]`
   **Output:** `[[0,0,0]]`
   **Explanation:** The only possible triplet sums up to 0.

## Constraints

- `3 <= nums.length <= 3000`
- `-10^5 <= nums[i] <= 10^5`

## Hints

- So, we essentially need to find three numbers `x`, `y`, and `z` such that they add up to the given value. If we fix one of the numbers say `x`, we are left with the two-sum problem at hand.
- For the two-sum problem, if we fix one of the numbers, say `x`, we have to scan the entire array to find the next number `y`, which is `value - x` where value is the input parameter. Can we change our array somehow so that this search becomes faster?
- The second train of thought for two-sum is, without changing the array, can we use additional space somehow? Like maybe a hash map to speed up the search?
