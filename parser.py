fin = open("/home/nathan/Projects/linuxlogger/keymaps.txt", "r")
lineList = fin.readlines()
fin.close()
args = ['nul']*88

for line in lineList:
	if line[0] == "k":
          args.insert(int(line[8:10]),line[13:len(line)-1])
          args.pop()

fin = open("/home/nathan/Projects/linuxlogger/log.txt", "r")
lineList = fin.readlines()
fin.close()
f = open("/home/nathan/Projects/linuxlogger/output.txt", "a")


index = 0
for line in lineList:
	if line[0:5] == "keyco":
		index = int(line[9:11])
		if (index == 42 or index == 54) and line[12:len(line) - 1] == "press":
			# shift has been pressed
			f.write("<Shift pressed>")
		elif index == 58 and line[12:len(line) - 1] == "press":
			# caps has been pressed
			f.write("<Caps pressed>")
		elif index == 28 and line[12:len(line) - 1] == "release":
			f.write("\n")
		elif index == 57 and line[12:len(line) - 1] == "release":
			f.write("\t")
		elif (index == 42 or index == 54) and line[12:len(line) - 1] == "release":
			# shift has been released
			f.write("<Shift released>")
		elif index == 58 and line[12:len(line) - 1] == "release":
			# caps has been released
			f.write("<Caps released>")
		elif line[12:len(line) - 1] == "release":
			f.write(args[index])

f.close()

