import random


def example(i):
    """

    :param i: i numbers after the comma
    :return: random decimal value
    """
    return f'{random.randint(1, 99) + random.random():.{i}f}'


def main():
    print()
    operators = ["-", "+", "*", "/"]
    for _ in range(25):
        sample = '[{} {} {}] [{} {} {}] [{} {} {}] [{} {} {}]'.format(example(random.randint(1, 5)),
                                                                      random.choice(operators),
                                                                      example(random.randint(1, 5)),
                                                                      example(random.randint(1, 5)),
                                                                      random.choice(operators),
                                                                      example(random.randint(1, 5)),
                                                                      example(random.randint(1, 5)),
                                                                      random.choice(operators),
                                                                      example(random.randint(1, 5)),
                                                                      example(random.randint(1, 5)),
                                                                      random.choice(operators),
                                                                      example(random.randint(1, 5))
                                                                      )
        print(sample)


if __name__ == "__main__":
    main()
