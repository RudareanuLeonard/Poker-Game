from tkinter import *
import tkinter as tk
from PIL import ImageTk, Image
import PIL as pil

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


    against_computer_button = tk.Button(root, text="Press A to play against the computer", font=("Times New Roman", 15), background="blue").place(x=335, y=400)

    against_human_button = tk.Button(root, text = "Press U to play against another human", font=("Times New Roman", 15), background="blue").place(x=335, y=480)

    rules_button = tk.Button(root, text = "Press R to read the rules", font=("Times New Roman", 15), background="blue").place(x=335, y=560)

    quit_button = tk.Button(root, text = "Press Q to exit the game", font=("Times New Roman", 15), background="blue").place(x=335, y=640)

    root.bind('<Key>', key_press_start_frame)
    

    root.mainloop()




def human_vs_computer(): # human vs computer
    
    #CLASSES HERE

    class Card: #class for attributes of a Card
        def __init__(self, card_value, card_suit):
            self.card_value = card_value
            self.card_suit = card_suit
    

    class Deck(list): #class for attributes of entire deck of cards////// INHERITANCE from list class, so we can use append, pop and so on...
        def __init__(self):
            number_of_values = 13 #13 because A is either 1 or 11
            number_of_suits = 4 #Spades, Hearts, Diamonds, Clubs

            #now we generate all the posibilities and assign it to a Card obj which is placed into a list
            for suit in number_of_suits:
                for value in number_of_values:
                    self.append(Card(value, suit))

        
        def shuflle_deck(self): #shuffle the deck
            random.shuffle(self)
        
        def pop_a_card(self, card_to_pop): #pop a card after it been dealt
            get_index = self.index(card_to_pop)
            self.pop(get_index)

    
    
    #GUI STARTS HERE
    root = tk.Tk()
    root.title("User VS Computer")

    main_frame= tk.Frame(root, width=1000, height=1000, background="gray") #the screen
    main_frame.pack()

    computer_frame = tk.Frame(root)
    computer_frame.pack()

    user_frame = tk.Frame(root)
    user_frame.pack()

    cards_dealt_frame = tk.Frame(root)
    cards_dealt_frame.pack()


    #FIRST CARD IMAGE
    not_resized_img = Image.open("cards/default.png")
    img = not_resized_img.resize((55, 85))
    first_card = pil.ImageTk.PhotoImage(img)

    first_card_image = tk.Label(image = first_card)
    first_card_image.image = first_card

    first_card_image.place(x=50, y=50)

    
    #SECOND CARD IMAGE
    second_card = pil.ImageTk.PhotoImage(img)
    second_card_image = tk.Label(image = second_card)
    second_card_image.place(x=110, y=50)




    root.mainloop()







def main(): #main
    # GUI_start_frame()
    
    human_vs_computer()
    


if __name__ == "__main__":
    main()
