from random import randint

def generate_random_game():
    prize_index = randint(0, 2)
    if prize_index == 0:
        return (1, 0, 0)
    if prize_index == 1:
        return (0, 1, 0)
    if prize_index == 2:
        return (0, 0, 1)

def always_keep_first_random_choice(n):
    victories = 0
    for game in range(n):
        three_doors = generate_random_game()
        first_random_choice = randint(0, 2)
        # Host: **Opens random door with bad prize**
        # Player: **Keeps same door**
        victories += three_doors[first_random_choice]
    return victories / n

def always_switch_door_after_first_random_choice(n):
    victories = 0
    for game in range(n):
        three_doors = generate_random_game()
        first_random_choice = randint(0, 2)
        # Host: **Opens random door with bad prize**
        opened_door_with_bad_prize = [ x for x in range(3) if three_doors[x] == 0 and x != first_random_choice ][0]
        # Player: **Switches door**
        second_choice_after_switch = [ x for x in range(3) if x != first_random_choice and x != opened_door_with_bad_prize ][0]
        victories += three_doors[second_choice_after_switch]
    return victories / n

def main():
    number_of_games = 10000
    result_always_keep_first_choice = always_keep_first_random_choice(number_of_games)
    result_always_switch_door_after_first_choice = always_switch_door_after_first_random_choice(number_of_games)
    print("Wins when always keeping first random choice: " + str(result_always_keep_first_choice * 100) + "%")
    print("Wins when always switching door after first random choice: " + str(result_always_switch_door_after_first_choice * 100) + "%")  

if __name__ == "__main__":
    main()