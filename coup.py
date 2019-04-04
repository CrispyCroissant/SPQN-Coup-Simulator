"""
The score range is (1,51)
100% probability of winning == score of 50.
Max possible score == 43.
Max possible percentage of winning == 43/50 == 86%
"""
import random, time

position_scores = {
    "Oberbefehl": 10,
    "Geheimpolizei": 9,
    "Reichsprotektor": 7,
    "Finansminister": 5,
    "Diplomacyminister": 4,
    "Sozialminister": 3,
    "Mfi": 3,
    "Rustning": 2
}

coup_score = 0
positions_supporting_coup = []

# print all possible positions
print("Here are the senates positions:\n")
for key in position_scores.keys():
    print(key)


def add_to_score():
    global coup_score

    coup_score += position_scores[user_input]
    probab = coup_score / 50
    print(f"{user_input} was added.\n")


# position loop
while True:
    user_input = input(
        "\nWhich positions are supporting the coup? (q to quit) ")
    user_input = user_input[0].upper() + user_input[1:]

    if user_input != "Q":
        if user_input in position_scores:
            positions_supporting_coup.append(user_input)
            add_to_score()
        else:
            raise ValueError("No such position")
    else:
        break

# add increased probability per member supporting the coup
for x in positions_supporting_coup:
    coup_score *= 1.13

print(f"Probability of coup succeeding: {(coup_score / 50) * 100}%")
print("Coup d'etat is underway...")
time.sleep(10)
print("All radio- and TV-channels have been changed to the emergency broadcast!\n")
time.sleep(5)

# simulator
if random.randint(1, 51) < coup_score:
    print("The Reichskonsuls have been captured, along with the supporters of the government. The coup has succeeded! ")
else:
    print("The coup members have been captured, along with their supporters, and are being escorted to prison. The coup has failed!")
