import re

def add(input: str) -> int:
    if not input:
        return 0
    separators = [',', '\n']

    match_chosen_separator = re.match(r"//(\D+)\n", input)

    if match_chosen_separator:
        separators = [match_chosen_separator.group(1)]
        prefix_to_remove = input[match_chosen_separator.start():match_chosen_separator.end()]
        input = input.removeprefix(prefix_to_remove)

    numbers = input.split(separators.pop())
    for sep in separators:
        numbers = sum([n.split(sep) for n in numbers], start=[])
    
    if '' in numbers:
        raise ExceptionSeparatorAtTheEnd()

    numbers_sum = 0
    for n in numbers:
        numbers_sum += int(n)
    return numbers_sum

class ExceptionSeparatorAtTheEnd(Exception):
    ...
