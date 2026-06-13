---
slug: subdomain-visit-count
title: Subdomain Visit Count
difficulty: medium
source: leetcode
url: https://leetcode.com/problems/subdomain-visit-count/
tags: [string, hash-map]
companies: [roblox]
added: 2026-06-10
---

## Description

A website domain `"discuss.leetcode.com"` consists of various subdomains. At the top level we have `"com"`, at the next level we have `"leetcode.com"` and at the lowest level `"discuss.leetcode.com"`. When we visit a domain like `"discuss.leetcode.com"`, we will also visit the parent domains `"leetcode.com"` and `"com"` implicitly.

A **count-paired domain** is a string that contains a count of visits and a domain, separated by a space, e.g. `"9001 discuss.leetcode.com"` means 9001 visits to `"discuss.leetcode.com"`.

Given an array of count-paired domains `cpdomains`, return an array of the count-paired domains for each subdomain in the input. You may return the answer in any order.

## Examples

1. **Input:** `cpdomains = ["9001 discuss.leetcode.com"]`
   **Output:** `["9001 leetcode.com","9001 discuss.leetcode.com","9001 com"]`

2. **Input:** `cpdomains = ["900 google.mail.com","50 yahoo.com","1 intel.mail.com","5 wiki.org"]`
   **Output:** `["901 mail.com","50 yahoo.com","900 google.mail.com","5 wiki.org","5 org","1 intel.mail.com","951 com"]`

## Constraints

- `1 <= cpdomains.length <= 100`
- Each `cpdomain` consists of a count and a domain separated by a single space.
- Each domain has between 1 and 3 labels (separated by `.`).
- The count is a positive integer at most `10^4`.

## Hints

- For each entry, split off the count (parse it to a number) and the domain.
- A subdomain is a suffix of the domain's labels. Split the domain on `.`, then for each starting index `i`, `parts.slice(i).join(".")` yields one subdomain.
- Accumulate counts in a hash map keyed by subdomain, doing the parse and the subdomain generation in a single pass per entry so the count stays in scope.
