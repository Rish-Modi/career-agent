# Coding Bank

A shared library of coding-interview problems. One file per problem in `problems/<slug>.md`. Used by the `coding-prep` skill.

The bank stores **problems only**, never solutions or personal notes. Personal artifacts (attempts, code, time taken, struggle points) live in `$PERSONAL/career/coding-log/`, linked back to bank entries by `slug`.

## Schema

Each `problems/<slug>.md` file uses this frontmatter and body:

```yaml
---
slug: two-sum                          # kebab-case, matches filename (no extension)
title: Two Sum
difficulty: easy                       # easy | medium | hard
source: leetcode                       # leetcode | hackerrank | codesignal | neetcode | other
url: https://leetcode.com/problems/two-sum/
tags: [array, hash-map]                # pattern tags — see "Tag vocabulary" below
added: 2026-05-16                      # YYYY-MM-DD
---

## Description
<problem statement, verbatim from source>

## Examples
1. **Input:** ...
   **Output:** ...
   **Explanation:** ...

## Constraints
- ...

## Hints
- <hint 1>
- <hint 2>
```

Sections may be omitted when the source does not provide them (e.g., no official hints). Keep section order stable so the skill can parse consistently.

## Slug rules

- All lowercase, kebab-case.
- Match the canonical problem name on the source platform.
- Strip articles ("the", "a", "an") only if they are not load-bearing.
- Numbers spelled out only when they start the title.

Examples:

| Title                                              | Slug                                              |
| -------------------------------------------------- | ------------------------------------------------- |
| Two Sum                                            | `two-sum`                                         |
| Longest Substring Without Repeating Characters     | `longest-substring-without-repeating-characters`  |
| 3Sum                                               | `three-sum`                                       |
| Best Time to Buy and Sell Stock II                 | `best-time-to-buy-and-sell-stock-ii`              |

## Tag vocabulary

Prefer existing tags when adding new problems. Add new ones only when the pattern is genuinely distinct.

**Data structures:** `array`, `string`, `hash-map`, `hash-set`, `linked-list`, `stack`, `queue`, `heap`, `tree`, `binary-tree`, `bst`, `trie`, `graph`, `matrix`

**Patterns:** `two-pointers`, `sliding-window`, `binary-search`, `prefix-sum`, `monotonic-stack`, `monotonic-queue`, `union-find`, `topological-sort`, `bfs`, `dfs`, `backtracking`, `greedy`, `divide-and-conquer`

**Algorithm families:** `dynamic-programming`, `recursion`, `bit-manipulation`, `math`, `intervals`, `sorting`

## What does NOT belong here

- Solutions (in any language).
- Your attempts, time taken, struggle points, or learning notes.
- Application or interview metadata.

All of the above goes in `$PERSONAL/career/coding-log/`.

## Copyright disclaimer

Many problems in this bank are sourced from third-party platforms (LeetCode, HackerRank, etc.) whose terms of service may restrict redistribution of problem text. This bank stores full text for **personal practice purposes only**. The `source` and `url` fields credit the origin of each problem.

**Do not make this repository public without first reviewing the licensing of each source.** If you intend to publish, replace copied text with your own paraphrase, keep only the title and URL, or seek permission from the platform.
