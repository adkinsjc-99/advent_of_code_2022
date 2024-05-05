maxCal = [0, 0, 0]
currElf = 0

def update(cal):
  for i in range(len(maxCal)):
    if cal > maxCal[i]:
      temp = maxCal[i]
      maxCal[i] = cal
      cal = temp

while True:
  try:
    cal = input()
    if len(cal) == 0:
      update(currElf)

      currElf = 0

    else:
      currElf += int(cal)

  except EOFError:
    update(currElf)
    break

print(sum(maxCal))