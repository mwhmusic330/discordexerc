""" A number can "eat" the number to its right if it’s larger than that number.

When it eats, it becomes the sum of both numbers.

Keep repeating this process from left to right until no more eating can happen. """


def nom_nom(example: list) -> list[int]:
    output = []
    current = example[0]
    for i in range(1, len(example)):
        if current > example[i]:
            current = current + example[i]
        else:
            output.append(current)
            current = example[i]
    output.append(current)

    return output


def main():

    output = nom_nom([5, 3, 7])
    print(output)

    output = nom_nom([5, 3, 9])
    print(output)

    output = nom_nom([1, 2, 3])
    print(output)

    output = nom_nom([2, 1, 3])
    print(output)

    output = nom_nom([8, 5, 9])
    print(output)

    output = nom_nom([6, 5, 6, 100])
    print(output)


if __name__ == '__main__':
    main()

