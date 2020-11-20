'''
 You are given a string and you have to find its first word.

This is a simplified version of the First Word mission, which can be solved later.

    The input string consists of only English letters and spaces.
    There aren’t any spaces at the beginning and the end of the string.

Input: A string.

Output: A string.

Example:
first_word("Hello world") == "Hello"

'''

def first_word(text: str) -> str:
    """
        returns the first word in a given text.
    """
    if ' ' in text:
        x = text.find(' ')
        return text[0:x]
    else:
        return text


if __name__ == '__main__':
    print("Example:")
    print(first_word("Hello"))