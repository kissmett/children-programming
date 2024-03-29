import os
import random
import tkinter as tk
from PIL import ImageTk

assets_folder = os.path.abspath('.')+'\\assets_en'
print(assets_folder)
class Card:
    def __init__(self, suit, value):
        self.suit = suit
        self.value = value
    def __repr__(self):
        # return " of ".join((self.value, self.suit))
        return "".join((self.suit, self.value))
    def get_file(self):
        print('get_file:',self.suit,self.value)
        # return ImageTk.PhotoImage(file=assets_folder + "\\back.jpg" ) 
        return ImageTk.PhotoImage(file=assets_folder + "\\%s%s.jpg" %(self.suit,self.value)) 
        # return assets_folder + "\\%s%s.jpg" %(self.suit,self.value)
    @classmethod
    def get_back_file(cls):
        cls.back = ImageTk.PhotoImage(file=assets_folder + "\\back.jpg")        
        return cls.back
#"Spades", "Clubs", "Hearts", "Diamonds"
class Deck:
    def __init__(self):
        self.cards = [Card(s, v) for s in [
        "Spades", 
        "Clubs", 
        "Hearts",
        "Diamonds"] for v in ["A", "2", "3", "4", "5", "6",
        "7", "8", "9", "10", "J", "Q", "K"]]
    def shuffle(self):
        if len(self.cards) > 1:
            random.shuffle(self.cards)
    def deal(self):
        if len(self.cards) > 1:
            return self.cards.pop(0)

class Hand:
    def __init__(self, dealer=False):
        self.dealer = dealer
        self.cards = []
        self.value = 0
    def add_card(self, card):
        self.cards.append(card)
    def calculate_value(self):
        self.value = 0
        has_ace = False
        for card in self.cards:
            if card.value.isnumeric():
                self.value += int(card.value)
            else:
                if card.value == "A":
                    has_ace = True
                    self.value += 11
                else:
                    self.value += 10
        if has_ace and self.value > 21:
            self.value -= 10

    def get_value(self):
        self.calculate_value()
        return self.value
    def display(self):
        if self.dealer:
            print("隐藏牌")
            print(self.cards[1])
        else:
            for card in self.cards:
                print(card)
            print("牌面总分:", self.get_value())
class GameState:
    def __init__(self):
        self.deck = Deck()
        self.deck.shuffle()
        self.player_hand = Hand() #玩家
        self.dealer_hand = Hand(dealer=True) #发牌者
        for i in range(2):
            self.player_hand.add_card(self.deck.deal())
            self.dealer_hand.add_card(self.deck.deal())
        self.has_winner = ''

#    def check_for_blackjack(self):
#         player = False
#         dealer = False
#         if self.player_hand.get_value() == 21:
#             player = True
#         if self.dealer_hand.get_value() == 21:
#             dealer = True
#         return player, dealer

    def someone_has_blackjack(self):
        player = False
        dealer = False
        if self.player_hand.get_value() == 21:
            player = True
        if self.dealer_hand.get_value() == 21:
            dealer = True
        if player and dealer:
            return 'dp'
        elif player:
            return 'p'
        elif dealer:
            return 'd'
        return False
    
    # def show_blackjack_results(self, player_has_blackjack,dealer_has_blackjack):
    #     if player_has_blackjack and dealer_has_blackjack:
    #         print("Both players have blackjack! Draw!")
    #     elif player_has_blackjack:
    #         print("You have blackjack! You win!")
    #     elif dealer_has_blackjack:
    #         print("Dealer has blackjack! Dealer wins!")

    def player_is_over(self):
        return self.player_hand.get_value() > 21
    #叫牌
    def hit(self):
        self.player_hand.add_card(self.deck.deal())
        if self.someone_has_blackjack() == 'p':
            self.has_winner = 'p'
        if self.player_is_over():
            self.has_winner = 'd'
        return self.has_winner
    def get_table_state(self):
        blackjack = False
        winner = self.has_winner
        if not winner:
            winner = self.someone_has_blackjack()
            if winner:
                blackjack = True
        table_state = {
            'player_cards': self.player_hand.cards,
            'dealer_cards': self.dealer_hand.cards,
            'has_winner': winner,
            'blackjack': blackjack,
            }
        return table_state
    def calculate_final_state(self):
        player_hand_value = self.player_hand.get_value()
        dealer_hand_value = self.dealer_hand.get_value()
        if player_hand_value == dealer_hand_value:
            winner = 'dp'
        elif player_hand_value > dealer_hand_value:
            winner = 'p'
        else:
            winner = 'd'
        table_state = {
        'player_cards': self.player_hand.cards,
        'dealer_cards': self.dealer_hand.cards,
        'has_winner': winner,
        }
        return table_state
    def player_score_as_text(self):
        return "Score: " + str(self.player_hand.get_value())

class GameScreen(tk.Tk):
    def __init__(self):
        super().__init__()
        self.title("21点")
        self.geometry("800x640")
        self.resizable(False, False)

        self.CARD_ORIGINAL_POSITION = 100
        self.CARD_WIDTH_OFFSET = 150
        self.PLAYER_CARD_HEIGHT = 300
        self.DEALER_CARD_HEIGHT = 100
        self.PLAYER_SCORE_TEXT_COORDS = (400, 450)
        self.WINNER_TEXT_COORDS = (400, 250)

        self.game_state = GameState()
        self.game_screen = tk.Canvas(self, bg="white", width=800, height=500)

        self.bottom_frame = tk.Frame(self, width=800, height=140, bg="gray")
        self.bottom_frame.pack_propagate(0)

        self.hit_button = tk.Button(self.bottom_frame, text="要牌", width=25, command=self.hit)
        self.stick_button = tk.Button(self.bottom_frame, text="停牌", width=25, command=self.stick)
        self.play_again_button = tk.Button(self.bottom_frame, text="再玩一局", width=25, command=self.play_again)
        self.quit_button = tk.Button(self.bottom_frame, text="退出", width=25, command=self.destroy)

        self.hit_button.pack(side=tk.LEFT, padx=(100, 200))
        self.stick_button.pack(side=tk.LEFT)
        self.bottom_frame.pack(side=tk.BOTTOM, fill=tk.X)
        self.game_screen.pack(side=tk.LEFT, anchor=tk.N)

        self.display_table()

    def display_table(self, hide_dealer=True, table_state=None):
        if not table_state:
            table_state = self.game_state.get_table_state()
        self.player_card_images = [card.get_file() for card in
            table_state['player_cards']]
        self.dealer_card_images = [card.get_file() for card in
            table_state['dealer_cards']]
        if hide_dealer and not table_state['blackjack']:
            self.dealer_card_images[0] = Card.get_back_file()
            pass

        self.game_screen.delete("all")
        self.tabletop_image = ImageTk.PhotoImage(file=assets_folder + "\\tabletop.jpg")
        self.game_screen.create_image((400, 250), image=self.tabletop_image)

        for card_number, card_image in enumerate(self.player_card_images):
            print('player create_image:',card_number,card_image)
            self.game_screen.create_image(
                (self.CARD_ORIGINAL_POSITION + self.CARD_WIDTH_OFFSET * card_number, self.PLAYER_CARD_HEIGHT),
                image=card_image
            )
        for card_number, card_image in enumerate(self.dealer_card_images):
            print('dealer create_image:',card_number,card_image)
            self.game_screen.create_image(
                (self.CARD_ORIGINAL_POSITION + self.CARD_WIDTH_OFFSET * card_number, self.DEALER_CARD_HEIGHT),
                image=card_image
            )
        if table_state['has_winner']:
            if table_state['has_winner'] == 'p':
                self.game_screen.create_text(self.WINNER_TEXT_COORDS,
                text="你赢了!", font=(None, 50))
            elif table_state['has_winner'] == 'dp':
                self.game_screen.create_text(self.WINNER_TEXT_COORDS, text="平局!",
                font=(None, 50))
            else:
                self.game_screen.create_text(self.WINNER_TEXT_COORDS,
                text="对手赢!", font=(None, 50))
            self.show_play_again_options()

    def show_play_again_options(self):
        self.hit_button.pack_forget()
        self.stick_button.pack_forget()
        self.play_again_button.pack(side=tk.LEFT, padx=(100, 200))
        self.quit_button.pack(side=tk.LEFT)
    #发牌    
    def hit(self):
        self.game_state.hit()
        self.display_table()
    #停牌    
    def stick(self):
        table_state = self.game_state.calculate_final_state()
        self.display_table(False, table_state)
    def play_again(self):
        self.show_gameplay_buttons()
        self.game_state = GameState()
        self.display_table()
    def show_gameplay_buttons(self):
        self.play_again_button.pack_forget()
        self.quit_button.pack_forget()
        self.hit_button.pack(side=tk.LEFT, padx=(100, 200))
        self.stick_button.pack(side=tk.LEFT)

if __name__ == "__main__":
    # s = tk.Tk()
    # game_screen = tk.Canvas(s, bg="white", width=800, height=500)
    # Card.get_back_file() #独立使用会报错: RuntimeError: Too early to create image; 需要首先创建根元素(tk.Tk()),然后创建其余的小部件
    # s.mainloop()

    gs = GameScreen()
    # Card.get_back_file() # this is OK.
    gs.mainloop()
