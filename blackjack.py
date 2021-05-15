import random
class Card:
    def __init__(self, suit, value):
        self.suit = suit
        self.value = value
    def __repr__(self):
        # return " of ".join((self.value, self.suit))
        return "".join((self.suit, self.value))
#"Spades", "Clubs", "Hearts", "Diamonds"
class Deck:
    def __init__(self):
        self.cards = [Card(s, v) for s in ["黑桃", "梅花", "红桃",
        "方块"] for v in ["A", "2", "3", "4", "5", "6",
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

class Game:
    def __init__(self):
        playing = True
        while playing:
            self.deck = Deck()
            self.deck.shuffle()
            self.player_hand = Hand()
            self.dealer_hand = Hand(dealer=True)
            for i in range(2):
                self.player_hand.add_card(self.deck.deal())
                self.dealer_hand.add_card(self.deck.deal())
            print("你手中的牌:")
            self.player_hand.display()
            print()
            print("对手的牌:")
            self.dealer_hand.display()

            game_over = False
            has_won = False
            while not game_over:
                player_has_blackjack, dealer_has_blackjack = self.check_for_blackjack()
                if player_has_blackjack or dealer_has_blackjack:
                    game_over = True
                    self.show_blackjack_results(player_has_blackjack, dealer_has_blackjack)
                    continue
                choice = input("请选择 [Hit / Stick] ").lower()
                while choice not in ["h", "s", "hit", "stick"]:
                    choice = input("请输入 'hit' 或者 'stick' (或者 H/S) ").lower()
                if choice in ['hit', 'h']:
                    self.player_hand.add_card(self.deck.deal())
                    self.player_hand.display()
                    # print()
                    # self.dealer_hand.display()
                    
                    if self.player_is_over():
                        print("You have lost!")
                        has_won = True
                else:
                    print("最终结果")
                    print("你手中的牌:", self.player_hand.get_value())
                    print("对手的牌:", self.dealer_hand.get_value())
                    if self.player_hand.get_value() > self.dealer_hand.get_value():
                        print("You Win!")
                        break
                    else:
                        print("Dealer Wins!")
                        has_won = True
                if has_won:
                    game_over = True
            again = input("再来一局? [Y/N] ")
            while again.lower() not in ["y", "n"]:
                again = input("请输入 Y or N ")
            if again.lower() == "n":
                print("期待下次再玩!")
                playing = False
            else:
                has_won = False


    def check_for_blackjack(self):
        player = False
        dealer = False
        if self.player_hand.get_value() == 21:
            player = True
        if self.dealer_hand.get_value() == 21:
            dealer = True
        return player, dealer

    def show_blackjack_results(self, player_has_blackjack,dealer_has_blackjack):
        if player_has_blackjack and dealer_has_blackjack:
            print("Both players have blackjack! Draw!")
        elif player_has_blackjack:
            print("You have blackjack! You win!")
        elif dealer_has_blackjack:
            print("Dealer has blackjack! Dealer wins!")

    def player_is_over(self):
        return self.player_hand.get_value() > 21


if __name__ == "__main__":
    game = Game()
