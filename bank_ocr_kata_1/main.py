input_str = """ _  _  _  _  _  _  _  _  _
| || || || || || || || || |
|_||_||_||_||_||_||_||_||_|
                           """

def parse_input(input_string):
    lines = [line for line in input_string.split('\n')]
    return lines


def find_nums(input_string):

    lines =  parse_input(input_str)

    content = lines[:3]
    print(content)

    zero = (" _ ", "| |", "|_|")

    digits = []
    width = len(content[0]) // 3
    
    for d in range(width):
        cell = tuple(row[d * 3 : d * 3 + 3] for row in content)
        if cell == zero:
            digits.append("0")
        else:
            digits.append("?")
    return "".join(digits)


def main():
    lines =  parse_input(input_str)
    print(lines)

    result = find_nums(input_str)
    print(result)


if __name__ == '__main__':
    main()
