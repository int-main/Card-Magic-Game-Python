#!/usr/bin/python3
import random
from os import system,name

no_pattern_mode = True

card_numbers = ['A','2','3','4','5','6','7','8','9','10','J','Q','K']
card_types = ['Clubs','Diamonds','Hearts','Spades']

#makes 4 decks each containing 13 cards
def make_four_decks(all_cards):
	decks = [[],[],[],[]]
	while all_cards != []:
		for i in range(4):
			decks[i].append(all_cards.pop())
	return decks

#prints cards in each deck and asks the user in which deck his/her selected card is		
def question(decks):
	if name == 'nt':
		system('cls')
	else:
		system('clear')
	all_decks = [i[:] for i in decks] #make a deep copy of original decks(required in case of no_pattern_mode)
	#randomly shuffle cards in all decks before displaying
	if no_pattern_mode:
		for i in all_decks:
			random.shuffle(i)
	print("\n  %-15s  %-15s %-15s %-15s"%('Deck 1','Deck 2','Deck 3','Deck 4'))
	print("="*64)
	for i in range(13):
			print("%-15s %-15s %-15s %-15s"%(all_decks[0][i],all_decks[1][i],all_decks[2][i],all_decks[3][i]))

	ch = int(input('\nEnter the deck number which contains your chosen card: '))
	return ch

#function for pushing card decks to stack
def push_cards(all_cards,decks,ch):
	for i in range(4):
		if i != ch-1:
			all_cards.extend(decks[i])

#class for storing Card information
class Card:
	def __init__(self,number,card_type):
		self.number = number
		self.card_type = card_type
	def __repr__(self):
		return self.number+' of '+self.card_type

all_cards = [Card(card_numbers[i],card_types[j]) for i in range(13) for j in range(4)] #create all 52 cards
random.shuffle(all_cards) #Shuffle all cards in deck

print("\nList of all cards after shuffling:\n")
for i in all_cards:
	print(i)
input("\nChoose any one card from deck and remember it. Press Enter key when you have chosen...")


decks = make_four_decks(all_cards)
ch = question(decks)
all_cards = decks[ch-1] #push chosen deck first in stack
push_cards(all_cards,decks,ch) #push the remaining decks in stack

decks = make_four_decks(all_cards)
ch = question(decks)
all_cards = [] #empty stack
push_cards(all_cards,decks,ch) #push all decks in stack except the chosen deck
all_cards.extend(decks[ch-1]) #push the chosen deck in stack

decks = make_four_decks(all_cards)
ch = question(decks)

print("\n\nYour chosen card is: %s\n"%(decks[ch-1][0]))
