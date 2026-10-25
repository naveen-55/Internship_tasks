"""Run all Task 3 functions with the assignment examples and extra test cases."""

from solutions import (
    word_frequency,
    character_frequency,
    first_non_repeating_character,
    are_anagrams,
    first_repeating_character,
    move_zeros_to_end,
    second_highest_distinct,
    remove_duplicates_preserve_order,
    find_missing_number,
    two_sum_first_pair,
    closest_to_zero,
    common_elements,
    rotate_right,
    max_consecutive_pair_sum,
    all_unique_pairs_sum,
)


def show(question, function, *args):
    print(f"Q{question}: {function(*args)}")


if __name__ == "__main__":
    print("=== Assignment examples ===")
    show(1, word_frequency, "python is easy and python is powerful")
    show(2, character_frequency, "banana")
    show(3, first_non_repeating_character, "swiss")
    show(4, are_anagrams, "listen", "silent")
    show(5, first_repeating_character, "programming")
    show(6, move_zeros_to_end, [0, 3, 0, 1, 2, 0, 4])
    show(7, second_highest_distinct, [10, 20, 40, 30, 40, 20])
    show(8, remove_duplicates_preserve_order, [4, 2, 4, 5, 2, 7, 5])
    show(9, find_missing_number, [1, 2, 4, 5, 6], 6)
    show(10, two_sum_first_pair, [2, 7, 11, 15], 9)
    show(11, closest_to_zero, [-8, -3, 2, 5, -2])
    show(12, common_elements, [1, 2, 3, 4, 5], [3, 4, 5, 6, 7])
    show(13, rotate_right, [1, 2, 3, 4, 5], 2)
    show(14, max_consecutive_pair_sum, [4, 7, 2, 9, 5])
    show(15, all_unique_pairs_sum, [2, 4, 3, 5, 7, 8, 1], 9)

    print("\\n=== Additional test cases ===")
    show(1, word_frequency, "red blue red")
    show(2, character_frequency, "level")
    show(3, first_non_repeating_character, "aabbc")
    show(4, are_anagrams, "Dormitory", "Dirtyroom")  # case-sensitive by design
    show(5, first_repeating_character, "abcdefa")
    show(6, move_zeros_to_end, [1, 0, 2, 0, 3])
    show(7, second_highest_distinct, [5, 5, 5])
    show(8, remove_duplicates_preserve_order, ["a", "b", "a", "c"])
    show(9, find_missing_number, [1, 3, 4], 4)
    show(10, two_sum_first_pair, [1, 4, 2, 3], 5)
    show(11, closest_to_zero, [-4, 4, -1, 1])
    show(12, common_elements, [3, 1, 3, 2], [2, 3, 3])
    show(13, rotate_right, [1, 2, 3], 5)
    show(14, max_consecutive_pair_sum, [-5, -2, -8])
    show(15, all_unique_pairs_sum, [1, 1, 2, 2, 3, 4], 4)
