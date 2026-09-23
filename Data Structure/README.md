# Data Structure

This folder contains 26 BOJ solution files. Dates are the earliest recorded study dates in the original Study Log.

## 📅 Study Log

| Date | Category | Problem | Key Learnings |
| :--- | :--- | :--- | :--- |
| 2026-02-07 | Data Structure | 10828 | Class Implementation, Amortized Analysis (Dynamic Array Resizing). |
| 2026-02-08 | Data Structure | 10845 | Implemented Queue with Deque; Optimized pop from $O(N)$ to $O(1)$; Analyzed list shifting cost. |
| 2026-02-09 | Data Structure | 10866 | Implemented Deque; Analyzed memory shift cost ($O(N)$) of `insert(0)` vs `append` ($O(1)$). |
| 2026-02-10 | Data Structure | 1406 | Represented text on either side of the cursor with two stacks, allowing each editing command to run in O(1) time. |
| 2026-02-11 | Data Structure | 1158 | Implemented Circular Queue simulation using deque.rotate() to solve Josephus Problem in O(NK). |
| 2026-02-18 | Data Structure | 9012 | Implemented Stack class; Solved 'Empty Pop' edge case using Boolean return signals. |
| 2026-02-19 | Data Structure | 10773 | Implemented Stack class; Managed LIFO memory operations and optimized I/O using sys.stdin.readline. |
| 2026-02-20 | Data Structure | 2164 | Utilized collections.deque for $O(1)$ front/back operations; Replaced custom class overhead with standard library to prevent Time Limit Exceeded (TLE). |
| 2026-02-23 | Data Structure | 1966 | Simulated Priority Queue rotation using `collections.deque`; Implemented `enumerate` for index tracking; Applied `any()` for dynamic priority scanning. |
| 2026-02-27 | Data Structure | 1874 | Mastered Stack LIFO logic using an independent counter to avoid array-comparison traps; Refactored procedural logic into an Object-Oriented class structure. |
| 2026-03-03 | Data Structure | 4949 | Engineered a multi-bracket validation system using LIFO stack architecture, patching empty-stack crashes and object memory states. |
| 2026-03-06 | Data Structure | 1021 | Used a deque and its current target index to choose the shorter rotation direction before removing each item. |
| 2026-03-08 | Data Structure | 10799 | Engineered an O(N) stack-based sweep to bypass O(N^2) geometric coordinate calculations. |
| 2026-03-10 | Data Structure | 3986 | Engineered LIFO stack architectures to process non-crossing state cancellations. |
| 2026-03-12 | Data Structure | 28278 | Implemented stack commands through a class and handled empty-stack cases. |
| 2026-03-13 | Data Structure | 12789 | Engineered a strict 4-rule State Machine using an O(1) reversed array and a LIFO stack to simulate physical line management. |
| 2026-03-14 | Data Structure | 18258 | Engineered a strictly O(1) FIFO Queue bypassing the O(N) list pop(0) bottleneck using collections.deque. |
| 2026-03-16 | Data Structure | 11866 | Simulated Josephus elimination with `deque.rotate()` and `popleft()`. |
| 2026-03-16 | Data Structure | 28279 | Implemented the eight deque commands in an OOP wrapper around `collections.deque`. |
| 2026-03-17 | Data Structure | 2346 | Engineered complex circular rotation logic for balloons. |
| 2026-03-17 | Data Structure | 24511 | Bypassed O(N*M) time limit by ignoring Stacks and filtering Queues using `zip()` and list comprehension. |
| 2026-04-29 | Data Structure | 15828 | Simulated a fixed-size network router buffer using a deque to handle incoming packets and process them in FIFO order. |
| 2026-05-04 | Data Structure | 1544 | Rotated each word with a deque and used a set to identify equivalent circular words. |
| 2026-05-15 | Data Structure | 1935 | Solved postfix expression evaluation by implementing a stack (LIFO), handling operand ordering with a temporary list, and formatting float outputs. |
| 2026-06-17 | Data Structure | 33848 | Implemented a persistent stack capable of reverting state changes (undo). Managed push and pop histories using an auxiliary log and a temporary stack to restore elements efficiently. |
| 2026-06-18 | Data Structure | 34944 | Implemented a stack-based bracket validator and applied a brute-force approach to determine if substituting exactly one bracket resolves an invalid sequence. Annotated time complexity O(N * L^2). |
