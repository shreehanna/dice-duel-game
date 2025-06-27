import random

class Dice:
    """Simulates a six-sided dice."""
    def roll(self):
        return random.randint(1, 6)

class Player:
    """Represents a player with a name and a score."""
    def __init__(self, name):
        self.name = name
        self.score = 0

    def update_score(self, points):
        """Updates the player's score."""
        self.score += points

class Game:
    """Manages the gameplay between two players."""
    def __init__(self, player1_name, player2_name, rounds=3):
        self.dice = Dice()
        self.player1 = Player(player1_name)
        self.player2 = Player(player2_name)
        self.rounds = rounds

    def play(self):
        for round_num in range(1, self.rounds + 1):
            print(f"\nRound {round_num}:")
            p1_roll = self.dice.roll()
            p2_roll = self.dice.roll()
            print(f"{self.player1.name} rolled {p1_roll}")
            print(f"{self.player2.name} rolled {p2_roll}")

            if p1_roll > p2_roll:  # Determines which player wins the round
                self.player1.update_score(1)
                print(f"{self.player1.name} wins this round!")
            elif p2_roll > p1_roll:
                self.player2.update_score(1)
                print(f"{self.player2.name} wins this round!")
            else:
                print("It's a tie!")

        self.display_winner()

    def display_winner(self):
        """Displays the final winner after all rounds."""
        print(f"\nFinal Scores:")
        print(f"{self.player1.name}: {self.player1.score}")
        print(f"{self.player2.name}: {self.player2.score}")
        if self.player1.score > self.player2.score:
            print(f"{self.player1.name} wins the game! 🏆")
        elif self.player2.score > self.player1.score:
            print(f"{self.player2.name} wins the game! 🏆")
        else:
            print("The game is a tie! 🤝")

if __name__ == "__main__":
    game = Game("Shree", "Bot")
    game.play()
