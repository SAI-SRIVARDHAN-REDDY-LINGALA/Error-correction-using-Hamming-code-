
# 🧠 Hamming Code: Error Detection & Correction

## 📌 Introduction
In digital systems, data can get corrupted during transmission due to noise, interference, or hardware faults.  
To ensure reliable communication, we use **error detection and correction codes**.

**Hamming Code** is a simple and effective method that:
- ✅ Detects and **corrects single-bit errors**
- ⚠️ Detects (but does **not** correct) **double-bit errors**

---

## 📌 Goal
Encode 11-bit data into a longer bit stream using **Hamming (15,11) code**, such that:
- ✅ Single-bit errors can be detected and corrected
- ✅ Double-bit errors can be detected (but not corrected)

---

## 📌 Hamming (15,11) Code
- ➡️ **11 data bits**
- ➕ **4 parity bits**
- 📏 **Total: 15 bits**

### 📍 Parity Bit Positions
Parity bits are placed at **positions that are powers of 2**:

| Bit Position | Type   |
|--------------|--------|
| 1            | P1     |
| 2            | P2     |
| 3            | D1     |
| 4            | P4     |
| 5            | D2     |
| 6            | D3     |
| 7            | D4     |
| 8            | P8     |
| 9            | D5     |
| 10           | D6     |
| 11           | D7     |
| 12           | D8     |
| 13           | D9     |
| 14           | D10    |
| 15           | D11    |

---

## 📌 Parity Bit Calculation

Each **parity bit** checks specific positions based on **binary representation** of the index:

| Parity Bit | Checks Positions (1-based)                                                                 |
|------------|---------------------------------------------------------------------------------------------|
| P1 (1)     | 1, 3, 5, 7, 9, 11, 13, 15  → (binary: xxxx1)                                                |
| P2 (2)     | 2, 3, 6, 7, 10, 11, 14, 15 → (binary: xxx1x)                                                |
| P4 (4)     | 4–7, 12–15               → (binary: xx1xx)                                                  |
| P8 (8)     | 8–15                      → (binary: x1xxx)                                                 |

- Each parity bit is set to ensure **even parity** (even number of 1s in its group).

---

## 📌 Error Detection & Correction

### How it works:
1. **Receiver recalculates parity bits** from the received 15-bit code.
2. Compares with the received parity bits.
3. If there’s a mismatch → Constructs a **syndrome** (4-bit binary value).
4. The **syndrome** gives the position of the **error bit** (if any).

### 🔍 Syndrome Cases:
- `0000` → ✅ No error
- Non-zero syndrome → ❌ Error at the position = syndrome value  
  (e.g., syndrome = `0101` = 5 → Error at bit position 5)

### ✅ Example:
```

Received Code:     101001101101011
Calculated Syndrome: 5
→ Flip 5th bit
Corrected Code:    101011101101011

```

---

## 📌 Double-Bit Error Detection
- If **2 bits** flip, the calculated syndrome will be incorrect.
- Hamming Code can **detect** that something's wrong.
- ❌ Cannot identify and correct the 2 bits.

---

## 📌 (Optional) Hamming (16,11) - SECDED

Add one extra parity bit for:
- ✅ Single Error Correction
- ✅ Double Error Detection

### 🔹 Structure:
- 11 data bits  
- 4 Hamming parity bits  
- 1 overall parity bit (P0)  
- 🔄 Total = 16 bits

This is called **SECDED**:
> Single Error Correction, Double Error Detection

---

## 📌 Advantages
- ✔️ Simple to implement
- ✔️ Fast single-bit error correction
- ✔️ Used in hardware and communication systems

---

## 📌 Limitations
- ❌ Only corrects 1-bit errors
- ❌ Detects but doesn't correct 2-bit errors
- ❌ Doesn't handle burst errors (more than 2 bits)

---

## 📌 Applications
- 💾 ECC RAM (Error-Correcting Code Memory)
- 🌐 Network data transmission
- 🛰️ Satellite & space communication
- 💿 CD/DVD error correction systems

---

## ✨ Summary

| Feature                     | Hamming (15,11)        | Hamming (16,11) (SECDED)   |
|----------------------------|------------------------|----------------------------|
| Data bits                  | 11                     | 11                         |
| Parity bits                | 4                      | 5 (4 + 1 overall)          |
| Detects single-bit errors  | ✅ Yes                 | ✅ Yes                     |
| Corrects single-bit errors | ✅ Yes                 | ✅ Yes                     |
| Detects double-bit errors  | ⚠️ Yes (not correct)   | ✅ Yes                     |
| Corrects double-bit errors | ❌ No                  | ❌ No                      |

---

## ✍️ Author

**Sai Srivardhan Lingala**  
🎓 Passionate about tech, learning, and building error-free systems!  

---

✨ *Happy Learning & Debugging!* 🚀  
```

---


