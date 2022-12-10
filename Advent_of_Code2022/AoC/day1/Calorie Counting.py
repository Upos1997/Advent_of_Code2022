def main():
    with open("input.txt", "rb") as f:
        top3 = [0, 0, 0]
        current_elf = 0

        for line in f:
            line = line.decode().strip()
            if line == "":
                for top in range(3):
                    if current_elf > top3[top]:
                        top3.insert(top, current_elf)
                        top3 = top3[:-1]
                        break
                current_elf = 0
            else:
                current_elf += int(line)
        print(sum(top3))


if __name__ == "__main__":
    main()
