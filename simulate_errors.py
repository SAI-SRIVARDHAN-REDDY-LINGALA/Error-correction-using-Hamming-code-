# simulate_errors.py
# Flip bits in a given Hamming code to simulate errors

def flip_bits(code, positions):
    """
    Flip bits at given positions (1-based indexing).
    Positions out of range or repeated will be ignored safely.
    """
    code_list = list(code)
    length = len(code_list)

    for pos in positions:
        if 1 <= pos <= length:
            code_list[pos - 1] = '1' if code_list[pos - 1] == '0' else '0'
        else:
            print(f"Warning: position {pos} is out of range and will be ignored.")

    return ''.join(code_list)


def main():
    code = input("Enter the 15-bit Hamming code: ").strip()
    if len(code) != 15 or any(bit not in '01' for bit in code):
        print("Invalid input! Please enter exactly 15 bits of 0 or 1.")
        return

    positions_str = input("Enter bit positions to flip (comma-separated, e.g. 3,7): ").strip()
    try:
        positions = [int(pos) for pos in positions_str.split(',') if pos]
    except ValueError:
        print("Invalid positions! Please enter integers separated by commas.")
        return

    corrupted_code = flip_bits(code, positions)
    print(f"Code after flipping bits at positions {positions}:")
    print(corrupted_code)


if __name__ == "__main__":
    main()
