

questions = [
    {"question": "What is the capital of France?", "options": ["A) Berlin", "B) Madrid", "C) Paris", "D) Rome"], "correct": "C"},
    {"question": "What is 5 + 7?", "options": ["A) 10", "B) 12", "C) 11", "D) 13"], "correct": "B"},
    {"question": "Which planet is known as the Red Planet?", "options": ["A) Earth", "B) Mars", "C) Jupiter", "D) Venus"], "correct": "B"},
]

scores = {}


def add_player(name):
    if name not in scores:
        scores[name] = 0
    print(f"{name} has joined the game!")

def ask_questions(player_name):
    for i, q in enumerate(questions):
        print(f"\nQuestion {i+1}: {q['question']}")
        for option in q['options']:
            print(option)
        answer = input(f"{player_name}, choose your answer (A/B/C/D): ").upper()

        if answer == q['correct']:
            print("Correct!")
            scores[player_name] += 1
        else:
            print("Incorrect!")

def display_scores():
    print("\nFinal Scores:")
    for player, score in scores.items():
        print(f"{player}: {score}")

def quiz_game():
    print("Welcome to the Quiz Game!")
    
    num_players = int(input("Enter the number of players: "))
    
    for _ in range(num_players):
        player_name = input("Enter player name: ")
        add_player(player_name)
    
    for player in scores.keys():
        print(f"\n{player}'s turn:")
        ask_questions(player)
    
    display_scores()

quiz_game()
