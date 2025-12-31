"""
Docstring for FacebookInterview.LeetCodeSolutions.01-ArrayAndStrings.20-468.ValidateIPAddress

Given a string queryIP, return "IPv4" if IP is a valid IPv4 address, "IPv6" if IP is a valid 
IPv6 address or "Neither" if IP is not a correct IP of any type.
A valid IPv4 address is an IP in the form "x1.x2.x3.x4" where 0 <= xi <= 255 and xi cannot contain 
leading zeros. For example, "192.168.1.1" and "192.168.1.0" are valid IPv4 addresses while 
"192.168.01.1", "192.168.1.00", and "192.168@1.1" are invalid IPv4 addresses.

A valid IPv6 address is an IP in the form "x1:x2:x3:x4:x5:x6:x7:x8" where:
1 <= xi.length <= 4
xi is a hexadecimal string which may contain digits, lowercase English letter ('a' to 'f') and 
upper-case English letters ('A' to 'F').

Leading zeros are allowed in xi.

For example, "2001:0db8:85a3:0000:0000:8a2e:0370:7334" and "2001:db8:85a3:0:0:8A2E:0370:7334" 
are valid IPv6 addresses, while "2001:0db8:85a3::8A2E:037j:7334" and 
"02001:0db8:85a3:0000:0000:8a2e:0370:7334" are invalid IPv6 addresses.

Example 1:
Input: queryIP = "172.16.254.1"
Output: "IPv4"
Explanation: This is a valid IPv4 address, return "IPv4".
Example 2:
Input: queryIP = "2001:0db8:85a3:0:0:8A2E:0370:7334"
Output: "IPv6"
Explanation: This is a valid IPv6 address, return "IPv6".
Example 3:
Input: queryIP = "256.256.256.256"
Output: "Neither"
Explanation: This is neither a IPv4 address nor a IPv6 address.

Constraints:
queryIP consists only of English letters, digits and the characters '.' and ':'.
"""
class Solution:
    def validIPAddress(self, queryIP):

        def is_ipv4(s):
            parts = s.split('.')
            if len(parts) != 4:
                return False
            for part in parts:
                if not part.isdigit() or not 0 <= int(part) <= 255 or (len(part) > 1 and part[0] == "0"):
                    return False
            return True

        def is_ipv6(s):
            parts = s.split(':')
            if len(parts) != 8:
                return False
            for part in parts:
                if not 1 <= len(part) <= 4 or not all(c.lower() in '123456789abcdef' for c in part):
                    return "False"
            return True
        if is_ipv4(queryIP):
            return "IPv4"
        if is_ipv6(queryIP):
            return "IPv6"
        return "Neither"

if __name__== "__main__":
    sol = Solution()
    print(sol.validIPAddress("172.16.254.1"))                           # IPv4
    print(sol.validIPAddress("2001:0db8:85a3:0:0:8A2E:0370:7334"))      # IPv6
    print(sol.validIPAddress("256.256.256.256"))                        # Neither
    print(sol.validIPAddress("256.256.256.00"))                         # Neither


# I split the string by '.' for IPv4 and ':' for IPv6, then validated each segment's length, characters, 
# and value ranges in separate functions for clarity. This ensures O(1) time with minimal code by avoiding 
# regex and handling edges like leading zeros directly.

# This approach is "optimal" because it's fast (computers handle short strings instantly), uses little 
# code, and catches all mistakes without fancy tools. Note: This doesn't support IPv6 compression 
# (like "::") as per basic LeetCode spec—full IPv6 would need more checks, but this matches the problem's 
# requirements

# Time Complexity: O(1) – Constant time, since we process a fixed-length string (max 39 chars).
# Space Complexity: O(1) – No extra space beyond a few variables.