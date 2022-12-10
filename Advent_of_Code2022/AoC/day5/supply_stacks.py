stacks = [['T', 'D', 'W', 'Z', 'V', 'P'],
                ['L', 'S', 'W', 'V', 'F', 'J', 'D'],
                ['Z', 'M', 'L', 'S', 'V', 'T', 'B', 'H'],
                ['R', 'S', 'J'],
                ['C', 'Z', 'B', 'G', 'F', 'M', 'L', 'W'],
                ['Q', 'W', 'V', 'H', 'Z', 'R', 'G', 'B'],
                ['V', 'J', 'P', 'C', 'B', 'D', 'N'],
                ['P', 'T', 'B', 'Q'],
                ['H', 'G', 'Z', 'R', 'C']]

def stack_pop(stack: int) -> str:
        return stacks[stack-1].pop()

def multi_pop(stack: int, amount: int)-> list[str]:
    list = []
    for x in range(amount):
        list.insert(0, stack_pop(stack))
    return list

def stack_put(stack: int, element: str) -> None:
        stacks[stack-1].append(element)

def multi_put(stack: int, elements: list[str]) -> None:
    stacks[stack-1].extend(elements)

def move1(amount: int, start_stack: int, stop_stack: int) -> None:
        def move_one() -> None:
            stack_put(stop_stack, stack_pop(start_stack))
        for x in range(amount):
            move_one()

def move2(amount: int, start_stack: int, stop_stack: int) -> None:
    multi_put(stop_stack, multi_pop(start_stack, amount))
    

with open("AoC/day5/input.txt", "rb") as f:
    for line in f:
        line = line.decode().strip().split(" ")
        print(line)
        move2(int(line[1]), int(line[3]), int(line[5]))
    for stack in stacks:
        print(stack.pop())