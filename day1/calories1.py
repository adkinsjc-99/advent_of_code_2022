maxElf = 0
currElf = 0

while True:
  try:
    cal = input()
    if len(cal) == 0:
      if currElf > maxElf: maxElf = currElf

      currElf = 0

    else:
      currElf += int(cal)

  except EOFError:
    if currElf > maxElf: maxElf = currElf
    break

print(maxElf)