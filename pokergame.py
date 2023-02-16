from tkinter import *
import tkinter as tk

import random

def key_press_start_frame(event): #it checks what key is pressed
    key = event.char
    print(key, 'is pressed')

    if key in ('A', 'a'):
        # enter vs AI window
        pass

    if key in ('U', 'u'):
        # enter vs user window
        pass

    if key in ('R', 'r'):
        # enter rules window
        pass

    if key in ('Q', 'q'):
        # exit window
        pass

    



def GUI_start_frame():#game_start_frame
    root = tk.Tk()
    root.title("Poker Game")
    
    main_frame= tk.Frame(root, width=1000, height=1000, background="gray") #the screen
    main_frame.pack()

    title_label = tk.Label(root, text="Welcome to our Poker Game", font=("Times New Roman", 25), background="blue").place(x=335, y=200)


    against_computer_label = tk.Label(root, text="Press A to play against the computer", font=("Times New Roman", 15), background="blue").place(x=335, y=400)

    against_human_label = tk.Label(root, text = "Press U to play against another human", font=("Times New Roman", 15), background="blue").place(x=335, y=480)

    rules_label = tk.Label(root, text = "Press R to read the rules", font=("Times New Roman", 15), background="blue").place(x=335, y=560)

    quit_label = tk.Label(root, text = "Press Q to exit the game", font=("Times New Roman", 15), background="blue").place(x=335, y=640)

    root.bind('<Key>', key_press_start_frame)

    
    
    

    root.mainloop()



def main(): #main
    GUI_start_frame()


if __name__ == "__main__":
    main()
