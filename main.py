# Check if 2 strings are anagrams(built from same letters)
# Answer 1
def check_if_strings_anagrams_1(string1, string2):
    sorted_string1_list = sorted(list(string1))
    sorted_string2_list = sorted(list(string2))
    if len(string1) == len(string2):
        if sorted_string1_list == sorted_string2_list:
            return True
    return False


def check_if_strings_anagrams_2(string1, string2):
    if len(string1) == len(string2):
        for letter in string1:
            if letter not in string2:
                return False
        return True
    return False


def check_if_strings_anagrams_3(string1, string2):
    string1_dict = {}
    string2_dict = {}
    if len(string1) == len(string2):
        for character in string1:
            if character in string1_dict:
                string1_dict[character] += 1
            else:
                string1_dict[character] = 1
        for character in string2:
            if character in string2_dict:
                string2_dict[character] += 1
            else:
                string2_dict[character] = 1
        print(string1_dict)
        print(string2_dict)
        for key, value in string1_dict.items():
            if key not in string2_dict or string2_dict[key] != value:
                return False
            return True
    return False


def find_indexes(target, arr):
    target_index = []
    for index, n in enumerate(arr):
        if str(target) in str(n):
            target_index.append(index)
    if len(target_index) == 1 or len(target_index) == 0:
        result = [-1, -1]
    else:
        result = [target_index[0], target_index[-1]]
    return result


def find_indexes_2(target, arr):
    for i in range(len(arr)):
        if arr[i] == target:
            start = i
            while i+1 < len(arr) and arr[i+1] == target:
                i += 1
            return [start, i]
    return [-1, -1]


def total_sum_to_index(arr):
    sum = 0
    for i in range(len(arr)):
        sum += arr[i]
        if i+1 < len(arr) and sum == arr[i+1]:
            return i


def valid_phantasies(string):
    open_count = 0
    close_count = 0
    open_pattern = "("
    close_pattern = ")"
    for ch in string:
        if ch == open_pattern:
            open_count += 1
        if ch == close_pattern:
            close_count += 1
        if close_count > open_count:
            return False
    return True


if __name__ == "__main__":
    # 1 check if 2 words are anagram(same letters)
    string_1 = "dangeraa"
    string_2 = "gardenaa"
    print(check_if_strings_anagrams_1(string_1, string_2))
    print(check_if_strings_anagrams_2(string_1, string_2))
    print(check_if_strings_anagrams_3(string_1, string_2))

    # 2 First and last index of target in sorted array if not found return [-1, -1]
    target = 4
    arr = [2, 4, 5, 5, 5, 5, 5, 7, 9, 9]
    print(find_indexes(target, arr))
    print(find_indexes_2(target, arr))

    # 3 find the index that equa; to sum of the nums until it
    array_new = [0, 2, 4, 2, 2, 0, 0, 10, 0, 11, 98]
    print(f"index of sum: {total_sum_to_index(array_new)}")

    # 4 check if phantasies valid
    phantasies_arr = ")()()()()"
    print(valid_phantasies(phantasies_arr))
    print("BIG CONFLICT")
