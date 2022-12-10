import math

def getPriority(item: str) -> int:
			item = ord(item)
			if (item < 97):
				return item-38
			else:
				return item-96

def step1():
	def find_same(rucksack: str) -> int:
		length = len(rucksack)
		compartment1 = {rucksack[x] for x in range(math.floor(length/2))}
		compartment2 = {rucksack[x] for x in range(math.floor(length/2), length)}
		print(compartment1)
		print(compartment2)
		print(f"0-{math.floor((length/2))-1}|{math.floor(length/2)}-{length}")
		identical = compartment1.intersection(compartment2)
		print(identical)
		identical: set(int) = map(getPriority, identical)
		return sum(identical)

	with open("input.txt", "rb") as f:
		priority: int = 0
		for line in f:
			line = line.decode().strip()
			priority += find_same(line)
		print(priority)

def step2():
	with open("input.txt", "rb") as f:
		priority: int = 0
		while True:
			def getset() -> str:
				return {x for x in f.readline().decode().strip()}
			line1 = getset()
			line2= getset()
			line3= getset()
			if (len(line1)):
				duplicate = map(getPriority, line1.intersection(line2).intersection(line3))
				priority += sum(duplicate)
			else:
				break
		print(priority)

step2()