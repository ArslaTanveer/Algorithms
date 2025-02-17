file = open("something.txt", 'w')
file.write("idk im cooked ig")
file.close()

file = open("something.txt", 'r')
readline = file.readline()
while len(readline) != 0:
  print(readline)
  readline = file.readline()
file.close()
