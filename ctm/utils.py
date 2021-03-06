import os

def cpr(parentFile, pasteDir, names):
	parentFileContent = open(parentFile, "rb").read()
	extension = os.path.splitext(parentFile)[1]
	for name in names:
		name = str(name)
		currentDir = os.path.join(pasteDir, name)+extension
		currentFile = open(currentDir, "wb")
		currentFile.write(parentFileContent)
		currentFile.close()

def xor(a, b):
	return a | b

def tupleRange(a, b):
	xList = []
	yList = []
	for x in zip(range(a[0], b[0]+1)):
		xList.append(x[0])
	for y in zip(range(a[1], b[1]+1)):
		yList.append(y[0])
	tuples = []
	lastX = 0
	lastY = 0
	endAt = max(len(xList), len(yList))
	index = 0
	while True:
		try: 
			lastX = xList[index]
		except:
			pass
		try:
			lastY = yList[index]
		except:
			pass
		tuples.append((lastX, lastY))
		if index >= endAt:
			break
		index += 1
	return tuples

def genProps(sides, name, p_id, path, tiles, method, metadata):
	try:
		f = open(os.path.join(path, name)+".properties", "x")
	except:
		f = open(os.path.join(path, name)+".properties", "w")
	f.write(f"method={method}\n")
	f.write(f"tiles=0-{str(tiles)}\n")
	if sides != "":
		f.write(f"sides={sides}\n")
	else:
		pass
	f.write(f"matchBlocks={p_id}\n")
	if sides != 0:
		f.write(f"metadata={metadata}")
	else:
		pass
	f.close()

class Side():
	def __init__(self, l, r, u, d):
		self.x1 = l
		self.y1 = r
		self.x2 = u
		self.y2 = d

class Map():
	def __init__(self, pattern = [
			[1,1,1],
			[1,0,1],
			[1,1,1]
		]):
		self.pat = pattern

	def __add__(self, other):
		newPattern = [[0,0,0], [0,0,0], [0,0,0]]
		for x1, x2, indX in zip(self.pat, other.pat, range(len(other.pat))):
			for y1, y2, indY in zip(x1, x2, range(len(x2))):
				newPattern[indX][indY] = xor(y1, y2)

		return Map(newPattern)

	def __repr__(self):
		string = ""
		for x1 in self.pat:
			string += "\n"
			for y1 in x1:
				string += f"{y1}"

		return string

	@property
	def T(self):

		return self.pat[0][1]

	@property
	def B(self):

		return self.pat[2][1]

	@property
	def R(self):

		return self.pat[1][2]

	@property
	def L(self):

		return self.pat[1][0]

	@property
	def TR(self):

		return self.pat[0][2]

	@property
	def BR(self):

		return self.pat[2][2]

	@property
	def TL(self):

		return self.pat[0][0]

	@property
	def BL(self):

		return self.pat[2][0]

class Top(Map):
	def __init__(self):
		super().__init__([
			[1,1,1],
			[0,0,0],
			[0,0,0]
		])

class Down(Map):
	def __init__(self):
		super().__init__([
			[0,0,0],
			[0,0,0],
			[1,1,1]
		])

class Left(Map):
	def __init__(self):
		super().__init__([
			[1,0,0],
			[1,0,0],
			[1,0,0]
		])

class Right(Map):
	def __init__(self):
		super().__init__([
			[0,0,1],
			[0,0,1],
			[0,0,1]
		])

class TopLeft(Map):
	def __init__(self):
		super().__init__([
			[1,0,0],
			[0,0,0],
			[0,0,0]
		])

class DownLeft(Map):
	def __init__(self):
		super().__init__([
			[0,0,0],
			[0,0,0],
			[1,0,0]
		])

class TopRight(Map):
	def __init__(self):
		super().__init__([
			[0,0,1],
			[0,0,0],
			[0,0,0]
		])

class DownRight(Map):
	def __init__(self):
		super().__init__([
			[0,0,0],
			[0,0,0],
			[0,0,1]
		])
