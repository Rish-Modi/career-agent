---
slug: valid-parentheses
title: Valid Parentheses
difficulty: easy
source: leetcode
url: https://leetcode.com/problems/valid-parentheses/
tags: [string, stack]
lists: [blind-75, neetcode-150]
added: 2026-06-04
---

## Description
Given a string `s` containing just the characters `'('`, `')'`, `'{'`, `'}'`, `'['` and `']'`, determine if the input string is valid.

An input string is valid if:

- Open brackets must be closed by the same type of brackets.
- Open brackets must be closed in the correct order.
- Every close bracket has a corresponding open bracket of the same type.

## Examples
1. **Input:** `s = "()"`
   **Output:** `true`
2. **Input:** `s = "()[]{}"`
   **Output:** `true`
3. **Input:** `s = "(]"`
   **Output:** `false`
4. **Input:** `s = "([])"`
   **Output:** `true`
5. **Input:** `s = "([)]"`
   **Output:** `false`

## Constraints
- `1 <= s.length <= 10^4`
- `s` consists of parentheses only `'()[]{}'`.

## Hints
- Use a stack of characters.
- When you encounter an opening bracket, push it to the top of the stack.
- When you encounter a closing bracket, check if the top of the stack was the opening for it. If yes, pop it from the stack. Otherwise, return false.
