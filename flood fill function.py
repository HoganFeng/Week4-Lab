board = [
    "......................",
    "......##########......",
    "......#........#......",
    "......#........#......",
    "......#........#####..",
    "....###............#..",
    "....#............###..",
    "....##############....",
]

def flood_fill(input_board:list, old:str, new:str, x:int, y:int):
  if x < 0 or x >= len(input_board) or y < 0 or y >= len(input_board[0]) or input_board[x][y] != old:
    return input_board

  if input_board[x][y] == old:
    input_board[x] = input_board[x][:y] + new + input_board[x][y+1:]
    flood_fill(input_board, old, new, x - 1, y)
    flood_fill(input_board, old, new, x + 1, y)
    flood_fill(input_board, old, new, x, y -1)
    flood_fill(input_board, old, new, x, y + 1)
  return input_board


modified_board = flood_fill(input_board=board, old=".", new="~", x=5, y=12)

for a in modified_board:
  print(a)


modified_board = flood_fill(input_board=board, old=".", new ="~", x=1, y=1)

for a in modified_board:
  print(a)
