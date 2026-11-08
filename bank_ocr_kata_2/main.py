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
        digits.append(digit_map.get(cell, "?"))### type:ignore
        
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
    for i, acct_num in enumerate(test_cases):
      lines =  parse_input(acct_num)
      result = find_nums(acct_num)

      test = checksum(result)
      if "?" in result:
          final_output = f"{result} ILL"
      else:
          final_output = f"{result} {test}"
      print(final_output.strip())
    

if __name__ == '__main__':
    main()
