input_str = """ _  _  _  _  _  _  _  _  _
| || || || || || || || || |
|_||_||_||_||_||_||_||_||_|
                           """

def parse_input(input_string):
    lines = [line.strip() for line in input_string.split('\n')]
    return lines


def find_nums(input_string):
    lines =  parse_input(input_str)
    print(lines)

    content = lines[:3]
    print(content)

    zero = (" _ ", "| |", "|_|")

    digits = []
    width = len(content[0]) // 3


def main():
    result = find_nums(input_str)
    print(result)


if __name__ == '__main__':
    main()
