---
slug: longest-common-prefix
title: Longest Common Prefix
difficulty: easy
source: leetcode
url: https://leetcode.com/problems/longest-common-prefix/
tags: [string, array]
companies: [roblox]
added: 2026-06-09
---

## Description

Write a function to find the longest common prefix string amongst an array of strings.

If there is no common prefix, return an empty string `""`.

## Examples

1. **Input:** `strs = ["flower","flow","flight"]`
   **Output:** `"fl"`

2. **Input:** `strs = ["dog","racecar","car"]`
   **Output:** `""`
   **Explanation:** There is no common prefix among the input strings.

## Constraints

- `1 <= strs.length <= 200`
- `0 <= strs[i].length <= 200`
- `strs[i]` consists of only lowercase English letters if it is non-empty.

## Hints

- Take the first string as a candidate prefix and shrink it against each other string until it matches the start of all of them.
- Or compare characters column by column: at position `i`, every string must share the same character; stop at the first mismatch or when any string ends.
