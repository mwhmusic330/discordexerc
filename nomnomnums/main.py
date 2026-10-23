""" A number can "eat" the number to its right if it’s larger than that number.

When it eats, it becomes the sum of both numbers.

Keep repeating this process from left to right until no more eating can happen. """

def nom_nom(example: list) -> list[int]:
    output = []
    for i in range(len(example)-1):
        if example[i] < example[i+1]:
            output.append(example[i])
        if example[i] > example[i+1]:
            sum = example[i] + example[i+1]
            output.append(sum)
            if sum > example[i+2]:
                nextsum = sum + example[i+2]
                output.append(nextsum)
                del output[0]
    print(output)



















def main():

    output = nom_nom([5, 3, 7])

    output = nom_nom([5, 3, 9])

    output = nom_nom([1, 2, 3])

    output = nom_nom([2, 1, 3])

    output = nom_nom([8, 5, 9])

    output = nom_nom([6, 5, 6, 100])



if __name__ == '__main__':
    main()

