legend = {
  "A": {
    "X": 4,
    "Y": 8,
    "Z": 3
  },
  "B": {
    "X": 1,
    "Y": 5,
    "Z": 9
  },
  "C": {
    "X": 7,
    "Y": 2,
    "Z": 6
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