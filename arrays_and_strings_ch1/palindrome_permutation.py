def check_palindrome(palindrome):
    char_count = dict()
    odd = 0
    for i in palindrome:
        if i == ' ':
            continue
        if i in char_count:
            char_count[i] += 1
            if char_count[i] %2 == 1:
                odd += 1
            else:
                odd -= 1
        else:
            char_count[i] = 1

    return odd <= 1

if __name__ == '__main__':
    palindrome = input()
    print(check_palindrome(palindrome))