---
slug: two-sum
title: Two Sum
difficulty: easy
source: leetcode
url: https://leetcode.com/problems/two-sum/
tags: [array, hash-map]
added: 2026-05-16
---

## Description

Given an array of integers `nums` and an integer `target`, return indices of the two numbers such that they add up to `target`.

You may assume that each input would have exactly one solution, and you may not use the same element twice.

You can return the answer in any order.

## Examples

1. **Input:** `nums = [2,7,11,15]`, `target = 9`
   **Output:** `[0,1]`
   **Explanation:** Because `nums[0] + nums[1] == 9`, we return `[0, 1]`.

2. **Input:** `nums = [3,2,4]`, `target = 6`
   **Output:** `[1,2]`

3. **Input:** `nums = [3,3]`, `target = 6`
   **Output:** `[0,1]`

## Constraints

- `2 <= nums.length <= 10^4`
- `-10^9 <= nums[i] <= 10^9`
- `-10^9 <= target <= 10^9`
- Only one valid answer exists.

## Follow-up

Can you come up with an algorithm that is less than `O(n^2)` time complexity?

## Hints

- A really brute force way would be to search for all possible pairs of numbers, but that would be too slow. It is from these brute force solutions that you can come up with optimizations.
- If we fix one of the numbers, say `x`, we have to scan the entire array to find the next number `y` which is `target - x`. Can we change our array somehow so that this search becomes faster?
- Without changing the array, can we use additional space somehow? Like maybe a hash map to speed up the search?
