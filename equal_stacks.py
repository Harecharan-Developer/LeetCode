# You have three stacks of cylinders where each cylinder has the same diameter, but they may vary in height. You can change the height of a stack by removing and discarding its topmost cylinder any number of times.

# Find the maximum possible height of the stacks such that all of the stacks are exactly the same height. This means you must remove zero or more cylinders from the top of zero or more of the three stacks until they are all the same height, then return the height.

# Example


# hl [1, 2, 1, 1]
#h2=[1, 1, 2]
# h3 [1, 1]

# There are 4 3 and 2 cylinders in the three stacks, with their heights in the three arrays. Remove the top 2 cylinders from h1 (heights = [1, 2]) and from h2 (heights = [1, 1]) so that the three stacks all are 2 units tall. Return 2 as the answer.


def equalStacks(h1, h2, h3):
    # Reverse the input lists to efficiently pop from the top
    h1.reverse()
    h2.reverse()
    h3.reverse()

    # Calculate the cumulative heights of each stack
    cum_height_h1 = [0] + [sum(h1[:i + 1]) for i in range(len(h1))]
    cum_height_h2 = [0] + [sum(h2[:i + 1]) for i in range(len(h2))]
    cum_height_h3 = [0] + [sum(h3[:i + 1]) for i in range(len(h3))]

    # Initialize pointers at the end of each cumulative height list
    i, j, k = len(cum_height_h1) - 1, len(cum_height_h2) - 1, len(cum_height_h3) - 1

    # Iterate until a common height is found or one of the lists is exhausted
    while i > 0 and j > 0 and k > 0:
        # Find the minimum common height among the three stacks
        common_height = min(cum_height_h1[i], cum_height_h2[j], cum_height_h3[k])

        # If the common height is found, return it
        if cum_height_h1[i] == cum_height_h2[j] == cum_height_h3[k]:
            return common_height

        # Move the pointer of the list with a greater cumulative height towards the common height
        while cum_height_h1[i] > common_height:
            i -= 1
        while cum_height_h2[j] > common_height:
            j -= 1
        while cum_height_h3[k] > common_height:
            k -= 1

    # If no common height is found, return 0
    return 0