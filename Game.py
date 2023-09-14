from tkinter import*
from PIL import Image,ImageTk
from random import randint

#main window
root=Tk()
root.title("Rock Scissor Paper")
root.configure(background="#9b59b6")

#pictures
rock_img= ImageTk.PhotoImage(Image.open("Rock_User.png"))
paper_img= ImageTk.PhotoImage(Image.open("Paper_User.png"))
scissor_img= ImageTk.PhotoImage(Image.open("Scissor_User.png"))
rock_img_com= ImageTk.PhotoImage(Image.open("Rock.png"))
paper_img_com= ImageTk.PhotoImage(Image.open("Paper.png"))
scissor_img_com= ImageTk.PhotoImage(Image.open("Scissor.png"))

#insert picture
user_label= Label(root, image=rock_img,bg="#9b59b6")
com_label= Label(root,image=rock_img_com)
com_label.grid(row=1,column=0)
user_label.grid(row=1,column=4)

#score
playerScore= Label(root,text=0,font=100,bg="#9b59b6",fg="white")
compScore=Label(root,text=0,font=100,bg="#9b59b6",fg="white")
compScore.grid(row=1,column=1)
playerScore.grid(row=1,column=3)

#indicator
user_indicator=Label(root,font=50,text="USER",bg="#9b59b6",fg="white")
comp_indicator=Label(root,font=50,text="COMPUTER",bg="#9b59b6",fg="white")
user_indicator.grid(row=0,column=3)
comp_indicator.grid(row=0,column=1)

#message
msg=Label(root,font=50,bg="#9b59b6",fg="white")
msg.grid(row=3,column=2)

#update message
def updateMessage(x):
    msg['text']=x
#update user score
def updateUserScore():
    score=int(playerScore["text"])
    score +=1
    playerScore["text"]=str(score)

#update comp score

def updateCompScore():
    score=int(compScore["text"])
    score +=1
    compScore["text"]=str(score)

#check winner
def checkWin(player,computer):
    if player==computer:
        updateMessage("It is Tie!")
    elif player=="rock":
        if computer =="paper":
            updateMessage("You loose")
            updateCompScore()
        else:
            updateMessage("You Win")
            updateUserScore()
    elif player =="paper":
        if computer=="scissor":
            updateMessage("You Loose")
            updateCompScore()
        else:
            updateMessage("You Win")
            updateUserScore()
    elif player=="scissor":
        if computer=="rock":
            updateMessage("You Loose")
            updateCompScore()
        else:
            updateMessage("You Win")
            updateUserScore()
    else:
        pass


#udate choice

choices=["rock","paper","scissor"]
def updateChoice(x):

#for computer
    compChoice= choices[randint(0,2)]
    if compChoice=="rock":
        com_label.configure(image=rock_img_com)
    elif compChoice=="paper":
        com_label.configure(image=paper_img_com)
    else:
        com_label.configure(image=scissor_img_com)



#for user
    if x=="rock":
        user_label.configure(image=rock_img)
    elif x=="paper":
        user_label.configure(image=paper_img)
    else:
        user_label.configure(image=scissor_img)

    checkWin(x,compChoice)
    

#button
rock=Button(root,width=20,height=2,text="ROCK",bg="#FF3E4D",fg="white",command=lambda:updateChoice("rock"))
rock.grid(row=2,column=1)
paper=Button(root,width=20,height=2,text="PAPER",bg="#FAD02E",fg="white",command=lambda:updateChoice("paper"))
paper.grid(row=2,column=2)
scissor=Button(root,width=20,height=2,text="SCISSOR",bg="#0ABDE3",fg="white",command=lambda:updateChoice("scissor"))
scissor.grid(row=2,column=3)


root.mainloop()
