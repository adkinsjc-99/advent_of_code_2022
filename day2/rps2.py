legend = {
  "A": {
    "X": 3,
    "Y": 4,
    "Z": 8
  },
  "B": {
    "X": 1,
    "Y": 5,
    "Z": 9
  },
  "C": {
    "X": 2,
    "Y": 6,
    "Z": 7
  }
}

score = 0

while True:
  try:
    guide = input().split()
    score += legend[guide[0]][guide[1]]

  except EOFError:
    break

print(score)