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



def text_of_image(value, suit):
    value_text = ""
    suit_text = ""

    if value == 1:
        value_text = "Ace"
    
    if value == 2:
        value_text = "Two"

    if value == 3:
        value_text = "Three"

    if value == 4:
        value_text = "Four"

    if value == 5:
        value_text = "Five"

    if value == 6:
        value_text = "Six"

    if value == 7:
        value_text = "Seven"

    if value == 8:
        value_text = "Eight"

    if value == 9:
        value_text = "Nine"

    if value == 10:
        value_text = "Ten"

    if value == 12:
        value_text = "Jack"

    if value == 13:
        value_text = "Queen"

    if value == 14:
        value_text = "King"


    if suit == 0:
        suit_text = "Spades"

    if suit == 1:
        suit_text = "Hearts"

    if suit == 2:
        suit_text = "Diamonds"

    if suit == 3:
        suit_text = "Clubs"

    return value_text, suit_text
    



def human_vs_computer(): # human vs computer
    
    #CLASSES HERE

    class Card: #class for attributes of a Card
        def __init__(self, card_value, card_suit):
            self.card_value = card_value
            self.card_suit = card_suit

    class Deck(list): #class for attributes of entire deck of cards////// INHERITANCE from list class, so we can use append, pop and so on...
        def __init__(self):
            number_of_values = 14 # Ace is either 1 or 11
            number_of_suits = 4 #Spades, Hearts, Diamonds, Clubs

            #now we generate all the posibilities and assign it to a Card obj which is placed into a list
            for suit in range (0, number_of_suits):
                for value in range (0, number_of_values):
                    if value != 10:
                        self.append(Card(value + 1, suit))
                        # print(text_of_image(value, suit))
                    

            
        
        def shuflle_deck(self): #shuffle the deck
            random.shuffle(self)
        
        def pop_a_card(self, index): #pop a card after it been dealt
            self.pop(index)


    
    
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



    standard_deck = Deck() # we get the deck, so we can give each computer and user 2 random cards
    standard_deck.shuflle_deck() #we shuffle the deck



    # COMPUTER FIRST CARD IMAGE

    computer_first_card_index = random.randint(0, len(standard_deck) - 1)
    computer_get_first_card = standard_deck[computer_first_card_index]
    computer_first_card_tuple = text_of_image(computer_get_first_card.card_value, computer_get_first_card.card_suit)
    print("Computer first card = " + (str)(computer_first_card_tuple))
    standard_deck.pop(computer_first_card_index)

    computer_second_card_index = random.randint(0, len(standard_deck) - 1)
    computer_get_second_card = standard_deck[computer_second_card_index]
    computer_second_card_tuple = text_of_image(computer_get_second_card.card_value, computer_get_second_card.card_suit)
    print("Computer seoncd card = " + (str)(computer_second_card_tuple))

    standard_deck.pop(computer_second_card_index)


    not_resized_img = Image.open("cards/default.png")
    img = not_resized_img.resize((55, 85))
    computer_first_card = pil.ImageTk.PhotoImage(img)

    computer_first_card_image = tk.Label(image = computer_first_card)
    computer_first_card_image.image = computer_first_card

    computer_first_card_image.place(x=50, y=50)

    
    #COMPUTER SECOND CARD IMAGE
    second_card = pil.ImageTk.PhotoImage(img)
    second_card_image = tk.Label(image = second_card)
    second_card_image.place(x=110, y=50)



    #USER FIRST CARD IMAGE
    
    user_first_card_index = random.randint(0, len(standard_deck) - 1) #we get the first card index ---- random
    # print("Index = " + (str)(user_first_card_index))
    user_get_first_card = standard_deck[user_first_card_index] # we get the card from the list of cards

    # print(text_of_image(user_get_first_card.card_value, user_get_first_card.card_suit))

    user_first_card_tuple = text_of_image(user_get_first_card.card_value, user_get_first_card.card_suit)
    print("User first card = " + (str)(user_first_card_tuple))
    user_first_card_image_name = user_first_card_tuple[0] + " of " + user_first_card_tuple[1] + ".png" #we get the name of the image of the card that has been selected

    #we insert the first user card into the display
    not_resized_img = Image.open("cards/"+user_first_card_image_name)
    img = not_resized_img.resize((55,85))
    user_first_card = pil.ImageTk.PhotoImage(img)
    user_first_card_image = tk.Label(image = user_first_card)
    user_first_card_image.image = user_first_card
    user_first_card_image.place(x=50, y=900)


    #we pop the card
    standard_deck.pop_a_card(user_first_card_index)


     #USER SECOND CARD IMAGE - SAME AS  #USER FIRST CARD IMAGE
    user_second_card_index = random.randint(0, len(standard_deck) - 1)
    user_get_second_card = standard_deck[user_second_card_index]
    user_second_card_tuple = text_of_image(user_get_second_card.card_value, user_get_second_card.card_suit)
    print("User second card = " + (str)(user_second_card_tuple))
    user_second_card_image_name = user_second_card_tuple[0] + " of " + user_second_card_tuple[1] + ".png"
    not_resized_img = Image.open("cards/"+user_second_card_image_name)
    img = not_resized_img.resize((55,85))
    user_second_card = pil.ImageTk.PhotoImage(img)
    user_second_card_image = tk.Label(image = user_second_card)
    user_second_card_image.image = user_second_card
    user_second_card_image.place(x=110, y=900)
    standard_deck.pop_a_card(user_second_card_index)






    # #Deck
    # standard_deck = Deck()
    # for c in standard_deck:
    #     tuple_v_s = text_of_image(c.card_value, c.card_suit)
    #     print(tuple_v_s)
    #     # print(c.card_value)

    root.mainloop()







def main(): #main
    # GUI_start_frame()
    
    human_vs_computer()
    


if __name__ == "__main__":
    main()
