---
slug: longest-consecutive-sequence
title: Longest Consecutive Sequence
difficulty: medium
source: leetcode
url: https://leetcode.com/problems/longest-consecutive-sequence/
tags: [array, hash-set, union-find]
lists: [blind-75]
added: 2026-05-30
---

## Description
Given an unsorted array of integers `nums`, return the length of the longest consecutive elements sequence.

You must write an algorithm that runs in `O(n)` time.

## Examples
1. **Input:** `nums = [100,4,200,1,3,2]`
   **Output:** `4`
   **Explanation:** The longest consecutive elements sequence is `[1, 2, 3, 4]`. Therefore its length is 4.

2. **Input:** `nums = [0,3,7,2,5,8,4,6,0,1]`
   **Output:** `9`

3. **Input:** `nums = [1,0,1,2]`
   **Output:** `3`

## Constraints
- `0 <= nums.length <= 10^5`
- `-10^9 <= nums[i] <= 10^9`
