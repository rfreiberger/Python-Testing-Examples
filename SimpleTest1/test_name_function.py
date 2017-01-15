#!/usr/bin/env python3

import unittest
from name_function import get_formatted_name
from hello_world import hello_world
from good_bye import good_bye

class NamesTestCase(unittest.TestCase):
    """Test for 'name_function.py'."""

    def test_first_last_name(self):
        """Do names like 'Janis Joplin' work?"""
        formatted_name = get_formatted_name('janis', 'joplin')
        self.assertEqual(formatted_name, 'Janis Joplin')

    def test_hello_world(self):
        """Will this return 'Hello World!'?"""
        hello_world_test = hello_world()
        self.assertEqual(hello_world_test, 'Hello World!')

    def test_good_bye(self):
        """Will this return 'Good Bye!'?"""
        good_bye_test = good_bye()
        self.assertEqual(good_bye_test, 'Good Bye!')

    def test_good_bye2(self):
        """This will fail"""
        good_bye_test2 = good_bye()
        self.assertEqual(good_bye_test2, 'Good bye!')

unittest.main()
