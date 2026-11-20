# Minimax Individual Project

## Run

Requires Python 3.10 or newer. Open a terminal in this folder and run:

```text
python minimax.py
```

Enter the tree as nested JSON arrays. Numbers are leaf utilities; every array is a decision node. The root is MAX and roles alternate at every level (MAX, MIN, MAX, ...). Every node can have any positive number of children, and the tree can have any finite depth. A leaf may appear at a different depth from other leaves.

Example input:

```text
[[3, 5], [2, 9]]
```

This is a MAX root with two MIN children. The first MIN child returns min(3, 5) = 3; the second returns min(2, 9) = 2; the root returns max(3, 2) = 3.

Try changing the values or adding/removing nested arrays. The program reads the new tree each run and recalculates it; no algorithm changes are needed. For example, `[[[4, 8], [6, 2]], [[7, 1], [5, 9]]]` has three decision levels and returns 7.

## How it works

1. Parse the input with Python's JSON parser and validate that each leaf is a finite number and each branch is a non-empty array.
2. Recursively visit each child until reaching numeric leaves.
3. On the way back up, MAX selects the largest child value and MIN selects the smallest. The role switches at every level.
4. The value returned at depth zero is printed as the Minimax root value.

`minimax(node, depth, maximizing)` is the general algorithm. Its recursion stops at numbers, so tree depth is determined by the input rather than hard-coded. Its children are processed before their parent, which is the bottom-up value propagation required by Minimax.

## Discussion guide

- **What is Minimax?** A decision rule for a two-player, zero-sum game. It assumes both players choose moves optimally and finds the best guaranteed outcome for the player whose turn is at the root.
- **What are MAX and MIN?** MAX chooses the greatest value among its children. MIN chooses the least value, because that is the outcome most unfavorable to MAX.
- **How does the code work?** It represents the game tree using arrays for decisions and numbers for terminal outcomes. Recursion evaluates terminal numbers first and then backs values up through the tree, alternating MAX and MIN.
- **How is the root value calculated?** Each internal node applies its own rule to the values returned by its children. The final value returned at the root is printed as the answer.
- **How does it handle different depths?** The function has no fixed depth or number of levels. It recurses until it reaches a number, then returns through as many levels as the input contains. Different branches can also end at different depths.
- **What happens when input values change?** The program parses the new numbers and reevaluates every node, so the root result can change automatically. The tree shape can also change without modifying the code.

## Important assumption

The project treats the root as MAX and alternates player roles once per array level. Each number is a terminal utility from MAX's point of view. If your instructor wants MIN to start instead, change the initial `maximizing=True` argument in `main()` to `False`.

