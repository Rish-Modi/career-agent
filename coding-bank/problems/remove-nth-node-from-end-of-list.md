---
slug: remove-nth-node-from-end-of-list
title: Remove Nth Node From End of List
difficulty: medium
source: leetcode
url: https://leetcode.com/problems/remove-nth-node-from-end-of-list/
tags: [linked-list, two-pointers]
lists: [blind-75]
added: 2026-06-02
---

## Description

Given the `head` of a linked list, remove the `nth` node from the end of the list and return its head.

## Examples

1. **Input:** `head = [1,2,3,4,5], n = 2`
   **Output:** `[1,2,3,5]`

2. **Input:** `head = [1], n = 1`
   **Output:** `[]`

3. **Input:** `head = [1,2], n = 1`
   **Output:** `[1]`

## Constraints

- The number of nodes in the list is `sz`.
- `1 <= sz <= 30`
- `0 <= Node.val <= 100`
- `1 <= n <= sz`

## Follow-up

Could you do this in one pass?
