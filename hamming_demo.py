import random
from functools import reduce
import operator
from colorama import Fore, Style, init

# Initialize colorama for colored output in terminal
init(autoreset=True)

# -------------------------------
# Utility Functions
# -------------------------------

def xor_all(indices):
    """
    XOR all the values in a list.
    Used to calculate the syndrome in Hamming Code error detection.
    """
    return reduce(operator.xor, indices, 0)

def pretty_print_bits(label, bits, error_pos=None):
    """
    Print a label and bit array.
    If an error position is specified, highlight that bit in red.
    """
    output = f"{label:<30}: "
    for i, bit in enumerate(bits):
        if error_pos is not None and i == error_pos:
            # Highlight the erroneous bit
            output += Fore.RED + Style.BRIGHT + str(bit) + Style.RESET_ALL + " "
        else:
            output += str(bit) + " "
    print(output.strip())

# -------------------------------
# Hamming Code Core Functions
# -------------------------------

def encode_hamming(data_bits):
    """
    Encode an 11-bit data sequence into a 15-bit Hamming(15,11) block.
    Inserts parity bits at positions 1, 2, 4, and 8 (0-based: 0,1,3,7).
    """
    codeword = [0] * 15  # Final encoded message
    parity_positions = [0, 1, 3, 7]  # Positions for parity bits (1-based: 1,2,4,8)

    data_index = 0
    for i in range(15):
        if i not in parity_positions:
            codeword[i] = data_bits[data_index]
            data_index += 1

    # Calculate parity bits
    for p in parity_positions:
        parity = 0
        for i in range(15):
            if codeword[i] == 1 and ((i + 1) & (p + 1)):
                parity ^= 1
        codeword[p] = parity

    return codeword

def introduce_error(codeword):
    """
    Flip one random bit in the codeword to simulate a transmission error.
    """
    error_index = random.randint(0, 14)
    codeword[error_index] ^= 1  # Flip the bit
    return codeword, error_index

def detect_error(received_bits):
    """
    Detect a single-bit error using syndrome calculation (XOR of all 1-bit positions).
    Returns 1-based error position (0 if no error).
    """
    indices_with_ones = [i + 1 for i, bit in enumerate(received_bits) if bit == 1]
    error_position = xor_all(indices_with_ones)
    return error_position

def correct_error(bits, error_pos):
    """
    Flip the bit at the detected error position (1-based index).
    Returns corrected bit array.
    """
    if error_pos == 0:
        return bits  # No error to correct
    bits[error_pos - 1] ^= 1
    return bits

# -------------------------------
# Demo Driver
# -------------------------------

def run_hamming_demo():
    print(Fore.CYAN + "\n🧪 Hamming Code (15,11) Error Detection & Correction Demo\n")

    # 1. Generate 11-bit random data
    data_bits = [random.randint(0, 1) for _ in range(11)]
    pretty_print_bits("Original 11-bit Data", data_bits)

    # 2. Encode data using Hamming Code
    encoded_codeword = encode_hamming(data_bits)
    pretty_print_bits("Encoded Hamming(15,11)", encoded_codeword)

    # 3. Introduce single-bit error in transmission
    received_codeword, error_index = introduce_error(encoded_codeword.copy())
    pretty_print_bits("Received (with error)", received_codeword, error_pos=error_index)
    print(Fore.YELLOW + f"⚠️  Error introduced at bit index (0-based): {error_index}")

    # 4. Detect error position
    detected_error_pos = detect_error(received_codeword)
    if detected_error_pos == 0:
        print(Fore.GREEN + "✅ No error detected.")
    else:
        print(Fore.RED + f"🔍 Error detected at bit position: {detected_error_pos} (1-based)")

    # 5. Correct the error
    corrected_codeword = correct_error(received_codeword.copy(), detected_error_pos)
    pretty_print_bits("Corrected Codeword", corrected_codeword)

    # 6. Validate correction
    if corrected_codeword == encoded_codeword:
        print(Fore.GREEN + "🎉 Error successfully corrected!")
    else:
        print(Fore.RED + "❌ Correction failed. Possibly a double-bit error.")

# -------------------------------
# Main Entry Point
# -------------------------------

if __name__ == "__main__":
    while True:
        run_hamming_demo()
        user_choice = input(Fore.CYAN + "\n🔁 Run another demo? (y/n): ").strip().lower()
        if user_choice != 'y':
            print(Fore.BLUE + "👋 Exiting Hamming Code Simulator. Goodbye!")
            break
