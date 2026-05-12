# 백준 1991 — 트리 순회
# https://www.acmicpc.net/problem/1991
# Time: O(n)   Space: O(n)

import sys

input = sys.stdin.readline


def solve() -> None:
    n = int(input())
    tree: dict[str, tuple[str | None, str | None]] = {}

    for _ in range(n):
        parts = input().split()
        node = parts[0]
        left = parts[1] if parts[1] != "." else None
        right = parts[2] if parts[2] != "." else None
        tree[node] = (left, right)

    def preorder(node: str | None) -> None:
        if node is None:
            return
        print(node, end="")
        left, right = tree[node]
        preorder(left)
        preorder(right)

    def inorder(node: str | None) -> None:
        if node is None:
            return
        left, right = tree[node]
        inorder(left)
        print(node, end="")
        inorder(right)

    def postorder(node: str | None) -> None:
        if node is None:
            return
        left, right = tree[node]
        postorder(left)
        postorder(right)
        print(node, end="")

    preorder("A")
    print()
    inorder("A")
    print()
    postorder("A")
    print()


solve()
