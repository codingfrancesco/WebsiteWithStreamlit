
def fun_winner(value):
    import random
    computer = random.randint(1,3)
    
    if computer == 1:
        computer = 'rock'
    elif computer == 2:
        computer = 'paper'
    elif computer == 3:
        computer = 'scissors'

    # Add computer's choice to the result
    result_text = f"Computer chose: {computer}\n\n"

    if value == computer:
        result_text += "🤝 It's a tie! 🤝"
    elif value == 'rock' and computer == 'scissors':
        result_text += "🎉 You win! Rock smashes scissors! 🎉"
    elif value == 'rock' and computer == 'paper':
        result_text += "😔 You lose! Paper covers rock! 😔"
    elif value == 'paper' and computer == 'rock':
        result_text += "🎉 You win! Paper covers rock! 🎉"
    elif value == 'paper' and computer == 'scissors':
        result_text += "😔 You lose! Scissors cut paper! 😔"
    elif value == 'scissors' and computer == 'rock':
        result_text += "😔 You lose! Rock smashes scissors! 😔"
    elif value == 'scissors' and computer == 'paper':
        result_text += "🎉 You win! Scissors cut paper! 🎉"
    
    return (result_text)  # Display the result in the console or GUI label
