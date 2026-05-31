---
slug: longest-substring-without-repeating-characters
title: Longest Substring Without Repeating Characters
difficulty: medium
source: leetcode
url: https://leetcode.com/problems/longest-substring-without-repeating-characters/
tags: [string, hash-map, sliding-window]
lists: [blind-75]
added: 2026-05-30
---

## Description
Given a string `s`, find the length of the longest substring without duplicate characters.

## Examples
1. **Input:** `s = "abcabcbb"`
   **Output:** `3`
   **Explanation:** The answer is `"abc"`, with the length of 3. Note that `"bca"` and `"cab"` are also correct answers.

2. **Input:** `s = "bbbbb"`
   **Output:** `1`
   **Explanation:** The answer is `"b"`, with the length of 1.

3. **Input:** `s = "pwwkew"`
   **Output:** `3`
   **Explanation:** The answer is `"wke"`, with the length of 3. Notice that the answer must be a substring, `"pwke"` is a subsequence and not a substring.

## Constraints
- `0 <= s.length <= 5 * 10^4`
- `s` consists of English letters, digits, symbols and spaces.

## Hints
- Since maximum string size is at most 26, generate and check all possible substrings with length at most 26.
