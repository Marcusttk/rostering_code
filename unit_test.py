from roster_planner import *

# TODO need to implement a unit test for the swapping of people
people_swap = ["a", "b", "c", "d", "e", "f", "g", "h"]
test_date = [2025, 1, 1]
ooo_test = {
    "a": {"2025": {"1": {"1": 0}}},
    "b": {"2025": {"1": {"1": 0}}},
    "e": {"2025": {"1": {"1": 0}}},
    "f": {"2025": {"1": {"1": 0}}}
}
swap_one_person_start = ["f", "g", "h", "i"]
swap_one_person_end = ["aa", "ab", "c", "d", "e"]
swap_two_people1 = ["e", "f", "g", "h"]
swap_two_people2 = ["e", "y", "f", "g", "h"]
print(1)

# Example
big_list = ["a", "b", "c", "d", "e", "f", "g", "h"]
small_list = ["e", "g", "b"]

print(reorder_subset(big_list, small_list))
start_date = [2025, 9, 8]
test_file = "./FG1 OOO Calendar.ics"
main_test(start_date, test_file)
# expecting: people_to_swap: {0: {}, 1: {'Jaslynn': [[[2025, 10, 22], [2025, 10, 23]], [[2025, 10, 20], [2025, 10, 21], [2025, 10, 22], [2025, 10, 23]]]}}
