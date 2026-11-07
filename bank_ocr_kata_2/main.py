""" _  _  _  _  _  _  _  _  _

| || || || || || || || || |
|_||_||_||_||_||_||_||_||_|
                           """

"""                           
  |  |  |  |  |  |  |  |  |
  |  |  |  |  |  |  |  |  |
                           """
""" _  _  _  _  _  _  _  _  _ 
 _| _| _| _| _| _| _| _| _|
|_ |_ |_ |_ |_ |_ |_ |_ |_ 
                           """
""" _  _  _  _  _  _  _  _  _ 
 _| _| _| _| _| _| _| _| _|
 _| _| _| _| _| _| _| _| _|
                           """
"""                           
|_||_||_||_||_||_||_||_||_|
  |  |  |  |  |  |  |  |  |
                           """
""" _  _  _  _  _  _  _  _  _ 
|_ |_ |_ |_ |_ |_ |_ |_ |_ 
 _| _| _| _| _| _| _| _| _|
                           """
""" _  _  _  _  _  _  _  _  _ 
|_ |_ |_ |_ |_ |_ |_ |_ |_ 
|_||_||_||_||_||_||_||_||_|
                           """
""" _  _  _  _  _  _  _  _  _ 
  |  |  |  |  |  |  |  |  |
  |  |  |  |  |  |  |  |  |
                           """
""" _  _  _  _  _  _  _  _  _ 
|_||_||_||_||_||_||_||_||_|
|_||_||_||_||_||_||_||_||_|
                           """
""" _  _  _  _  _  _  _  _  _ 
|_||_||_||_||_||_||_||_||_|
 _| _| _| _| _| _| _| _| _|
                           """
"""    _  _     _  _  _  _  _ 
  | _| _||_||_ |_   ||_||_|
  ||_  _|  | _||_|  ||_| _
                           """  
""" _  _  _  _  _  _  _  _    
| || || || || || || ||_   |
|_||_||_||_||_||_||_| _|  |
                           """
"""    _  _  _  _  _  _     _ 
|_||_|| || ||_   |  |  | _ 
  | _||_||_||_|  |  |  | _|
                           """
input_str = """    _  _     _  _  _  _  _ 
  | _| _||_| _ |_   ||_||_|
  ||_  _|  | _||_|  ||_| _ 
                            """
def parse_input(input_string):
    lines = [line for line in input_string.split('\n')]
    return lines


def find_nums(input_string):

    lines =  parse_input(input_str)

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
        digits.append(digit_map.get(cell, "?"))### type:ignore
    print(digits)
        
    return "".join(digits)

def checksum(result):
    rev_result = result[::-1]
    total = 0
    for i, digit in enumerate(rev_result, 1):
        if digit.isdigit():
            total += i*int(digit)
        else:
            return " "
    if total % 11 == 0:
        return " "
    else:
        return "ERR"
def main():

    lines =  parse_input(input_str)

    

    result = find_nums(input_str)
    print(result)

    test = checksum(result)
    print(test)
    if "?" in result:
        print(f"{result} ILL")
    else:
        print(f"{result} {test}")
    

if __name__ == '__main__':
    main()
