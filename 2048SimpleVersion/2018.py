import curses
from random import randrange, choice
from collections import defaultdict

# 用户行为
actions = ['Up', 'Left', 'Down', 'Right', 'Restart', 'Exit']
# 用户有效输入 ord()将字符转换为ASCII码
# [87, 65, 83, 68, 82, 81, 119, 97, 115, 100, 114, 113]
letter_codes = [ord(ch) for ch in 'WASDRQwasdrq']
# 关联输入与行为 zip函数接受任意多个（包括0个和1个）list作为参数，返回一个tuple列表
actions_dict = dict(zip(letter_codes, actions * 2))
#  {65: 'Left', 83: 'Down', 68: 'Right', 97: 'Left', 119: 'Up', 114: 'Restart', 81: 'Exit', 82: 'Restart', 115: 'Down', 113: 'Exit', 87: 'Up', 100: 'Right'}


def get_user_action(keyboard):
    char = 'N'
    while char not in actions_dict:
        char = keyboard.getch()
    return actions_dict[char]

# 矩阵转置与矩阵逆转


def transpose(field):
    return [list(row) for row in zip(*field)]


def invert(field):
    return [row[::-1] for row in field]


class Gamefield(object):

    def __init__(self, height=4, width=4, win=2048):
        self.height = height
        self.width = width
        self.win_value = win
        self.score = 0
        self.highscore = 0
        self.reset()

# 在棋盘上随机生成一个2或4
    def spawn(self):
        new_element = 4 if randrange(100) > 89 else 2
        # choice() 方法返回一个列表，元组或字符串的随机项。
        # 返回一个位置坐标 (3,1)，将此位置的值设为2或4
        (i, j) = choice([(i, j) for i in range(self.width)
                         for j in range(self.height) if self.field[i][j] == 0])
        self.field[i][j] = new_element

    def reset(self):
        if self.score > self.highscore:
            self.highscore = self.score
        self.score = 0
        # [[0, 0, 0, 0], [0, 0, 0, 0], [0, 0, 0, 0], [0, 0, 0, 0]]
        self.field = [[0 for i in range(self.width)]
                      for j in range(self.height)]
        self.spawn()
        self.spawn()

    def move(self, direction):
        def move_row_left(row):
            def tighten(row):
                new_row = [i for i in row if i != 0]
                new_row += [0 for i in range(len(row) - len(new_row))]
                return new_row

            def merge(row):
                pair = False
                new_row = []
                for i in range(len(row)):
                    if pair:
                        new_row.append(2 * row[i])
                        self.score += 2 * row[i]
                        pair = False
                    else:
                        if i + 1 < len(row) and row[i] == row[i + 1]:
                            pair = True
                            new_row.append(0)
                        else:
                            new_row.append(row[i])
                assert len(new_row) == len(row)
                return new_row
            return tighten(merge(tighten(row)))

        moves = {}
        moves['Left'] = lambda field: [move_row_left(row) for row in field]
        moves['Right'] = lambda field: invert(moves['Left'](invert(field)))
        moves['Up'] = lambda field: transpose(moves['Left'](transpose(field)))
        moves['Down'] = lambda field: transpose(
            moves['Right'](transpose(field)))

        if direction in moves:
            if self.move_is_possible(direction):
                self.field = moves[direction](self.field)
                self.spawn()
                return True
            else:
                return False

    def is_win(self):
        return any(any(i >= self.win_value for i in row) for row in self.field)

    def is_gameover(self):
        return not any(self.move_is_possible(move) for move in actions)

    def draw(self, screen):
        help_string1 = '(W)Up (S)Down (A)Left (D)Right'
        help_string2 = '             (R)Restart (Q)Exit'
        gameover_string = '					GAME OVER'
        win_string = '					YOU WIN!'

        def cast(string):
            screen.addstr(string + '\n')

            # 绘制水平分割线

        def draw_hor_separator():
            line = '+' + ('+------' * self.width + '+')[1:]
            separator = defaultdict(lambda: line)
            if not hasattr(draw_hor_separator, "counter"):
                draw_hor_separator.counter = 0
            cast(separator[draw_hor_separator.counter])
            draw_hor_separator.counter += 1

            # 只将大于0的数字画出
        def draw_row(row):
            cast(''.join('|{: ^5} '.format(num) if num >
                         0 else '|      ' for num in row) + '|')

        screen.clear()

        cast('SCORE: ' + str(self.score))
        if self.highscore != 0:
            cast('HIGHSCORE: ' + str(self.highscore))

        for row in self.field:
            draw_hor_separator()
            draw_row(row)

        draw_hor_separator()

        if self.is_win():
            cast(win_string)
        else:
            if self.is_gameover():
                cast(gameover_string)
            else:
                cast(help_string1)
        cast(help_string2)

    def move_is_possible(self, direction):
        def row_is_left_movable(row):
            def change(i):
                if row[i] == 0 and row[i + 1] != 0:  # 可以移动
                    return True
                if row[i] != 0 and row[i + 1] == row[i]:  # 可以合并
                    return True
                return False
            return any(change(i) for i in range(len(row) - 1))

        check = {}
        check['Left'] = lambda field: any(
            row_is_left_movable(row) for row in field)

        check['Right'] = lambda field: check['Left'](invert(field))

        check['Up'] = lambda field: check['Left'](transpose(field))

        check['Down'] = lambda field: check['Right'](transpose(field))

        if direction in check:
            return check[direction](self.field)
        else:
            return False


def main(stdscr):

    def init():
        # 重置游戏
        game_field.reset()
        return 'Game'

    def not_game(state):
        # 1.画出GameOver or Win 2.读取输入得到action,判断重启游戏还是结束游戏
        game_field.draw(stdscr)
        action = get_user_action(stdscr)
        response = defaultdict(lambda: state)  # 默认是当前状态，没有行为就会一直在当前界面循环
        response['Restart'], response['Exit'] = 'Init', 'Exit'
        return response[action]

    def game():
        # 画出当前棋盘状态
        game_field.draw(stdscr)
        # 读取用户输入得到action
        action = get_user_action(stdscr)

        if action == 'Restart':
            return 'Init'
        if action == 'Exit':
            return 'Exit'
        # 向前移动了一步
        if game_field.move(action):
            if game_field.is_win():
                return 'Win'
            if game_field.is_gameover():
                return 'GameOver'
        return 'Game'

    state_actions = {
        'Init': init,
        'Win': lambda: not_game('Win'),
        'GameOver': lambda: not_game('GameOver'),
        'Game': game
    }

    curses.use_default_colors()
    game_field = Gamefield(win=512)

    state = 'Init'

    # 状态机开始循环
    while state != 'Exit':
        state = state_actions[state]()

curses.wrapper(main)
