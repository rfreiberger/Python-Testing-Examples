#!/usr/bin/env python3

from name_function import get_formatted_name
from hello_world import hello_world
from good_bye import good_bye

print("Enter 'q' at any time to quit.")
while True:
    first = input("\nPlease give me a first name: ")
    if first == 'q':
        break
    last = input("Please give me a last name: ")
    if last == 'q':
        break

    formatted_name = get_formatted_name(first, last)
    print("\nNeatly formatted name: " + formatted_name + '.')

    hello_world_fun = hello_world()
    print(hello_world_fun)

    good_bye = good_bye()
    print(good_bye)
