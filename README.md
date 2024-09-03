# ForceFuse
 The SSH and FTP brute forcing suite 
# 🛠️ SSH & FTP Brute Force Tool
[![Python 3.6](https://img.shields.io/badge/python-3.6-blue.svg)](https://www.python.org/downloads/release/python-360/)
## 📜 Table of Contents

- [Introduction](#introduction)
- [Features](#features)
- [Installation](#installation)
- [Usage](#usage)
- [Example Commands](#example-commands)
- [Disclaimer](#disclaimer)
- [Technologies Used](#technologies-used)

## ✨ Features

- **Brute Force SSH Logins**: Test multiple passwords against an SSH service.
- **Brute Force FTP Logins**: Check FTP credentials using a wordlist.
- **Anonymous FTP Login Check**: Quickly check if a server allows anonymous FTP access.
- **Customizable Wordlists**: Use your own wordlists to test credentials.

## 🚀 Installation

To get started with this tool, follow these steps:

1. **Clone the Repository**:
    ```bash
    git clone https://github.com/sensehat/ForceFuse.git
    cd Project
    chmod +x main.py
    ./main.py
    ```

2. **Install the Required Python Packages**:
    Make sure you have Python installed. Then, install the necessary dependencies using pip:
    ```bash
    pip install paramiko
    ```

3. **You’re Ready to Go!**

## 🕹️ Usage

This tool has been split into two main scripts: `main.py` and `ssh.py`. Here’s how you can use them:

### **Running the Tool**

1. **Run the Main Script**:
    ```bash
    python3 main.py
    ```

2. **Follow the On-Screen Instructions**:
   - **Option 1: Crack SSH**: Provide the target IP, username, and path to your wordlist.
   - **Option 2: Crack FTP**: (Implement your FTP brute-force logic or use existing FTP functionality.)

### **Example Commands**

**Running an SSH brute force attack**:
```bash
python3 main.py
```
### ⚠️ Disclaimer

This tool is intended only for educational purposes and should be used responsibly. Unauthorized use of this tool to gain access to systems without permission is illegal and unethical. Always ensure you have explicit permission before testing any system. The developers of this tool are not responsible for any misuse or damage caused by this tool.
