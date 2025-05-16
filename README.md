
# 🎯 **ERROR CORRECTION CODES** 🎯

*Author: Sai Srivardhan Lingala*
*Project: Hamming Code Implementation*

<br>

## 🗂️ **Project Structure**

```
error_correction_codes/
│
├── hamming_encode.py          # Encoder script for 11-bit to 15/16-bit Hamming code
├── simulate_errors.py         # Script to simulate bit flips/errors
├── hamming_decode.py          # Decoder script to detect & correct errors
├── hamming_demo.py            # Interactive colorful demo combining all steps
├── theory.md                  # In-depth theory explanations
├── README.md                  # This README file
├── requirements.txt           # Python dependencies (e.g. colorama)

```

<br>

## 🛠️ **Setup & Installation**

1. Clone or download this project folder.

2. (Recommended) Create and activate a Python virtual environment:

```bash
python3 -m venv venv
source venv/bin/activate      # Linux/macOS
venv\Scripts\activate         # Windows
```

3. Install required Python packages:

```bash
pip install -r requirements.txt
```

> *Note:* The interactive demo uses the `colorama` package for colorful terminal output.

<br>

## 🚀 **How to Run**

* Run the **interactive demo** (recommended for full experience):

```bash
python hamming_demo.py
```

* Or run individual scripts:

```bash
python hamming_encode.py
python simulate_errors.py
python hamming_decode.py
```

---

## 🔎 **What is This Project?**

This project dives deep into **ERROR DETECTION & CORRECTION** —
one of the most critical pillars of reliable digital communication.

It includes Python scripts to:<br>
➡️ Encode data with Hamming Codes (15,11) & (16,11)<br>
➡️ Simulate errors like single and double bit flips<br>
➡️ Detect and automatically correct those errors<br>

With clear theory and practical code, this is a great toolkit for
students and engineers alike!

<br>

## ⚡ **Why Does Error Correction Matter?**

Digital data is fragile! Bit flips happen because of:
• Voltage spikes<br>
• Scratched disks<br>
• Noisy transmissions<br>

Without error correction, your files, videos, or messages might get corrupted.

Hamming Codes add a small number of extra bits to:<br>
✔️ Detect errors<br>
✔️ Pinpoint the exact bit that flipped<br>
✔️ Fix it automatically<br>

<br>

## 📂 **What's Inside?**

* `hamming_encode.py` → Converts 11-bit data into error-protected code
* `hamming_decode.py` → Detects and fixes errors in received data
* `simulate_errors.py` → Flips bits to mimic transmission errors
* `hamming_demo.py` → Interactive demo showing encoding, error simulation, detection & correction
* `theory.txt` → In-depth explanations of Hamming Code theory

<br>

## ✨ **Key Features**

✔️ Easy-to-understand Python scripts<br>
✔️ Step-by-step explanations with colorful printouts<br>
✔️ Modular design for easy customization<br>
✔️ Ideal for learning ECC fundamentals<br>

<br>

## 🌍 **Applications**

• ECC Memory (RAM)<br>
• Satellite and Space Communications<br>
• Data Storage (CD, DVD, SSD)<br>
• Network Transmission Protocols<br>

<br>

## ⚠️ **Limitations**

❌ Only single-bit errors can be corrected<br>
❌ Double-bit errors are detected but not corrected<br>
❌ Burst errors require more advanced codes (e.g., Reed-Solomon)<br>

<br>

## 📜 **License**

Free to use for learning and educational purposes.
Please give credit when using or sharing.
☺☺☺☺☺☺☺☺

<br>

# ✨ Happy Learning & Coding! ✨

— Sai Srivardhan Lingala

---

