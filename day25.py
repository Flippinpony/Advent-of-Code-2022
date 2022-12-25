def dec_to_snafu(dec):
    snafu_chars = ['=','-','0','1','2']
    digits = []
    while dec:
        # shift value up 2 so we can treat it like normal base 5, remap it later
        base5_digit = (dec + 2) % 5
        dec = (dec + 2) // 5
        digits += snafu_chars[base5_digit]
    return ''.join(digits[::-1])

def snafu_to_dec(snafu):
    power = 0
    total = 0
    for char in snafu[::-1]:
        val = char
        if val == '-': val = -1
        elif val == '=': val = -2
        total += int(val) * pow(5,power)
        power += 1
    return total


def import_values():
    values = []
    with open("input/day25input.txt") as file:
        for line in file:
            values.append(line.strip())
    return values


# driver
values = import_values()
converted = []
total = 0
for value in values:
    converted.append(snafu_to_dec(value))
for conv in converted:
    total += conv
snafu_total = dec_to_snafu(total)
print(f"Part 1 answer: {snafu_total}")