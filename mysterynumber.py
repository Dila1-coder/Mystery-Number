import random

def generate_random_number():
    random_number = random.randint(1, 5)
    return random_number

def get_input():
    try:
        random_guess = int(input("Guess a number between 1 and 5: "))
        return random_guess
    except ValueError:
        print("Invalid input. Please enter a number.")

def evaluate_answer(player_name):
    score = 0  # Initialize the score variable
    
    for _ in range(3):
        guess = get_input()
        
        if guess is None:
            print("Guess not submitted.")
            continue
        
        correct_number = generate_random_number()
        
        if guess == correct_number:
            print("Correct!")
            score += 1  # Increment the score if the answer is correct
        else:
            print("Incorrect!")
            if guess < correct_number:
                print("Hint: The number is higher than your guess.")
            else:
                print("Hint: The number is lower than your guess.")
    
    print("Player:", player_name)
    print("Your final score is:", score)
    print()

# Enable multiplayer mode
num_players = int(input("Enter the number of players: "))

for player in range(1, num_players + 1):
    player_name = input("Enter the name of Player {}:".format(player))
    print("Let's begin, Player", player_name)
    evaluate_answer(player_name)

# Determine the winner
winners = []
max_score = 0

for player in range(1, num_players + 1):
    player_name = input("Enter the name of Player {}:".format(player))
    player_score = int(input("Enter the score for Player {}:".format(player)))
    
    if player_score > max_score:
        max_score = player_score
        winners = [player_name]
    elif player_score == max_score:
        winners.append(player_name)

print("Game over")
print("The winner(s) with the highest score of", max_score, "is/are:", ", ".join(winners))
