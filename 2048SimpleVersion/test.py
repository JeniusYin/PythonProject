from random import randrange, choice

# 用户行为
actions = ['Up', 'Left', 'Down', 'Right', 'Restart', 'Exit']
# 用户有效输入 ord()将字符转换为ASCII码
# [87, 65, 83, 68, 82, 81, 119, 97, 115, 100, 114, 113]
letter_codes = [ord(ch) for ch in 'WASDRQwasdrq']
# 关联输入与行为
actions_dict = dict(zip(letter_codes, actions * 2))

# print(actions * 2)

# for t in zip(letter_codes, actions * 2):
#     print(t)

# print(actions_dict)

# print(actions_dict[65])
# print([1, 2, 3, 4][::-1])

field = [[0 for i in range(4)]
         for j in range(4)]
print(field)
print([list(row) for row in zip(*field)])

print(choice([(i, j) for i in range(4)
              for j in range(4) if field[i][j] == 0]))
