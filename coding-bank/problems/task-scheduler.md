---
slug: task-scheduler
title: Task Scheduler
difficulty: medium
source: leetcode
url: https://leetcode.com/problems/task-scheduler/
tags: [array, hash-map, heap, greedy, math]
companies: [roblox]
added: 2026-06-09
---

## Description

You are given an array of CPU `tasks`, each labeled with a letter from A to Z, and a non-negative integer `n`. Each CPU interval can be idle or allow the completion of one task. Tasks do not need to be completed in order, but there is a constraint: there must be a gap of at least `n` intervals between two tasks with the same label.

Return the minimum number of CPU intervals required to complete all tasks.

## Examples

1. **Input:** `tasks = ["A","A","A","B","B","B"]`, `n = 2`
   **Output:** `8`
   **Explanation:** A valid sequence is `A -> B -> idle -> A -> B -> idle -> A -> B`. After completing task A, you must wait two intervals before doing A again. The same applies to task B. In the 3rd interval, neither A nor B can be done, so you idle. By the 4th interval, you can do A again as 2 intervals have passed.

2. **Input:** `tasks = ["A","C","A","B","D","B"]`, `n = 1`
   **Output:** `6`
   **Explanation:** A valid sequence is `A -> B -> C -> D -> A -> B`. With a cooling interval of 1, you can repeat a task after just one other task.

3. **Input:** `tasks = ["A","A","A","B","B","B"]`, `n = 3`
   **Output:** `10`
   **Explanation:** A valid sequence is `A -> B -> idle -> idle -> A -> B -> idle -> idle -> A -> B`.

## Constraints

- `1 <= tasks.length <= 10^4`
- `tasks[i]` is an uppercase English letter.
- `0 <= n <= 100`

## Hints

- The answer is driven by the most frequent task. It forces a skeleton of `maxCount` rows, each `n + 1` wide.
- Closed form: `max(tasks.length, (maxCount - 1) * (n + 1) + numMax)`, where `maxCount` is the highest task frequency and `numMax` is how many task types tie at that frequency.
- To produce an actual valid ordering (not just the count), simulate with a max-heap plus a cooldown queue of size `n`.
