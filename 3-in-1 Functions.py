
#Question_3a

def is_palindrome(string):
    """Returns True if the input string is a palindrome, False otherwise."""
    string = string.lower().replace(" ", "")
    return string == string[::-1]


#Question_3b

def most_frequent_letter_or_digit(s):
    # Convert string to upper case
    s = s.upper()
    
    # Create a dictionary to count the frequency of letters/digits
    freq = {}
    for c in s:
        if c.isalnum():
            freq[c] = freq.get(c, 0) + 1
    
    # Find the most frequent letter/digit
    most_freq = None
    for c in freq:
        if most_freq is None or freq[c] > freq[most_freq]:
            most_freq = c
    
    return most_freq


#Question_3c
def count_chars(string):
    """
    Counts the number of letters, spaces, and digits in a string and returns a dictionary containing the counts.
    """
    count_dict = {'letters': 0, 'spaces': 0, 'digits': 0}
    for char in string:
        if char.isalpha():
            count_dict['letters'] += 1
        elif char.isspace():
            count_dict['spaces'] += 1
        elif char.isdigit():
            count_dict['digits'] += 1
    return count_dict

