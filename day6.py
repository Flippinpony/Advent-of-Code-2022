
data = ""
input = ""
packet_index = 0
message_index = 0

with open("input/day6input.txt") as file:
    data = file.read()
    while (packet_index < len(data)-3):
        input = data[packet_index:packet_index+4]
        dupe_found = False
        for char in input:
            if input.count(char) > 1:
                dupe_found = True
                continue
        if dupe_found:
            packet_index += 1
        else:
            break

print(packet_index + 4)

while (message_index < len(data)-13):
        input = data[message_index:message_index+14]
        dupe_found = False
        for char in input:
            if input.count(char) > 1:
                dupe_found = True
                continue
        if dupe_found:
            message_index += 1
        else:
            break

print(message_index + 14)