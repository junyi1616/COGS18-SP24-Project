# This file includes the tests for our chatbot.

import unittest
from unittest.mock import patch
from io import StringIO
from chatbot import RestaurantChatbot, start_chatbot

class TestRestaurantChatbot(unittest.TestCase):
    def test_display_menu(self):
        bot = RestaurantChatbot()
        with patch('sys.stdout', new=StringIO()) as fake_out:
            bot.display_menu()
            output = fake_out.getvalue().strip()
            self.assertIn("Menu:", output)

    def test_take_order(self):
        bot = RestaurantChatbot()
        with patch('builtins.input', side_effect=['Sweet and Sour Pork', '2', 'done']), \
             patch('sys.stdout', new=StringIO()) as fake_out:
            bot.take_order()
            self.assertEqual(bot.order['Sweet and Sour Pork'], 2)

    def test_calculate_total(self):
        bot = RestaurantChatbot()
        bot.order = {'Sweet and Sour Pork': 2, 'Fried Rice': 1}
        total = bot.calculate_total()
        self.assertEqual(total, 2 * 12.5 + 1 * 7.5)

    def test_process_payment(self):
        bot = RestaurantChatbot()
        with patch('builtins.input', return_value='30'), \
             patch('sys.stdout', new=StringIO()) as fake_out:
            bot.process_payment(30)
            output = fake_out.getvalue().strip()
            self.assertIn("Thank you for your payment.", output)

if __name__ == '__main__':
    unittest.main()
