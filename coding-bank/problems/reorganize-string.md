---
slug: reorganize-string
title: Reorganize String
difficulty: medium
source: leetcode
url: https://leetcode.com/problems/reorganize-string/
tags: [string, hash-map, heap, greedy, sorting]
companies: [roblox]
added: 2026-06-09
---

## Description

Given a string `s`, rearrange the characters of `s` so that any two adjacent characters are not the same.

Return any possible rearrangement of `s` or return `""` if not possible.

## Examples

1. **Input:** `s = "aab"`
   **Output:** `"aba"`

2. **Input:** `s = "aaab"`
   **Output:** `""`

## Constraints

- `1 <= s.length <= 500`
- `s` consists of lowercase English letters.

## Hints

- Feasibility check: a valid rearrangement exists only if the most frequent character appears at most `ceil(n / 2)` times. Otherwise return `""`.
- Greedy fill: place the most frequent characters first, spreading them into alternating slots (even indices, then odd) so no two land adjacent. A max-heap by remaining count makes this clean.
