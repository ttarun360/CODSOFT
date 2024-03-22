from tkinter import *
from PIL import Image, ImageTk
from random import randint

# Main window
root = Tk()
root.title("Rock Scissor Paper")
root.configure(background="#e6f7ff")

# Pictures
rock_img = ImageTk.PhotoImage(Image.open("rock-user.png"))
paper_img = ImageTk.PhotoImage(Image.open("paper-user.png"))
scissor_img = ImageTk.PhotoImage(Image.open("scissors-user.png"))
rock_img_comp = ImageTk.PhotoImage(Image.open("rock.png"))
paper_img_comp = ImageTk.PhotoImage(Image.open("paper.png"))
scissor_img_comp = ImageTk.PhotoImage(Image.open("scissors.png"))

# Labels for user and computer choices
user_label = Label(root, image=scissor_img, bg="#e6f7ff")
comp_label = Label(root, image=scissor_img_comp, bg="#e6f7ff")
user_label.grid(row=1, column=4, pady=10)
comp_label.grid(row=1, column=0, pady=10)

# Scores
playerScore = Label(root, text=0, font=("Helvetica", 30), bg="#e6f7ff", fg="red")
computerScore = Label(root, text=0, font=("Helvetica", 30), bg="#e6f7ff", fg="red")
playerScore.grid(row=1, column=3)
computerScore.grid(row=1, column=1)

# Buttons
rock = Button(root, width=15, height=2, text="ROCK", bg="#ff6666", fg="white", command=lambda: updateChoice("rock"))
paper = Button(root, width=15, height=2, text="PAPER", bg="#66cc99", fg="white", command=lambda: updateChoice("paper"))
scissor = Button(root, width=15, height=2, text="SCISSOR", bg="#6666ff", fg="white", command=lambda: updateChoice("scissor"))
rock.grid(row=2, column=1, padx=10)
paper.grid(row=2, column=2, padx=10)
scissor.grid(row=2, column=3, padx=10)

# Indicators
user_indicator = Label(root, font=("Helvetica", 20), text="USER", bg="#e6f7ff", fg="red")
computer_indicator = Label(root, font=("Helvetica", 20), text="COMPUTER", bg="#e6f7ff", fg="red")
user_indicator.grid(row=0, column=3, pady=10)
computer_indicator.grid(row=0, column=1, pady=10)

# Messages
msg = Label(root, font=("Helvetica", 20), bg="#ff6666", fg="white")
msg.grid(row=3, column=2, pady=10)

# Update message
def updateMessage(x):
    msg['text'] = x

# Update user score
def updateUserScore():
    score = int(playerScore["text"])
    score += 1
    playerScore["text"] = str(score)

# Update computer score
def updateCompScore():
    score = int(computerScore["text"])
    score += 1
    computerScore["text"] = str(score)

# Check winner
def checkWin(player, computer):
    if player == computer:
        updateMessage("It's a tie!")
    elif player == "rock":
        if computer == "paper":
            updateMessage("You lose")
            updateCompScore()
        else:
            updateMessage("You win")
            updateUserScore()
    elif player == "paper":
        if computer == "scissor":
            updateMessage("You lose")
            updateCompScore()
        else:
            updateMessage("You win")
            updateUserScore()
    elif player == "scissor":
        if computer == "rock":
            updateMessage("You lose")
            updateCompScore()
        else:
            updateMessage("You win")
            updateUserScore()
    else:
        pass

# Updates choices
choices = ["rock", "paper", "scissor"]
def updateChoice(x):
    # For computer
    compChoice = choices[randint(0, 2)]
    if compChoice == "rock":
        comp_label.configure(image=rock_img_comp)
    elif compChoice == "paper":
        comp_label.configure(image=paper_img_comp)
    else:
        comp_label.configure(image=scissor_img_comp)

    # For user
    if x == "rock":
        user_label.configure(image=rock_img)
    elif x == "paper":
        user_label.configure(image=paper_img)
    else:
        user_label.configure(image=scissor_img)

    checkWin(x, compChoice)

root.mainloop()
