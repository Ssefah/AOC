def read_instructions(filename):
    """
    Read the contents of a file.

    Parameters:
        filename (str): The name of the file to read.

    Returns:
        str: The contents of the file.
    """
    with open(filename, "r") as file:
        return file.read()
    
def calculate_santa_floor(instructions):
    """
    Calculate Santa's floor based on a string of instructions.

    Args:
        instructions (str): A string of instructions containing parentheses.

    Returns:
        int: The floor Santa is on after following the instructions.

    Raises:
        ValueError: If an invalid instruction is encountered.

    Example:
        >>> calculate_santa_floor("(((())))")
        4

    Note:
        - The instructions string may contain opening and closing parentheses.
        - Opening parentheses increase the floor by 1.
        - Closing parentheses decrease the floor by 1.
        - An invalid instruction raises a ValueError.
    """
    floor = 0
    for instruction in instructions:
        if instruction == "(":
            floor += 1
        elif instruction == ")":
            floor -= 1
        else:
            raise ValueError("Invalid instruction: " + instruction)
    return floor
    

def find_basement(instructions):
    floor = 0
    position = 0
    for i, char in enumerate(instructions, 1):
        if char == "(":
            floor += 1
        elif char == ")":
            floor -=1
            if floor == -1:
                return i
        position += 1
    raise ValueError("Basement not reached if the given instructions!")

    


instructions = read_instructions("instructions.txt")
final_floor = calculate_santa_floor(instructions)

position = find_basement(instructions)
print(f"Final floor: {final_floor}")
print(f"Santa first reaches the basement at postion: {position}")