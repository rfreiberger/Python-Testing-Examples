#!/usr/bin/env python3
# Author: Robert Freiberger
# Title: process_check.py
# Notes: A simple test of subprocess and testing
# Date: 1/20/2017
# Repo:
# License: BSD

import subprocess


def decoder(coded_string):
    return coded_string.decode('UTF-8')


def command_run(command):
    results = subprocess.Popen(
            command,
            shell=True,
            stdin=subprocess.PIPE,
            stdout=subprocess.PIPE,
            stderr=subprocess.PIPE,
            )
    stdout_value, stderr_value = results.communicate()
    if stderr_value:
        print("### Error Output ###")
        print(decoder(stderr_value))
        print("### Error Output ###")
    else:
        return decoder(stdout_value)


def level_range(current_value, max_value):
    percent_value = int(100 * (current_value / max_value))
    if percent_value >= 0 and percent_value <= 25:
        return_message = "Value is near zero"
    elif percent_value >= 26 and percent_value <= 50:
        return_message = "Value is low"
    elif percent_value >= 51 and percent_value <= 75:
        return_message = "Value is medium"
    elif percent_value >= 76 and percent_value <= 100:
        return_message = "Value is high"
    return return_message


def level_alert(current_value, max_value):
    ## Alerts when current value is above max value
    if current_value >= max_value:
        return "Alert!!! - threshold passed!!!"
    else:
        return "Value below alerting threhold."

# Define the commands and alerts
cmd_results = int((command_run('ps aux | grep root | wc -l')))
print(level_range(cmd_results, 200))
print(level_alert(cmd_results, 200))
