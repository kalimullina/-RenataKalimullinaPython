"""
Given an array of size n, find the most common and the least common elements.
The most common element is the element that appears more than n // 2 times.
The least common element is the element that appears fewer than other.

You may assume that the array is non-empty and the most common element
always exist in the array.

Example 1:

Input: [3,2,3]
Output: 3, 2

Example 2:

Input: [2,2,1,1,1,2,2]
Output: 2, 1

"""
from typing import List, Tuple


def major_and_minor_elem1(inp: List) -> Tuple[int, int]:
    return tuple(inp)


def major_and_minor_elem(inp: List) -> Tuple[int, int]:
    freq = {}
    for elem in inp:
        if elem in freq:
            freq[elem] += 1
        else:
            freq[elem] = 1

    most_common_elem = max(freq, key=freq.get)
    least_common_elem = min(freq, key=freq.get)
    for elem in freq:
        if freq[elem] > freq[most_common_elem]:
            most_common_elem = elem
        elif freq[elem] < freq[least_common_elem]:
            least_common_elem = elem

    if freq[most_common_elem] > len(inp) // 2:
        return most_common_elem, least_common_elem
    #else:
     #   return (None, least_common_elem)
