import re
def part1() -> None:
	def hasOverlap(low1: int, high1: int, low2: int, high2: int):
		def overlap(low1: int, high1: int, low2: int, high2: int):
			return (low1 <= low2 and high1 >= high2)
		return (overlap(low1, high1, low2, high2) or overlap(low2, high2, low1, high1))
	with open("input.txt", "rb") as f:
		count: int = 0
		for line in f:
			line = re.split(",|-", line.decode().strip())
			line = list(map(int, line))
			print(line)
			if hasOverlap(line[0], line[1], line[2], line[3]):
				print(line)
				count += 1
		print(count)

def part2()-> None:
	def hasOverlap(low1: int, high1: int, low2: int, high2: int):
		def overlap(low1: int, high1: int, low2: int, high2: int):
			return ((low1 <= low2 and high1 >= low2) or (high1 >= high2 and low1 <= high2))
		return (overlap(low1, high1, low2, high2) or overlap(low2, high2, low1, high1))
	with open("input.txt", "rb") as f:
		count: int = 0
		for line in f:
			line = re.split(",|-", line.decode().strip())
			line = list(map(int, line))
			if hasOverlap(line[0], line[1], line[2], line[3]):
				print(line)
				count += 1
		print(count)

part2()