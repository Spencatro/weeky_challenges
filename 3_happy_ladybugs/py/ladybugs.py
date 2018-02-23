import sys


def wrap(board):
    return "YES" if ladybug(board) else "NO"


def ladybug(board):
    if "_" in board:
        counts = {}
        for char in board:
            if char != "_":
                if char not in counts:
                    counts[char] = 0
                counts[char] += 1
        return all([count >= 2 for count in counts.values()])
    else:  # no moves available, all bugs must be happy at start or never at all
        all_happy = len(board) > 1 and board[0] == board[1] and board[-1] == board[-2]
        for idx, bug in enumerate(board[1:-1]):
            idx += 1  # we started at 1
            all_happy = all_happy and (bug == board[idx - 1] or bug == board[idx + 1])
            if not all_happy:
                break
        return all_happy


Q = int(input().strip())
for a0 in range(Q):
    n = int(input().strip())
    b = input().strip()
    print(wrap(b))