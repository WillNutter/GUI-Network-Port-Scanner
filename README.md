# 🔍 Python Port Scanner (GUI)

A lightweight and portable **port scanner** built using **pure Python** with a **Tkinter GUI**.  
No external packages required — runs natively on any Linux system with Python 3 installed.

## 🧰 Features
- Scan any IP or hostname for open TCP ports
- Define start and end port range
- Displays open and closed ports
- GUI built with `tkinter` (standard library)
- Multithreaded scanning (non-blocking GUI)

## 🚀 Usage

### ▶️ Run the scanner:
```bash
python3 port_scanner_gui.py
```

### 🖥️ GUI Interface:
1. Enter the **IP address or domain name**
2. Choose a **start port** and **end port**
3. Click **"Scan"**
4. View results in the scrollable output window

## 📦 Requirements
- Python 3.x
- Linux (tested on Ubuntu/Debian/Fedora)
- No external dependencies!

## 📁 File Structure
| File | Purpose |
|------|---------|
| `port_scanner_gui.py` | Main script with GUI |
| `.gitignore` | Ignore system/cache files |
| `LICENSE` | MIT license |
| `README.md` | Project documentation |

## 📄 License
This project is licensed under the [MIT License](LICENSE).
