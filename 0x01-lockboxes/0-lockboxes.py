#!/usr/bin/python3
"""
You have n number of locked boxes in front of you. Each box is numbered
sequentially from 0 to n - 1 and each box may contain keys to the other boxes.

Write a method that determines if all the boxes can be opened.

Prototype: def canUnlockAll(boxes)
boxes is a list of lists
A key with the same number as a box opens that box
You can assume all keys will be positive integers
There can be keys that do not have boxes
The first box boxes[0] is unlocked
Return True if all boxes can be opened, else return False
"""


def canUnlockAll(boxes):
    if not boxes or not boxes[0]:
        return False

    num_boxes = len(boxes)
    visited = [False] * num_boxes
    visited[0] = True
    queue = [0]

    while queue:
        current_box = queue.pop(0)

        for key in boxes[current_box]:
            if 0 <= key < num_boxes and not visited[key]:
                visited[key] = True
                queue.append(key)

    return all(visited)
