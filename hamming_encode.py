# hamming_encode.py
# Encode 11-bit data into 15-bit Hamming code with parity bits

def calculate_parity_bits(data_bits):
    """Calculate parity bits for given 11-bit data according to Hamming (15,11)."""
    # Positions: 1-based indexing for easier mapping
    # parity bit positions: 1, 2, 4, 8 (powers of two)
    
    # Create a 15-bit array (indexes 1 to 15, index 0 unused)
    encoded = [0] * 16
    j = 0  # index for data bits

    # Place data bits into positions that are NOT powers of two
    for i in range(1, 16):
        if i not in [1, 2, 4, 8]:
            encoded[i] = int(data_bits[j])
            j += 1

    # Calculate parity bits:
    # parity bit covers positions where bitwise AND with parity position is non-zero

    for parity_pos in [1, 2, 4, 8]:
        parity = 0
        for i in range(1, 16):
            if i & parity_pos and i != parity_pos:
                parity ^= encoded[i]
        encoded[parity_pos] = parity

    # Return encoded list as a string (skip index 0)
    return ''.join(str(bit) for bit in encoded[1:])


def main():
    data = input("Enter 11-bit data (e.g. 10110011001): ").strip()
    if len(data) != 11 or any(bit not in '01' for bit in data):
        print("Invalid input! Please enter exactly 11 bits of 0 or 1.")
        return

    encoded_data = calculate_parity_bits(data)
    print(f"Encoded 15-bit Hamming code: {encoded_data}")


if __name__ == "__main__":
    main()
