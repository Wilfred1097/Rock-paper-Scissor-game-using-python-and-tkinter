from tkinter import*
from tkinter import messagebox
from PIL import ImageTk, Image
import random
import sys
import os

root = Tk()
root.title("Rock Paper Scissor")
root.geometry("500x550+650+200")
root.configure(bg="white")

com_score = []
your_score = []

your_pick = None
computer_pick = None

def compare():
	if sum(com_score) == 3:
		messagebox.showerror("Winner", "Computer Win")
		res = messagebox.askyesno("Try again", "Want to play again?")
		if res == False:
			root.destroy()
		else:
			python = sys.executable
			os.execl(python, python, * sys.argv)
	else:
		pass
	if sum(your_score) == 3:
		messagebox.showinfo("Winner", "You Win")
		res = messagebox.askyesno("Try again", "Want to play again?")
		if res == False:
			root.destroy()
		else:
			python = sys.executable
			os.execl(python, python, * sys.argv)
	else:
		pass

def rock():
	choices = ["Rock","Paper","Scissor"]
	random.shuffle(choices)

	openqr = Image.open("Rock.png")
	resize_image = openqr.resize((200,200))
	test = ImageTk.PhotoImage(resize_image)
	l1 = Label(root,image=test)
	l1.image = test
	l1.place(x=270,y=90) #70, 270

	if choices[0] == "Rock":
		openqr = Image.open("Rock.png")
		resize_image = openqr.resize((200,200))
		test = ImageTk.PhotoImage(resize_image)
		l1 = Label(root,image=test)
		l1.image = test
		l1.place(x=30,y=90)
		print("Tie")
	elif choices[0] == "Paper":
		openqr = Image.open("Paper.png")
		resize_image = openqr.resize((200,200))
		test = ImageTk.PhotoImage(resize_image)
		l1 = Label(root,image=test)
		l1.image = test
		l1.place(x=30,y=90)
		print("Lose")
		com_score.append(1)
	else:
		openqr = Image.open("Scissor.png")
		resize_image = openqr.resize((200,200))
		test = ImageTk.PhotoImage(resize_image)
		l1 = Label(root,image=test)
		l1.image = test
		l1.place(x=30,y=90)
		print("Win")
		your_score.append(1)
	Label(root, text=sum(com_score), font="helvetica 16", bg="white").place(x=145,y=8)
	Label(root, text=sum(your_score), font="helvetica 16", bg="white").place(x=430,y=8)
	compare()

def paper():
	choices = ["Rock","Paper","Scissor"]
	random.shuffle(choices)

	openqr = Image.open("Paper.png")
	resize_image = openqr.resize((200,200))
	test = ImageTk.PhotoImage(resize_image)
	l1 = Label(root,image=test)
	l1.image = test
	l1.place(x=270,y=90) #70, 270

	if choices[0] == "Rock":
		openqr = Image.open("Rock.png")
		resize_image = openqr.resize((200,200))
		test = ImageTk.PhotoImage(resize_image)
		l1 = Label(root,image=test)
		l1.image = test
		l1.place(x=30,y=90)
		print("Tie")
		your_score.append(1)
	elif choices[0] == "Paper":
		openqr = Image.open("Paper.png")
		resize_image = openqr.resize((200,200))
		test = ImageTk.PhotoImage(resize_image)
		l1 = Label(root,image=test)
		l1.image = test
		l1.place(x=30,y=90)
		print("Tie")
	else:
		openqr = Image.open("Scissor.png")
		resize_image = openqr.resize((200,200))
		test = ImageTk.PhotoImage(resize_image)
		l1 = Label(root,image=test)
		l1.image = test
		l1.place(x=30,y=90)
		print("Lose")
		com_score.append(1)
	Label(root, text=sum(com_score), font="helvetica 16", bg="white").place(x=145,y=8)
	Label(root, text=sum(your_score), font="helvetica 16", bg="white").place(x=430,y=8)
	compare()

def scissor():
	choices = ["Rock","Paper","Scissor"]
	random.shuffle(choices)

	openqr = Image.open("Scissor.png")
	resize_image = openqr.resize((200,200))
	test = ImageTk.PhotoImage(resize_image)
	l1 = Label(root,image=test)
	l1.image = test
	l1.place(x=270,y=90) #70, 270

	if choices[0] == "Rock":
		openqr = Image.open("Rock.png")
		resize_image = openqr.resize((200,200))
		test = ImageTk.PhotoImage(resize_image)
		l1 = Label(root,image=test)
		l1.image = test
		l1.place(x=30,y=90)
		print("Lose")
		com_score.append(1)
	elif choices[0] == "Paper":
		openqr = Image.open("Paper.png")
		resize_image = openqr.resize((200,200))
		test = ImageTk.PhotoImage(resize_image)
		l1 = Label(root,image=test)
		l1.image = test
		l1.place(x=30,y=90)
		print("Win")
		your_score.append(1)
	else:
		openqr = Image.open("Scissor.png")
		resize_image = openqr.resize((200,200))
		test = ImageTk.PhotoImage(resize_image)
		l1 = Label(root,image=test)
		l1.image = test
		l1.place(x=30,y=90)
		print("Tie")
	Label(root, text=sum(com_score), font="helvetica 16", bg="white").place(x=145,y=8)
	Label(root, text=sum(your_score), font="helvetica 16", bg="white").place(x=430,y=8)
	compare()

Label(root, text="Computer Score:", font="helvetica 13", bg="white").place(x=10,y=10)
Label(root, text="Your Score:", font="helvetica 13", bg="white").place(x=330,y=10)

Label(root, text="Computer picked:", font="helvetica 16", bg="white").place(x=16,y=50)
Label(root, text="You picked:", font="helvetica 16", bg="white").place(x=265,y=50)
Label(root, text="Pick Here:", font="helvetica 16", bg="white").place(x=60,y=320)

img1 = PhotoImage(file='rock.png')
img2 = PhotoImage(file='paper.png')
img3 = PhotoImage(file='scissor.png')

img_label = Label(image=img1)

Button(root, image=img1, relief='groove', width=100, height=130, command=rock).place(x=65,y=360)
Button(root, image=img2, relief='groove', width=100, height=130, command=paper).place(x=195,y=360)
Button(root, image=img3, relief='groove', width=100, height=130, command=scissor).place(x=325,y=360)

mainloop()