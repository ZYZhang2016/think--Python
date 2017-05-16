#coding:utf-8
import random

class Card(object):
	'''reprensts a card game

	'''
	def __init__(self,suit=0,rank=2):
		self.suit = suit
		self.rank = rank

	suits_name = ['Club','Diamond','Hearts','Spades']
	rank_name = [None,'1','2','3','4','5','6','7','8','9','10','Jack','Queen','King']

	def __str__(self):
		return '{} of {}'.format(self.rank_name[self.rank],self.suits_name[self.suit])

	def __cmp__(self, other):
		t1 = self.rank,self.suit
		t2 = other.rank,other.suit
		return cmp(t1,t2)

class Deck(object):
	'''create a set of cards

	'''
	def __init__(self):
		self.cards = []
		for suit in range(4):
			for rank in range(1,14):
				card = Card(suit,rank)
				self.cards.append(card)

	def __str__(self):
		res = []
		for card in self.cards:
			res.append(str(card))
		return '\n'.join(res)

	def pop_card(self):
		return self.cards.pop()

	def add_card(self,card):
		self.cards.append(card)

	def shuffle(self):
		random.shuffle(self.cards)

	def sort(self):
		self.cards.sort(cmp=Card.__cmp__())

	def move_cards(self,hand,num_cards):
		for i in range(num_cards):
			hand.add_card(self.pop_card())

	def deal_hand(self,num_hands,num_per_hand):
		for hand in range(num_hands):
			hand_name = 'Hand: '+str(hand+1)
			hand = Hand(hand_name)
			print hand_name+' is created'
			for num_cards in range(num_per_hand):
				hand.add_card(self.pop_card())
			print 'Hand has cards'
			print '#######################'
			hands = []
			hands.append(hand)
		return hands

class Hand(Deck):
	'''手牌类，继承自桌面牌,

	'''
	def __init__(self,lable=''):
		self.cards = []
		self.lable = lable



def main():
	#拿出一刀牌
	card = Card()
	deck = Deck()
	#洗牌
	deck.shuffle()

	#发牌，两人，每人17张
	deck.deal_hand(2,17)

if __name__=='__main__':
	main()