from itertools import combinations
def distinct_password(input1, input2):
    combination = list(combinations(input2, 2))
    distinct = input1
    for j in combination:
        length = len(j[0])
        password = list(j[0])
        for i in range(length - 2):
            password[i], password[i + 2] = password[i + 2], password[i]
            if password == list(j[1]):
                distinct -= 1
                break
    return distinct
print(distinct_password(2, ['abcd', 'cdab']))
print("distinct passwords are")
