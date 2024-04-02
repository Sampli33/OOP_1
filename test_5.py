from solution_5 import Game

first_game = Game({'command1': 'Волки', 'command2': 'Медведи'})
first_game.ball_thrown(1, 2)
first_game.ball_thrown(1, 3)
first_game.ball_thrown(2, 3)
first_game.ball_thrown(2, 2)
first_game.ball_thrown(1, 2)
print(first_game.get_score())
print(first_game.get_winner())
print(first_game)
b = [first_game.get_score()]
print(b)
