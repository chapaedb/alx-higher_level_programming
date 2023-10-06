#!/usr/bin/python3
import dis

if __name__ == "__main__":
    with open("hidden_4.pyc", "rb") as file:
        bytecode = file.read()

    names = []
    instructions = dis.get_instructions(bytecode)
    for instruction in instructions:
        if (
            instruction.opname == "LOAD_CONST"
            and isinstance(instruction.argval, str)
            and not instruction.argval.startswith("__")
        ):
            names.append(instruction.argval)

    names.sort()

    for name in names:
        print(name)
