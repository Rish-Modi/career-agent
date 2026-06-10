---
slug: course-schedule-ii
title: Course Schedule II
difficulty: medium
source: leetcode
url: https://leetcode.com/problems/course-schedule-ii/
tags: [graph, topological-sort, bfs, dfs]
companies: [roblox]
added: 2026-06-09
---

## Description

There are a total of `numCourses` courses you have to take, labeled from `0` to `numCourses - 1`. You are given an array `prerequisites` where `prerequisites[i] = [a_i, b_i]` indicates that you **must** take course `b_i` first if you want to take course `a_i`.

- For example, the pair `[0, 1]` indicates that to take course `0` you have to first take course `1`.

Return the ordering of courses you should take to finish all courses. If there are many valid answers, return any of them. If it is impossible to finish all courses, return an empty array.

## Examples

1. **Input:** `numCourses = 2, prerequisites = [[1,0]]`
   **Output:** `[0,1]`
   **Explanation:** There are a total of 2 courses to take. To take course 1 you should have finished course 0. So the correct course order is `[0,1]`.

2. **Input:** `numCourses = 4, prerequisites = [[1,0],[2,0],[3,1],[3,2]]`
   **Output:** `[0,1,2,3]`
   **Explanation:** One correct ordering is `[0,1,2,3]`. Another correct ordering is `[0,2,1,3]`.

3. **Input:** `numCourses = 1, prerequisites = []`
   **Output:** `[0]`

## Constraints

- `1 <= numCourses <= 2000`
- `0 <= prerequisites.length <= numCourses * (numCourses - 1)`
- `prerequisites[i].length == 2`
- `0 <= a_i, b_i < numCourses`
- `a_i != b_i`
- All the pairs `[a_i, b_i]` are distinct.

## Hints

- This is a topological sort of a directed graph. A valid ordering exists only if the graph is a DAG (no cycles).
- Kahn's algorithm (BFS): track each node's in-degree, start a queue with all in-degree-0 nodes, repeatedly pop one into the result and decrement its neighbors' in-degrees. If you process fewer than `numCourses` nodes, there's a cycle, return `[]`.
- Alternative: DFS post-order, pushing a node after all its descendants, then reverse. Detect cycles with a three-color (visiting/visited) marking.
