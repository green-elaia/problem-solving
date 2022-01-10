import itertools
import copy


def num_to_opts(l: list):
    ret = []
    ret += ["+"] * l[0]
    ret += ["-"] * l[1]
    ret += ["*"] * l[2]
    ret += ["/"] * l[3]
    return ret


def calc_nums(n1, n2, opt):
    ret = None
    if opt == "+":
        ret = n1 + n2
    elif opt == "-":
        ret = n1 - n2
    elif opt == "*":
        ret = n1 * n2
    elif opt == "/":
        if n1 < 0:
            n1 = -n1
            ret = -(n1 // n2)
        else:
            ret = n1 // n2
    return ret


def calc_max_min(numbers: list, operators: list):
    ret = []
    for opts in itertools.permutations(operators, len(operators)):
        num_copy = copy.deepcopy(numbers)
        for opt in opts:
            n1 = num_copy.pop(0)
            n2 = num_copy.pop(0)
            n = calc_nums(n1, n2, opt)
            num_copy.insert(0, n)
        else:
            ret.append(num_copy[0])

    return max(ret), min(ret)


if __name__ == "__main__":
    #     input = """6
    # 1 2 3 4 5 6
    # 2 1 1 1"""
    #     input = """3
    # 3 4 5
    # 1 0 1 0"""
    input = """2
5 6
0 0 1 0"""
    input_list = [int(x) for x in input.split()]
    numbers = input_list[1 : 1 + input_list[0]]
    operators = input_list[1 + input_list[0] :]
    operators = num_to_opts(operators)
    max, min = calc_max_min(numbers, operators)
    print(max, min)
