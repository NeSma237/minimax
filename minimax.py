"""General Minimax solver for a finite game tree represented as nested JSON arrays."""
from __future__ import annotations
import json
import math
import sys
from typing import TypeAlias

Tree: TypeAlias = int | float | list["Tree"]


def validate(node: object, path: str = "root") -> None:
    """Reject empty branches, booleans, and non-finite/non-numeric leaves."""
    if isinstance(node, bool):
        raise ValueError(f"{path}: booleans are not valid leaf values")
    if isinstance(node, (int, float)):
        if not math.isfinite(node):
            raise ValueError(f"{path}: leaf values must be finite numbers")
        return
    if isinstance(node, list):
        if not node:
            raise ValueError(f"{path}: a branch cannot be empty")
        for i, child in enumerate(node):
            validate(child, f"{path}[{i}]")
        return
    raise ValueError(f"{path}: use a number for a leaf or an array for a branch")


def minimax(node: Tree, depth: int = 0, maximizing: bool = True) -> float:
    """Return the backed-up value. The root is MAX; roles alternate by level."""
    if not isinstance(node, list):
        return float(node)
    child_values = [minimax(child, depth + 1, not maximizing) for child in node]
    return max(child_values) if maximizing else min(child_values)


def explain(node: Tree, depth: int = 0, maximizing: bool = True) -> float:
    """Print each internal decision while evaluating the tree bottom-up."""
    if not isinstance(node, list):
        return float(node)
    values = [explain(child, depth + 1, not maximizing) for child in node]
    result = max(values) if maximizing else min(values)
    role = "MAX" if maximizing else "MIN"
    print(f"Depth {depth} {role}: children {values} -> {result:g}")
    return result


def main() -> int:
    print("Minimax - enter a game tree as nested arrays and numeric leaves.")
    print("Example: [[3, 5], [2, 9]]  (root is MAX; next level is MIN)")
    raw = input("Tree: ").strip()
    try:
        tree = json.loads(raw)
        validate(tree)
    except (json.JSONDecodeError, ValueError) as exc:
        print(f"Invalid tree: {exc}", file=sys.stderr)
        return 2
    print("\nEvaluation (from leaves toward the root):")
    value = explain(tree)
    print(f"\nMinimax root value: {value:g}")
    return 0


if __name__ == "__main__":
    raise SystemExit(main())
