---
slug: number-of-ways-to-wear-different-hats-to-each-other
title: Number of Ways to Wear Different Hats to Each Other
difficulty: hard
source: leetcode
url: https://leetcode.com/problems/number-of-ways-to-wear-different-hats-to-each-other/
tags: [array, dynamic-programming, bit-manipulation]
companies: [roblox]
added: 2026-06-03
---

## Description

There are `n` people and `40` types of hats labeled from `1` to `40`.

Given a 2D integer array `hats`, where `hats[i]` is a list of all hats preferred by the `ith` person.

Return the number of ways that `n` people can wear different hats from each other.

Since the answer may be too large, return it modulo `10^9 + 7`.

## Examples

1. **Input:** `hats = [[3,4],[4,5],[5]]`
   **Output:** `1`
   **Explanation:** There is only one way to choose hats given the conditions. First person chooses hat 3, second person chooses hat 4, and last one chooses hat 5.

2. **Input:** `hats = [[3,5,1],[3,5]]`
   **Output:** `4`
   **Explanation:** There are 4 ways to choose hats: (3,5), (5,3), (1,3), and (1,5).

3. **Input:** `hats = [[1,2,3,4],[1,2,3,4],[1,2,3,4],[1,2,3,4]]`
   **Output:** `24`
   **Explanation:** Each person can choose hats labeled from 1 to 4. Number of permutations of (1,2,3,4) = 24.

## Constraints

- `n == hats.length`
- `1 <= n <= 10`
- `1 <= hats[i].length <= 40`
- `1 <= hats[i][j] <= 40`
- `hats[i]` contains a list of unique integers.

## Hints

- Dynamic programming + bitmask.
- `dp(peopleMask, idHat)` = number of ways to wear different hats given a bitmask (people visited) and used hats from 1 to `idHat - 1`.
