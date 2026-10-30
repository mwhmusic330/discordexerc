input_str = """ _  _  _  _  _  _  _  _  _
| || || || || || || || || |
|_||_||_||_||_||_||_||_||_|
                           """

def parse_input(input_string):
    lines = [line.strip() for line in input_string.split('\n')]
    return lines

lines =  parse_input(input_str)
print(lines)
