def same_case(a, b):
    if (a.isalpha() and b.isalpha()):
        if(a.isupper() and b.isupper()) or (a.islower() and b.islower()):
            return 1
        else:
            return 0
    else:
        return -1
print(same_case('a','g'))
print(same_case('A','C'))
print(same_case('b','G'))
print(same_case('B','g'))
print(same_case('0','?'))


# str_q = '1'
# print(str_q.isalpha())
