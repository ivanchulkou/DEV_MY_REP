print("Дан список строк: ['abcbca', 'abccba', 'bro', 'abcde', 'bad_dab', 'cbdeaff', 'asdfg gfdsa']")
spis_ok = ['abcbca', 'abccba', 'bro', 'abcde', 'bad_dab', 'cbdeaff', 'asdfg gfdsa']


def check_palindrome(s):
    if s == s[::-1]:
        return True
    return False


palindrome_filter = list(filter(check_palindrome, spis_ok))
print(f'Палиндромами являются данные строки: {palindrome_filter}')
