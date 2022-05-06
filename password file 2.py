def distinct_password(input1, input2):
    distinct = input1
    for i in range(input1):
        for e in range(i + 1, input1):
            length = len(input2[i])
            password = list(input2[i])
            for i in range(length - 2):
                password[i], password[i + 2] = password[i + 2], password[i]
            if password == list(input2[i]):
                distinct -= 1
                break
    return distinct
print(distinct_password(2, ['abcd', 'cdab']))
print("password done")
