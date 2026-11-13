test_cases = [
""" _  _  _  _  _  _  _  _  _
| || || || || || || || || |
|_||_||_||_||_||_||_||_||_|
                           """,

"""                           
  |  |  |  |  |  |  |  |  |
  |  |  |  |  |  |  |  |  |
                           """,
""" _  _  _  _  _  _  _  _  _ 
 _| _| _| _| _| _| _| _| _|
|_ |_ |_ |_ |_ |_ |_ |_ |_ 
                           """,
""" _  _  _  _  _  _  _  _  _ 
 _| _| _| _| _| _| _| _| _|
 _| _| _| _| _| _| _| _| _|
                           """,
"""                           
|_||_||_||_||_||_||_||_||_|
  |  |  |  |  |  |  |  |  |
                           """,
""" _  _  _  _  _  _  _  _  _ 
|_ |_ |_ |_ |_ |_ |_ |_ |_ 
 _| _| _| _| _| _| _| _| _|
                           """,
""" _  _  _  _  _  _  _  _  _ 
|_ |_ |_ |_ |_ |_ |_ |_ |_ 
|_||_||_||_||_||_||_||_||_|
                           """,
""" _  _  _  _  _  _  _  _  _ 
  |  |  |  |  |  |  |  |  |
  |  |  |  |  |  |  |  |  |
                           """,
""" _  _  _  _  _  _  _  _  _ 
|_||_||_||_||_||_||_||_||_|
|_||_||_||_||_||_||_||_||_|
                           """,
""" _  _  _  _  _  _  _  _  _ 
|_||_||_||_||_||_||_||_||_|
 _| _| _| _| _| _| _| _| _|
                           """,
"""    _  _     _  _  _  _  _ 
  | _| _||_||_ |_   ||_||_|
  ||_  _|  | _||_|  ||_| _
                           """,
""" _  _  _  _  _  _  _  _    
| || || || || || || ||_   |
|_||_||_||_||_||_||_| _|  |
                           """,
"""    _  _  _  _  _  _     _ 
|_||_|| || ||_   |  |  | _ 
  | _||_||_||_|  |  |  | _|
                           """,
"""    _  _     _  _  _  _  _ 
  | _| _||_| _ |_   ||_||_|
  ||_  _|  | _||_|  ||_| _ 
                            """]
def parse_input(acct):
    lines = [line for line in acct.split('\n')]
    return lines


def find_nums(acct):

    lines =  parse_input(acct)

    content = lines[:3]

    digit_map = {(" _ ", "| |", "|_|"): "0",
                 ("   ", "  |", "  |"): "1",
                 (" _ ", " _|", "|_ "): "2",
                 (" _ ", " _|", " _|"): "3",
                 ("   ", "|_|", "  |"): "4",
                 (" _ ", "|_ ", " _|"): "5",
                 (" _ ", "|_ ", "|_|"): "6",
                 (" _ ", "  |", "  |"): "7",
                 (" _ ", "|_|", "|_|"): "8",
                 (" _ ", "|_|", " _|"): "9"}


    digits = []
    width = len(content[0]) // 3

    for d in range(width):
        d  = d*3
        cell = tuple(row[d : d + 3] for row in content)
        print(cell)
        digits.append(digit_map.get(cell, "?"))### type:ignore

    return "".join(digits)

def check_cell(acct):

    lines =  parse_input(acct)

    content = lines[:3]

    digit_map = {(" _ ", "| |", "|_|"): "0",
                 ("   ", "  |", "  |"): "1",
                 (" _ ", " _|", "|_ "): "2",
                 (" _ ", " _|", " _|"): "3",
                 ("   ", "|_|", "  |"): "4",
                 (" _ ", "|_ ", " _|"): "5",
                 (" _ ", "|_ ", "|_|"): "6",
                 (" _ ", "  |", "  |"): "7",
                 (" _ ", "|_|", "|_|"): "8",
                 (" _ ", "|_|", " _|"): "9"}
    ascii_nums = []

    for i in range(0,27,3):
        digit_grid = [line[i: i + 3] for line in content]
        ascii_nums.append(digit_grid)
    test_digit = ascii_nums[0]
    mutable_grid = [list(row) for row in test_digit]
    mutable_grid[0][1] = "-"
    updated_grid = ["".join(row) for row in mutable_grid]
    print(updated_grid)
    return ascii_nums



def checksum(result):
    rev_result = result[::-1]
    total = 0
    for i, digit in enumerate(rev_result, 1):
        total += i*int(digit)
    return total % 11 == 0


def main():
    for acct_num in test_cases:
        result = find_nums(acct_num)

        if "?" in result:
            final_output = f"{result} ILL"
        else:
            test ="" if checksum(result) else "ERR" 
            final_output = f"{result} {test}"
        print(final_output.strip())

if __name__ == '__main__':
    main()
    example = test_cases[10]
    lines = parse_input(example)
    content = lines[:3]
    print(content[0][1])
    test = check_cell(example)
    print(test[3])
