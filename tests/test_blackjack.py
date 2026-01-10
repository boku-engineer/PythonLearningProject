import sys
import os

# Add project root to path so we can import the module
sys.path.insert(0, os.path.dirname(os.path.dirname(os.path.abspath(__file__))))

from learning_blackjack import deal_card, calculate_score, is_blackjack, cards


class TestDealCard:
    def test_deal_card_returns_valid_card(self):
        """deal_card should return a card value between 2 and 11"""
        card = deal_card()
        assert card in cards

    def test_deal_card_returns_integer(self):
        """deal_card should return an integer"""
        card = deal_card()
        assert isinstance(card, int)


class TestCalculateScore:
    def test_calculate_score_simple_hand(self):
        """Simple hand without aces"""
        hand = [10, 5, 3]
        assert calculate_score(hand) == 18

    def test_calculate_score_with_ace_no_bust(self):
        """Hand with ace that doesn't need conversion"""
        hand = [11, 5]  # Ace + 5 = 16
        assert calculate_score(hand) == 16

    def test_calculate_score_converts_ace_when_bust(self):
        """Ace should convert from 11 to 1 when hand would bust"""
        hand = [11, 10, 5]  # 11+10+5=26, convert ace: 1+10+5=16
        assert calculate_score(hand) == 16

    def test_calculate_score_converts_multiple_aces(self):
        """Multiple aces should convert as needed"""
        hand = [11, 11, 10]  # 32 -> 22 -> 12
        assert calculate_score(hand) == 12

    def test_calculate_score_empty_hand(self):
        """Empty hand should return 0"""
        hand = []
        assert calculate_score(hand) == 0

    def test_calculate_score_blackjack(self):
        """Blackjack hand (Ace + 10) should equal 21"""
        hand = [11, 10]
        assert calculate_score(hand) == 21


class TestIsBlackjack:
    def test_is_blackjack_with_ace_and_ten(self):
        """Ace + 10 is blackjack"""
        hand = [11, 10]
        assert is_blackjack(hand) is True

    def test_is_blackjack_with_ace_and_face_card(self):
        """Ace + face card (value 10) is blackjack"""
        hand = [10, 11]  # Order shouldn't matter
        assert is_blackjack(hand) is True

    def test_is_blackjack_false_for_three_cards(self):
        """21 with 3 cards is not blackjack"""
        hand = [7, 7, 7]  # 21 but not blackjack
        assert is_blackjack(hand) is False

    def test_is_blackjack_false_for_non_21(self):
        """Non-21 hand is not blackjack"""
        hand = [10, 5]
        assert is_blackjack(hand) is False
