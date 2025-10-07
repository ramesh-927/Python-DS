Leetcode 5 : longest palindromic substring in s. 
To find the longest palindromic substring efficiently, we can use the Expand Around Center approach. This is optimal for this problem because it avoids checking all possible substrings (which would be O(n^3) with naive palindrome checks) and leverages the fact that palindromes expand symmetrically around a center.
Reasoning
Palindrome Structure: A palindrome can have:

An odd length (e.g., "aba", centered at b).
An even length (e.g., "bb", centered between the two b’s).


Expand Around Center:

For each position i in the string, treat i as the center of a potential odd-length palindrome and expand outwards.
Also treat the space between i and i+1 as the center of a potential even-length palindrome and expand outwards.
Check characters on both sides to ensure they match, expanding as long as possible.


Track Maximum: Keep track of the longest palindrome found by storing its starting index and length.
Edge Cases:

Single-character strings (return the character).
Strings with no palindromes longer than 1 (return any single character).
Strings with repeated characters (e.g., "aaa" returns "aaa").