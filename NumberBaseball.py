from itertools import permutations

base_element_list = [1, 2, 3, 4, 5, 6, 7, 8, 9]
combination_number = 3
all_combination = list(permutations(base_element_list, combination_number))
all_combination_length = len(all_combination)


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


def get_part_search_space(search_space_binary, input_combination, result):
    result_search_space_binary = []

    for index in range(0, all_combination_length):
        if (search_space_binary[index] == 1) & (get_strike_and_ball(all_combination[index], input_combination) == result):
            result_search_space_binary.append(1)
        else:
            result_search_space_binary.append(0)

    return result_search_space_binary


def get_search_space_length(search_space):
    count = 0
    for i in search_space:
        if i == 1:
            count += 1

    return count


def get_max_size_of_part_search_space(search_space_binary, input_combination):
    part_search_space_lengths = []

    for i in range(0, combination_number + 1):
        for j in range(0, combination_number + 1):
            part_search_space_lengths.append(
                get_search_space_length(get_part_search_space(search_space_binary, input_combination, (i, j)))
            )

    return max(part_search_space_lengths)


def get_best_combination(search_space_binary):
    max_sizes = []

    for combination in all_combination:
        max_sizes.append(get_max_size_of_part_search_space(search_space_binary, combination))

    best_combination_max_size = min(max_sizes)
    temp_best_combination_index = max_sizes.index(best_combination_max_size)
    for index in range(len(max_sizes)):
        if (max_sizes[index] is best_combination_max_size) & search_space_binary[index] is 1:
            return all_combination[index]

    return all_combination[temp_best_combination_index]


def get_answer(initial_combination):

    temp_search_space_binary = []
    for i in range(0, all_combination_length):
        temp_search_space_binary.append(1)

    temp_combination = initial_combination

    while True:
        strike, ball = input('input strike and ball : ').split()
        strike = int(strike)
        ball = int(ball)
        temp_search_space_binary = get_part_search_space(temp_search_space_binary, temp_combination, (strike, ball))

        if get_search_space_length(temp_search_space_binary) == 1:
            return all_combination[temp_search_space_binary.index(1)]

        temp_combination = get_best_combination(temp_search_space_binary)
        print(temp_combination)


def main():
    print('made by CodingHelper in Elysium')
    while True:
        initial_combination = (1, 2, 3)
        print('initial combination : ', end='')
        print(initial_combination)

        answer = get_answer(initial_combination)

        print('answer', end='')
        print(answer)

        print('one more time?[y/n]')
        one_more_time = input()
        if not one_more_time == 'y':
            return

main()
