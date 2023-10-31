class Solution:
    def findArray(self, pref: List[int]) -> List[int]:
        n = len(pref)
        arr = [0] * n
        
        # To find arr[0], we know that pref[0] = arr[0] since there are no elements to XOR.
        arr[0] = pref[0]
        
        # Now, we can calculate the rest of the array elements.
        for i in range(1, n):
            # We know that pref[i] = arr[0] ^ arr[1] ^ ... ^ arr[i].
            # To find arr[i], we can use the property of XOR:
            # a ^ a = 0 for any integer a, and a ^ 0 = a for any integer a.
            # So, arr[i] = pref[i] ^ pref[i-1].
            arr[i] = pref[i] ^ pref[i-1]
        
        return arr


# You are given an integer array pref of size n. Find and return the array arr of size n that satisfies:

# pref[i] = arr[0] ^ arr[1] ^ ... ^ arr[i].
# Note that ^ denotes the bitwise-xor operation.

# It can be proven that the answer is unique.