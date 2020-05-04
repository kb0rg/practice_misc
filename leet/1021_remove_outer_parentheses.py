"""
1021. Remove Outermost Parentheses
https://leetcode.com/problems/remove-outermost-parentheses/

A valid parentheses string is either empty (""), "(" + A + ")", or A + B,
where A and B are valid parentheses strings, and + represents string
concatenation.

For example, "", "()", "(())()", and "(()(()))" are all valid parentheses
strings.

A valid parentheses string S is primitive if it is nonempty, and there does not
exist a way to split it into S = A+B, with A and B nonempty valid parentheses
strings.

Given a valid parentheses string S, consider its primitive decomposition:
S = P_1 + P_2 + ... + P_k, where P_i are primitive valid parentheses strings.

Return S after removing the outermost parentheses of every primitive string in
the primitive decomposition of S.


Example 1:

Input: "(()())(())"
Output: "()()()"
Explanation:
The input string is "(()())(())", with primitive decomposition "(()())" + "(())".
After removing outer parentheses of each part, this is "()()" + "()" = "()()()".

Example 2:

Input: "(()())(())(()(()))"
Output: "()()()()(())"
Explanation:
The input string is "(()())(())(()(()))", with primitive decomposition
"(()())" + "(())" + "(()(()))".
After removing outer parentheses of each part, this is
"()()" + "()" + "()(())" = "()()()()(())".

Example 3:

Input: "()()"
Output: ""
Explanation:
The input string is "()()", with primitive decomposition "()" + "()".
After removing outer parentheses of each part, this is "" + "" = "".


Note:

S.length <= 10000
S[i] is "(" or ")"
S is a valid parentheses string
"""

class Solution:
    def removeOuterParentheses(self, S: str) -> str:
        return_substrings = []

        substring_stack = []
        start_index = 0
        end_index = 0
        current_index = 0

        # check for valid primitives by looking for complete sets of "()" chars
        for char in S:
            if char == "(":
                if not len(substring_stack):
                    start_index = current_index
                substring_stack.append(char)
            else:
                if substring_stack[-1] == "(":
                    substring_stack.pop()

            if not len(substring_stack):
                # once I've identified a valid primitive, strip the outer char
                # and add it to a list
                return_substrings.append(S[start_index + 1: end_index])
                start_index = end_index + 1

            end_index += 1
            current_index += 1

        # return remaining substrings as a string
        return "".join(return_substrings)
