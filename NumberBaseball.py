from itertools import permutations

base_element_list = [1, 2, 3, 4, 5, 6, 7, 8, 9]
combination_number = 3
all_combination = list(permutations(base_element_list, combination_number))


def get_strike_and_ball(combination_a, combination_b):
    strike = 0
    ball = 0
    for i in range(0, 3):
        if combination_a[i] == combination_b[i]:
            strike += 1

        if combination_a[i] == combination_b[(i + 1) % 3]:
            ball += 1

        if combination_a[i] == combination_b[(i + 2) % 3]:
            ball += 1

    return strike, ball


def get_search_space(search_space, input_combination, result):
    result_search_space = []

    for combination in all_combination:
        if (get_strike_and_ball(combination, input_combination) == result)\
                & (combination in search_space):
            result_search_space.append(combination)

    return result_search_space


def get_max_size_of_part_search_space(search_space, input_combination):
    part_search_space_lengths = []

    for i in range(0, combination_number + 1):
        for j in range(0, combination_number + 1):
            part_search_space_lengths.append(
                len(get_search_space(search_space, input_combination, (i, j)))
            )
    return max(part_search_space_lengths)


def get_best_combination(search_space):
    max_sizes = []

    for combination in all_combination:
        part_search_space_max_size = get_max_size_of_part_search_space(search_space, combination)
        max_sizes.append(part_search_space_max_size)

    best_combination_index = max_sizes.index(min(max_sizes))

    return all_combination[best_combination_index]


def main():

    temp_search_space = all_combination
    temp_combination = (1, 2, 3)

    while True:
        strike, ball = input('input strike and ball : ').split()
        strike = int(strike)
        ball = int(ball)

        temp_search_space = get_search_space(temp_search_space, temp_combination, (strike, ball))
        temp_combination = get_best_combination(temp_search_space)
        print(temp_combination)

main()