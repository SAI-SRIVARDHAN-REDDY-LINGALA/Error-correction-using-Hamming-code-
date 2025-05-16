# hamming_decode.py
# Detect and correct errors in received 15-bit Hamming code

def calculate_syndrome(code):
    """Calculate the 4-bit syndrome from the received code."""
    code_bits = [int(bit) for bit in code]
    # Add a 0 at front to make 1-based indexing easier
    code_bits = [0] + code_bits

    syndrome = 0
    for i, parity_pos in enumerate([1, 2, 4, 8], start=0):
        parity = 0
        for j in range(1, 16):
            if j & parity_pos:
                parity ^= code_bits[j]
        syndrome |= (parity << i)
    return syndrome


def correct_error(code, syndrome):
    """Correct single-bit error if syndrome != 0."""
    if syndrome == 0:
        return code, False  # No error
    elif 1 <= syndrome <= 15:
        # Flip the bit at syndrome position
        code_list = list(code)
        idx = syndrome - 1
        code_list[idx] = '1' if code_list[idx] == '0' else '0'
        corrected_code = ''.join(code_list)
        return corrected_code, True
    else:
        # Syndrome outside valid range (shouldn't happen in Hamming 15)
        return code, False


def extract_data(code):
    """Extract the original 11 data bits from the 15-bit code."""
    # Data bits are all bits except parity bits at 1,2,4,8
    data_bits = []
    for i in range(1, 16):
        if i not in [1, 2, 4, 8]:
            data_bits.append(code[i - 1])
    return ''.join(data_bits)


def main():
    received_code = input("Enter received 15-bit Hamming code: ").strip()
    if len(received_code) != 15 or any(bit not in '01' for bit in received_code):
        print("Invalid input! Please enter exactly 15 bits of 0 or 1.")
        return

    syndrome = calculate_syndrome(received_code)

    if syndrome == 0:
        print("No errors detected.")
        corrected_code = received_code
    else:
        print(f"Error detected at bit position: {syndrome}")
        corrected_code, corrected = correct_error(received_code, syndrome)
        if corrected:
            print("Single-bit error corrected.")
        else:
            print("Error detected but unable to correct.")

    print(f"Corrected Code: {corrected_code}")
    original_data = extract_data(corrected_code)
    print(f"Original 11-bit data extracted: {original_data}")


if __name__ == "__main__":
    main()
