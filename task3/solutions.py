"""Task 3: Python Coding & Problem-Solving
Contains reusable functions for all 15 questions.
"""


# Q1. Find the Frequency of Each Word in a Sentence
def word_frequency(sentence):
    """Return a dictionary containing each word's frequency, in first-seen order."""
    counts = {}
    for word in sentence.split():
        word = word.lower()
        counts[word] = counts.get(word, 0) + 1
    return counts


# Q2. Find the Frequency of Each Character in a Word
def character_frequency(word):
    """Return a dictionary containing each character's frequency."""
    counts = {}
    for character in word:
        counts[character] = counts.get(character, 0) + 1
    return counts


# Q3. Find the First Non-Repeating Character in a Word
def first_non_repeating_character(word):
    """Return the first character occurring once, or None if there is no such character."""
    counts = character_frequency(word)
    for character in word:
        if counts[character] == 1:
            return character
    return None


# Q4. Check Whether Two Strings Are Anagrams
def are_anagrams(s1, s2):
    """Return True when both strings have the same character frequencies."""
    return character_frequency(s1) == character_frequency(s2)


# Q5. Find the First Repeating Character in a String
def first_repeating_character(text):
    """Return the character whose second occurrence is first encountered, or None."""
    seen = set()
    for character in text:
        if character in seen:
            return character
        seen.add(character)
    return None


# Q6. Move All Zeros to the End of a List
def move_zeros_to_end(nums):
    """Return a new list with non-zero elements in order followed by all zeros."""
    non_zeros = [number for number in nums if number != 0]
    zeros = [number for number in nums if number == 0]
    return non_zeros + zeros


# Q7. Find the Second Highest Distinct Number in a List
def second_highest_distinct(nums):
    """Return the second-largest distinct number, or None if it does not exist."""
    distinct = sorted(set(nums), reverse=True)
    return distinct[1] if len(distinct) >= 2 else None


# Q8. Remove Duplicates Without Changing the Original Order
def remove_duplicates_preserve_order(items):
    """Return unique items in the order of their first appearance."""
    result = []
    seen = set()
    for item in items:
        if item not in seen:
            result.append(item)
            seen.add(item)
    return result


# Q9. Find the Missing Number from 1 to N
def find_missing_number(nums, n):
    """Return the missing number from 1..n using the expected-sum formula."""
    expected_sum = n * (n + 1) // 2
    return expected_sum - sum(nums)


# Q10. Find Two Numbers Whose Sum Equals a Target
def two_sum_first_pair(nums, target):
    """Return the first qualifying pair by scan order, or an empty list."""
    seen = set()
    for number in nums:
        needed = target - number
        if needed in seen:
            # The earlier matching value was encountered before this number.
            return [needed, number]
        seen.add(number)
    return []


# Q11. Find the Number Closest to Zero
def closest_to_zero(nums):
    """Return the value closest to zero; prefer the positive value on a tie."""
    if not nums:
        return None
    return min(nums, key=lambda number: (abs(number), -number))


# Q12. Find Common Elements Between Two Lists
def common_elements(list1, list2):
    """Return unique common elements in the order they first occur in list1."""
    second_set = set(list2)
    result = []
    seen = set()
    for item in list1:
        if item in second_set and item not in seen:
            result.append(item)
            seen.add(item)
    return result


# Q13. Rotate a List to the Right by K Positions
def rotate_right(nums, k):
    """Return a list rotated right by k positions; handle k larger than its length."""
    if not nums:
        return []
    k %= len(nums)
    if k == 0:
        return nums[:]
    return nums[-k:] + nums[:-k]


# Q14. Find the Maximum Sum of Two Consecutive Elements
def max_consecutive_pair_sum(nums):
    """Return the maximum sum of adjacent elements; assumes at least two elements."""
    if len(nums) < 2:
        raise ValueError("At least two elements are required.")
    return max(nums[index] + nums[index + 1] for index in range(len(nums) - 1))


# Q15. Find All Pairs of Numbers Whose Sum Equals a Target
def all_unique_pairs_sum(nums, target):
    """Return unique value pairs summing to target, each ascending and sorted."""
    values = set(nums)
    pairs = set()
    for number in nums:
        other = target - number
        if other in values and other != number:
            pairs.add(tuple(sorted((number, other))))
        elif other == number and nums.count(number) >= 2:
            pairs.add((number, number))
    return [list(pair) for pair in sorted(pairs)]
