from sympy import Eq, Symbol, solve, sympify

def load_monkeys():
    monkeys = {}
    with open("input/day21input.txt") as file:
        for line in file:
            split = line.split(":")
            monkeys[split[0]] = split[1].strip()
    return monkeys    

def sim_monkeys(monkeys):
    time = 1
    to_process = monkeys.copy()
    registers = {}
    to_remove = set()
    # initial step - cache constants
    for monkey in to_process:
        if to_process[monkey].isdigit():
            registers[monkey] = int(to_process[monkey])
            to_remove.add(monkey)
    to_process = {k: v for k, v in to_process.items() if k not in to_remove}
    to_remove.clear()
    # Now iterate through list looking for equations we can solve until we're done
    while to_process:
        time += 1
        for monkey in to_process:
            split = to_process[monkey].split(" ")
            if split[0] in registers and split[2] in registers:
                to_remove.add(monkey)
                statement = to_process[monkey].replace(split[0],str(registers[split[0]])).replace(split[2],str(registers[split[2]]))
                registers[monkey] = eval(statement)
        to_process = {k: v for k, v in to_process.items() if k not in to_remove}
        to_remove.clear()
    print(f"Sim completed in time t={time}")
    return registers

def get_human_number(in_monkeys):
    monkeys = in_monkeys.copy()
    l_value = monkeys['root'].split(" ")[0]
    r_value = monkeys['root'].split(" ")[2]
    # solve l_value
    while True:
        sub_made = False
        vals = l_value.split(" ")
        for val in vals:
            if len(val) == 4 and val.isalpha() and val != "humn":
                l_value = l_value.replace(val, "( "+monkeys[val]+" )")
                sub_made = True
        if not sub_made:
            break

    # solve r_value
    while True:
        sub_made = False
        vals = r_value.split(" ")
        for val in vals:
            if len(val) == 4 and val.isalpha() and val != "humn":
                r_value = r_value.replace(val, "( "+monkeys[val]+" )")
                sub_made = True
        if not sub_made:
            break
    
    # solve for humn
    l_expr = sympify(l_value)
    r_expr = sympify(r_value)
    humn = Symbol('humn')
    equation = Eq(l_expr, r_expr)
    return solve(equation)

# driver
monkeys = load_monkeys()
registers = sim_monkeys(monkeys)
print(f"Part 1 answer: {int(registers['root'])}")

result = get_human_number(monkeys)
print(f"Part 2 answer: {result[0]}")