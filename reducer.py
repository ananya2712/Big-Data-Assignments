#!/usr/bin/env python3

import sys

current_state = None
current_city = None
current_count = 0
total_count = 0

for line in sys.stdin:

    try:
        line = line.strip()
        state, city, count = line.split(',')
        state = state.strip()
        city = city.strip()
        count = count.strip()
        count = int(count)
    except BaseException:
        continue

    if current_state is None:
        current_state = state
        total_count = count
        current_count = count
        current_city = city
        print(state)
        continue

    if current_state != state:
        print(current_city, current_count)
        print(current_state, total_count)
        current_state = state
        current_city = city
        current_count = count
        total_count = count
        print(state)
        continue

    if current_city != city:
        print(current_city, current_count)
        current_city = city
        current_count = count
        total_count += count
        continue

    total_count += count
    current_count += count


print(current_city, current_count)
print(current_state, total_count)
