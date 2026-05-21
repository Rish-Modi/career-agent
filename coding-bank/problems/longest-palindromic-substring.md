---
slug: longest-palindromic-substring
title: Longest Palindromic Substring
difficulty: medium
source: leetcode
url: https://leetcode.com/problems/longest-palindromic-substring/
tags: [string, dynamic-programming, two-pointers]
added: 2026-05-17
---

## Description

Given a string `s`, return the longest palindromic substring in `s`.

## Examples

1. **Input:** `s = "babad"`
   **Output:** `"bab"`
   **Explanation:** `"aba"` is also a valid answer.

2. **Input:** `s = "cbbd"`
   **Output:** `"bb"`

## Constraints

- `1 <= s.length <= 1000`
- `s` consist of only digits and English letters.

## Hints

- How can we reuse a previously computed palindrome to compute a larger palindrome?
- If `"aba"` is a palindrome, is `"xabax"` a palindrome? Similarly, is `"xabay"` a palindrome?
- Complexity based hint: If we use brute-force and check whether for every start and end position a substring is a palindrome we have `O(n^2)` start/end pairs and `O(n)` palindromic checks. Can we reduce the time for palindromic checks to `O(1)` by reusing some previous computation?
