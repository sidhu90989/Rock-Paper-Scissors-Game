import random

class RockPaperScissors:
    def __init__(self):
        """
        Initialize the game with choices and scoring
        """
        self.choices = ['rock', 'paper', 'scissors']
        self.user_score = 0
        self.computer_score = 0
        self.rounds_played = 0

    def get_user_choice(self):
        """
        Prompt user for their choice with input validation
        
        :return: User's valid choice
        """
        while True:
            print("\nChoose your move:")
            for i, choice in enumerate(self.choices, 1):
                print(f"{i}. {choice.capitalize()}")
            print("4. Quit")

            try:
                user_input = input("Enter your choice (1-4): ").strip()
                
                # Convert numeric input to choice
                if user_input in ['1', '2', '3', '4']:
                    if user_input == '4':
                        return 'quit'
                    return self.choices[int(user_input) - 1]
                
                # Allow text input
                user_input = user_input.lower()
                if user_input in self.choices:
                    return user_input
                
                print("Invalid choice. Please try again.")
            
            except ValueError:
                print("Invalid input. Please enter a number or valid choice.")

    def get_computer_choice(self):
        """
        Generate computer's random choice
        
        :return: Computer's choice
        """
        return random.choice(self.choices)

    def determine_winner(self, user_choice, computer_choice):
        """
        Determine the winner based on game rules
        
        :param user_choice: Player's choice
        :param computer_choice: Computer's choice
        :return: Winner (user/computer/tie)
        """
        if user_choice == computer_choice:
            return 'tie'
        
        winning_moves = {
            'rock': 'scissors',
            'paper': 'rock',
            'scissors': 'paper'
        }
        
        if winning_moves[user_choice] == computer_choice:
            return 'user'
        return 'computer'

    def display_result(self, user_choice, computer_choice, winner):
        """
        Display game round results
        
        :param user_choice: Player's choice
        :param computer_choice: Computer's choice
        :param winner: Round winner
        """
        print("\n--- Round Result ---")
        print(f"Your choice: {user_choice.capitalize()}")
        print(f"Computer's choice: {computer_choice.capitalize()}")
        
        if winner == 'tie':
            print("It's a tie!")
        elif winner == 'user':
            print("You win this round! 🎉")
        else:
            print("Computer wins this round! 🤖")
        
        # Update and display scores
        if winner == 'user':
            self.user_score += 1
        elif winner == 'computer':
            self.computer_score += 1
        
        self.rounds_played += 1
        
        print(f"\nScore:")
        print(f"You: {self.user_score}  |  Computer: {self.computer_score}")
        print(f"Rounds Played: {self.rounds_played}")

    def play_game(self):
        """
        Main game loop
        """
        print("🎮 Rock-Paper-Scissors Game 🎮")
        print("Welcome! Let's play Rock-Paper-Scissors.")
        
        while True:
            # Get user choice
            user_choice = self.get_user_choice()
            
            # Check for quit
            if user_choice == 'quit':
                self.display_final_results()
                break
            
            # Get computer choice
            computer_choice = self.get_computer_choice()
            
            # Determine and display winner
            winner = self.determine_winner(user_choice, computer_choice)
            self.display_result(user_choice, computer_choice, winner)
            
            # Ask to continue
            play_again = input("\nDo you want to play another round? (yes/no): ").lower()
            if play_again != 'yes':
                self.display_final_results()
                break

    def display_final_results(self):
        """
        Display final game statistics
        """
        print("\n🏆 Final Game Statistics 🏆")
        print(f"Total Rounds Played: {self.rounds_played}")
        print(f"Your Score: {self.user_score}")
        print(f"Computer Score: {self.computer_score}")
        
        # Determine overall winner
        if self.user_score > self.computer_score:
            print("\nCongratulations! You won the game! 🎊")
        elif self.user_score < self.computer_score:
            print("\nComputer won the game. Better luck next time! 🤖")
        else:
            print("\nIt's a tie game! Well played! 🤝")

def main():
    """
    Initialize and start the game
    """
    game = RockPaperScissors()
    game.play_game()

if __name__ == "__main__":
    main()