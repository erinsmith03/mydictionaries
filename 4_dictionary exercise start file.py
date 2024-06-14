# This program uses a dictionary as a deck of cards.

import random
def main():

    # Create a deck of cards.
    mydeck=create_deck()#dont need to put anything in () bc there are no parameters
    #mydeck is going to be a dictionary of all these cards
    #create deck is value returning, so it must be stored in a variable so that we can use it


    # Get the number of cards to deal.
    num_cards = int(input('How many cards should I deal? '))



    # Deal the cards.
    deal_cards(mydeck,num_cards)#variable is a storage location, and u have to call those two objects
    #program knows what to do with it when we call it

    
    #keys HAVE to be unique, but the values dont

# The create_deck function returns a dictionary
# representing a deck of cards.
def create_deck():
    # Create a dictionary with each card and its value
    # stored as key-value pairs.
    deck = {'Ace of Spades':1, '2 of Spades':2, '3 of Spades':3,
            '4 of Spades':4, '5 of Spades':5, '6 of Spades':6,
            '7 of Spades':7, '8 of Spades':8, '9 of Spades':9,
            '10 of Spades':10, 'Jack of Spades':10,
            'Queen of Spades':10, 'King of Spades': 10,
            
            'Ace of Hearts':1, '2 of Hearts':2, '3 of Hearts':3,
            '4 of Hearts':4, '5 of Hearts':5, '6 of Hearts':6,
            '7 of Hearts':7, '8 of Hearts':8, '9 of Hearts':9,
            '10 of Hearts':10, 'Jack of Hearts':10,
            'Queen of Hearts':10, 'King of Hearts': 10,
            
            'Ace of Clubs':1, '2 of Clubs':2, '3 of Clubs':3,
            '4 of Clubs':4, '5 of Clubs':5, '6 of Clubs':6,
            '7 of Clubs':7, '8 of Clubs':8, '9 of Clubs':9,
            '10 of Clubs':10, 'Jack of Clubs':10,
            'Queen of Clubs':10, 'King of Clubs': 10,
            
            'Ace of Diamonds':1, '2 of Diamonds':2, '3 of Diamonds':3,
            '4 of Diamonds':4, '5 of Diamonds':5, '6 of Diamonds':6,
            '7 of Diamonds':7, '8 of Diamonds':8, '9 of Diamonds':9,
            '10 of Diamonds':10, 'Jack of Diamonds':10,
            'Queen of Diamonds':10, 'King of Diamonds': 10}

    # Return the deck.
    return deck



# The deal_cards function deals a specified number of cards
# from the deck.

def deal_cards(deck, number): #these are local variable assignments, now that we are in the function, the variable names change to local ones
    # Initialize an accumulator for the hand value.
    hand_value=0
    if number>52:
        number=52 #we dont have to ask the user for more bc we assume they dont want more

    for x in range(number): #loop as many times as user asks for cards
        #we want a random key value, and then pop it out of the deck
        #card,value=deck.popitem() #its a tuple, so that comma separates the two variables into the two distinct ones
        card=random.choice(list(deck)) #converting keys into list

        print(card)
        value=deck[card] #card is the key, so giving the key to a dictionary u get the value
        hand_value+=value
        #we need to remove it from the dictionary so the card doesnt show up again 
        del deck[card]
    print(f'The value of the hand is: {hand_value}')
    
    
    # DATA VALIDATION
    # Make sure the number of cards to deal is not
    # greater than the number of cards in the deck (52).

    
    

    # Deal the cards and accumulate their values.
    


    

    # Display the value of the hand.

    
    

# Call the main function.
main()
