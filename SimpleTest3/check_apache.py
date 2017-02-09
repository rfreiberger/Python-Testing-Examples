from __future__ import print_function
#!/usr/bin/env python
# author: Robert Freiberger
# date: 1/26/2017
# license: BSD
# notes: Just testing how to test with unittest

import re
import subprocess

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
        return("1")
    else:
        return(stdout_value)

def linux_command(system_services, action="status"):
    full_command = ("service " + system_services + " " + action)
    return(full_command)

def check_curl(curl_command_result, expected_return):
    if re.search(expected_return, curl_command_result):
        return("No action taken")
        return("0")
    else:
        return("1")

def system_check(system_service, command_result):
    if command_result == "0":
        return("0")
    else:
        return(system_service + " failed")
        return("1")

def service_check_cmd(service):
    command_check = "ps aux | grep " + service + " | grep -v grep"
    return(command_check)

def main():
    # Main variables
    url_curl_command = "curl -I http://hostname/index.html"
    url_curl = "http://hostname/index.html"
    url_return = "HTTP/1.1 200 OK"
    system_services = ['httpd']
    # Main logic
    if check_curl(command_run(url_curl_command), url_return) == "0":
        print("No action taken")
        return("0")
    else:
        for services in system_services:
            if system_check(services, command_run(linux_command(services, "stop"))) == "0":
                if command_run(services_check_cmd(services)) == "0":
                    return("0")
                else:
                    print("Services still running")
                    return("1")
            else:
                print("Service stop failure")
                return("1")
            if system_check(services, command_run(linux_command(services, "start"))) == "0":
                if check_curl(command_run(url_curl_command), url_return) == "0":
                    print("Services are up and running")
                    return("0")
                else:
                    print("Services are still down, please escalate!")
                    return("1")

if __name__ == "__main__":
    main()
