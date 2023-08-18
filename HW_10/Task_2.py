'''
Угадайка
'''

import random


class Puzzle:
    def __init__(self, puzzle_text, answers):
        self.puzzle_text = puzzle_text
        self.answers = answers

    def check_answer(self, user_answer):
        return user_answer.lower() in self.answers


class PuzzleGame:
    def __init__(self, puzzles: list[Puzzle], trials_num: int):
        self.puzzles = puzzles
        self.trials_num = trials_num
        self.stats = {puzzle.puzzle_text: 0 for puzzle in puzzles}

    def play(self):
        shuffled_puzzles = self.puzzles.copy()
        random.shuffle(shuffled_puzzles)

        for puzzle in shuffled_puzzles:
            print(puzzle.puzzle_text)
            for trial in range(self.trials_num):
                current_try = input(f'Осталось попыток: {self.trials_num - trial}. Ваш ответ: ')
                if puzzle.check_answer(current_try):
                    print('Верно!')
                    self.stats[puzzle.puzzle_text] = trial + 1
                    break
                else:
                    print('Неверно!')
            else:
                print('Ваши ответы не верны. Попытки закончились.')

    def show_stat(self):
        print()
        print('Статистика отгадывания:')
        for puzzle_text, trial_count in self.stats.items():
            if trial_count > 0:
                print(f'Загадка: {puzzle_text} Угадана с {trial_count} попытки.')
            else:
                print(f'Загадка: {puzzle_text} Не угадана.')


if __name__ == '__main__':
    PUZZLES = [
        Puzzle('В поле лестница лежит, дом по лестнице бежит?', ['поезд']),
        Puzzle('Чудо-ящик. В нём окно. В том окошечке - кино?', ['телевизор']),
        Puzzle('Что за братцы из стекла. Для чая, сока и молока?', ['стаканы', 'кружки'])
    ]

    puzzle_game = PuzzleGame(PUZZLES, 2)
    puzzle_game.play()
    puzzle_game.show_stat()
