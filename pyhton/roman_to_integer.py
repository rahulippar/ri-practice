"""
Roman numerals use a system of seven unique symbols to represent specific values:

Symbol	Value
I	1
V	5
X	10
L	50
C	100
D	500
M	1000
For example:

The number 2 is written as II, which is simply two I symbols added together.
Similarly, 12 is represented as XII (10 + 1 + 1), and 27 as XXVII (10 + 10 + 5 + 1 + 1).
Roman numerals are generally arranged from largest to smallest values, ordered from left to right. However, certain numbers use a subtraction principle:

Four is represented as IV (5 - 1) instead of IIII.
Similarly, nine is written as IX (10 - 1).
There are specific cases where this subtraction rule is applied:

I appears before V (5) or X (10) to form 4 and 9.
X precedes L (50) or C (100) to create 40 and 90.
C is placed before D (500) or M (1000) to represent 400 and 900.
Your task:
Given a Roman numeral string, convert it into its corresponding integer value.

Examples:

Example 1:
Input: s = "III"
Output: 3
Explanation: The value III directly translates to 3.

Example 2:
Input: s = "LVIII"
Output: 58
Explanation: Breakdown: L = 50, V = 5, and III = 3.

Example 3:
Input: s = "MCMXCIV"
Output: 1994
Explanation: Breakdown: M = 1000, CM = 900, XC = 90, and IV = 4.

"""

def romanToInt(s: str) -> int:

  roman_to_integer = {
      "I": 1,
      "V": 5,
      "X": 10,
      "L": 50,
      "C": 100,
      "D": 500,
      "M": 1000,
  }

  roman_conversions = {
      "IV": "IIII",
      "IX": "VIIII",
      "XL": "XXXX",
      "XC": "LXXXX",
      "CD": "CCCC",
      "CM": "DCCCC",
  }

  for key, value in roman_conversions.items():
      s = s.replace(key, value)

  sum = 0

  for roman_charactor in s:
      sum = sum + roman_to_integer.get(roman_charactor, 0)

  return sum
"""
