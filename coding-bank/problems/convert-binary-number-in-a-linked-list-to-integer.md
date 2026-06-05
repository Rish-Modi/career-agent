---
slug: convert-binary-number-in-a-linked-list-to-integer
title: Convert Binary Number in a Linked List to Integer
difficulty: easy
source: leetcode
url: https://leetcode.com/problems/convert-binary-number-in-a-linked-list-to-integer/
tags: [linked-list, math, bit-manipulation]
added: 2026-06-04
---

## Description
Given `head` which is a reference node to a singly-linked list. The value of each node in the linked list is either `0` or `1`. The linked list holds the binary representation of a number.

Return the decimal value of the number in the linked list.

The most significant bit is at the head of the linked list.

## Examples
1. **Input:** `head = [1,0,1]`
   **Output:** `5`
   **Explanation:** `(101)` in base 2 = `(5)` in base 10
2. **Input:** `head = [0]`
   **Output:** `0`

## Constraints
- The Linked List is not empty.
- Number of nodes will not exceed `30`.
- Each node's value is either `0` or `1`.

## Hints
- Traverse the linked list and store all values in a string or array. Convert the values obtained to decimal value.
- You can solve the problem in O(1) memory using bits operation. Use shift left operation (`<<`) and or operation (`|`) to get the decimal value in one operation.
