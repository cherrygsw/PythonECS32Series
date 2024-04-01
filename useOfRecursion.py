def smallest(elements):
    # if the list is down to one element, that's the smallest
    if len(elements) == 1:
        return elements[0]
    # compare the first element with the smallest of the rest
    min_of_rest = smallest(elements[1:])
    return elements[0] if elements[0] < min_of_rest else min_of_rest

def linearSearchValueIndexEqual(arr):
    matches = []  # list to hold matching indices
    for idx in range(len(arr)):
        # add index if it matches the element
        if idx == arr[idx]:
            matches.append(idx)
    return matches

def binarySearchValueIndexEqual(arr):
    def find_matches(low, high):
        if low > high:
            return []
        
        mid = (low + high) // 2
        match_found = []
        
        # check match at mid position
        if mid == arr[mid]:
            match_found = [mid]
        
        # search left and right halves, including mid if match is found
        left_matches = find_matches(low, mid - 1)
        right_matches = find_matches(mid + 1, high)
        
        # combine all matches found
        return left_matches + match_found + right_matches
    
    # initiate recursive search
    return find_matches(0, len(arr) - 1)

def ladder(steps):
    # base case: 0 or 1 step has only 1 way to climb
    if steps <= 1:
        return 1
    # recursive case: sum of ways to climb the last two steps
    return ladder(steps - 1) + ladder(steps - 2)