#!/usr/bin/env python3

import unittest
from process_check import command_run
from process_check import level_alert
from process_check import level_range

class ProcessTestCase(unittest.TestCase):
    """Testing the process_check script"""

    def test_command_run(self):
        # 
        # 
        command_string = command_run("uname")
        self.assertEqual(command_string, "Darwin\n")

    def test_level_range(self):
        c_value = 75
        m_value = 100
        l_results = level_range(c_value, m_value)
        self.assertEqual(l_results, "Value is medium")

    def test_level_alert(self):
        c_value = 10
        m_value = 20
        a_results = level_alert(c_value, m_value)
        self.assertEqual(a_results, "Value below alerting threhold.")

unittest.main()
