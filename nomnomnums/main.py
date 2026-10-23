""" A number can "eat" the number to its right if it’s larger than that number.

When it eats, it becomes the sum of both numbers.

Keep repeating this process from left to right until no more eating can happen. """

def nom_nom(example: list): ->



















def main():
    output = nom_nom([5, 3, 7])

    nom_nom([5, 3, 9])

    nom_nom([1, 2, 3])

    nom_nom([2, 1, 3])

    nom_nom([8, 5, 9])

    nom_nom([6, 5, 6, 100])



if __name__ == '__main__':
    main()

