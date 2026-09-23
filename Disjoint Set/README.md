# Disjoint Set

This folder contains 4 BOJ solution files. Dates are the earliest recorded study dates in the original Study Log.

## 📅 Study Log

| Date | Category | Problem | Key Learnings |
| :--- | :--- | :--- | :--- |
| 2026-09-16 | Disjoint Set | 20040 | Implemented the Union-Find (Disjoint Set) data structure with path compression to detect cycle formation in an undirected graph. Tracked component connectivity dynamically on each edge insertion, evaluating root equivalence to trigger an early exit in amortized near $O(1)$ time per operation. |
| 2026-09-18 | Disjoint Set | 1976 | Implemented the Disjoint Set (Union-Find) data structure with path compression to evaluate itinerary reachability on an undirected graph. Merged adjacent cities into disjoint components and validated whether all planned transit cities share an identical root component in amortized near $O(1)$ time per query. |
| 2026-09-20 | Disjoint Set | 4195 | Utilized a Disjoint Set (Union-Find) backed by hash maps to dynamically index arbitrary string identifiers and track component sizes. Maintained component cardinality upon set mergers and applied path compression to achieve amortized near $O(1)$ time complexity per relationship query. |
| 2026-09-21 | Disjoint Set | 1717 | Implemented canonical Disjoint Set (Union-Find) data structure with path compression. Processed large-scale dynamic set unions and identity queries efficiently in amortized $O(M \cdot \alpha(N))$ time complexity, strictly preventing call-stack overflows. |
