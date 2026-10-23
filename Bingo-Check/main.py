"""

Create a function that takes a 5x5 2D list and returns True if it has at least one Bingo, and False If it doesn't.

"""


def bingo_check(board: list) -> bool:
    line = board[0]
    ...# horizontal
    if ["x", "x", "x", "x", "x"] in board:
        return True
    # vertical
    if "x" in line:
        fp = line.index("x")

        for i in board[1:]:
            if i[fp] != "x":
                return False
        return True
    if board[0][0] == "x":

    return False


def main():

    output = bingo_check([
      [45, "x", 31, 74, 87],
      [64, "x", 47, 32, 90],
      [37, "x", 68, 83, 54],
      [67, "x", 98, 39, 44],
      [21, "x", 24, 30, 52]
    ])
    assert output == True

    output = bingo_check([
      ["x", 43, 31, 74, 87],
      [64, "x", 47, 32, 90],
      [37, 65, "x", 83, 54],
      [67, 98, 39, "x", 44],
      [21, 59, 24, 30, "x"]
    ]) 
    assert output == True

    output = bingo_check([
      ["x", "x", "x", "x", "x"],
      [64, 12, 47, 32, 90],
      [37, 16, 68, 83, 54],
      [67, 19, 98, 39, 44],
      [21, 75, 24, 30, 52]
    ]) 
    assert output == True

    output = bingo_check([
      [45, "x", 31, 74, 87],
      [64, 78, 47, "x", 90],
      [37, "x", 68, 83, 54],
      [67, "x", 98, "x", 44],
      [21, "x", 24, 30, 52]
    ]) 
    assert output == False

if __name__ == '__main__':
    main()
