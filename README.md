# 🎮 Genesis / Mega Drive Game Genie Tools

A simple Python CLI tool to **encode and decode Sega Mega Drive / Genesis Game Genie codes**.

Perfect for:
- ROM hacking
- Reverse engineering game logic
- Verifying existing Game Genie codes

---

## ✨ Features

- 🔁 Encode ROM address + value → Game Genie code  
- 🔍 Decode Game Genie code → address + value  
- 💻 Simple CLI interface  
- ⚡ Fast and dependency-free  

## 🚀 Usage

### Encode

Convert a ROM address and value into a Game Genie code:

```bash
python convert_gg.py -e 0015D1C 0004
```

**Output:**

```text
AVRT-CAA6
```

---

### Decode

Convert a Game Genie code back into address and value:

```bash
python convert_gg.py -d AVRT-CAA6
```

**Output:**

```text
Address: 0015D1C
Value:   0004
```

---

## 🧠 How it Works

The Sega Genesis Game Genie uses:

- A custom **32-character alphabet**
- 5-bit encoding per character
- A **bit-scrambling algorithm** to hide address and value

This tool implements the full encoding/decoding process based on known reverse-engineered methods.

---

## 🎯 Example Use Case

```text
Sonic Delta Origins v0.79
CRC 2F8DAAD7
No death: AVRT-CAA6
99 rings on hit: NNCA-EAER
```

---

## ⚠️ Notes

- Addresses must be **ROM (not RAM)**  
- Values are **16-bit (word-sized)**  

---

## 🛠️ Roadmap (Ideas)

- Batch conversion support  
- ROM file patching integration  
- GUI frontend  
- Cheat database support  

---

## 🤝 Contributing

Pull requests welcome!  
Feel free to submit improvements or additional features.
