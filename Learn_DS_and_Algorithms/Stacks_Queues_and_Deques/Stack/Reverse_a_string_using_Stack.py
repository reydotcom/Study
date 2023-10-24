# Reverse a string using Stack
# Source: https://practice.geeksforgeeks.org/problems/reverse-a-string-using-stack/1

# You are given a string S, the task is to reverse the string using stack.

# Example 1:

# Input: S = "GeeksforGeeks"
# Output: skeeGrofskeeG

# Your Task:
# You don't need to read input or print anything. Your task is to complete the function reverse()
# which takes the string S as an input parameter and returns the reversed string.

# Expected Time Complexity: O(N)
# Expected Auxiliary Space: O(N)

# Constraints: 1 ≤ length of the string ≤ 100


# The function takes a string and returns the reversed string
def reverse(s: str):
    stack = []   # Creating a stack.
    r_str = ''   # Creating a reversed string.

    # Adding all letters to a stack
    for letter in s:
        stack.append(letter)

    # Taking all letters from the stack.
    while stack:
        for letter in stack.pop():
            r_str += letter

    return r_str


# Driver Code Starts.
if __name__ == '__main__':
    t = int(input())
    for i in range(t):
        str1 = input()
        print(reverse(str1))
