# 🖼️ Simple Image Encryption Tool (Pixel Manipulation)

A beginner-friendly Python project that performs **image encryption and decryption** using **pixel manipulation techniques**. The tool supports **pixel swapping** and **mathematical pixel transformation** to demonstrate basic image security concepts.

---

## 📌 Project Overview

This project implements a simple image encryption mechanism using Python and the Pillow (PIL) library. The encryption is performed by modifying pixel values of an image and can be reversed using the correct method and key.

The tool is designed for **educational purposes** to help understand how images store pixel data and how encryption can be applied at the pixel level.

---

## ✨ Features

- 🔐 Encrypt images using pixel manipulation 
- 🔓 Decrypt images using the same key/method  
- 🧩 Supports two encryption techniques:
  - 🔄 Pixel Swapping 
  - ➕ Mathematical Operation on Pixels  
- 🖼️ Supports RGB and RGBA Images
- 💻 Simple console-based interface  
- 📚 Beginner Friendly & Easy to Understand  

---

## 🛠️ Technologies Used

- Python  
- Pillow (PIL Library)  

---

## 📂 Project Structure

```
Image-Encryption-Tool/
│
├── main.py
├── input.png
├── encrypted.png
├── decrypted.png
└── README.md
```

---

## ⚙️ Installation

### 1️⃣ Clone the Repository

```bash
git clone https://github.com/your-username/image-encryption-tool.git
cd image-encryption-tool
```

### 2️⃣ Install Required Library

```bash
pip install pillow
```

---

## ▶️ How to Run

### Step 1: Place Image in Folder

For encryption:
```
Rename image to → input.png
```

For decryption:
```
Rename image to → encrypted.png
```

---

### Step 2: Run the Program

```bash
python main.py
```

---

### Step 3: Choose Operation

```
1 → Encrypt Image  
2 → Decrypt Image  
```

---

### Step 4: Select Encryption Method

```
1 → Pixel Swapping  
2 → Mathematical Operation  
```

---

### Step 5: Output Files

```
Encrypted Image → encrypted.png  
Decrypted Image → decrypted.png  
```

---

## 🔍 Encryption Techniques Explained

### 🔹 1. Pixel Swapping

- Swaps pixels from left to right across the image  
- Creates a mirrored and scrambled image  
- Fully reversible using the same method  

---

### 🔹 2. Mathematical Pixel Operation

- Adds or subtracts a key value to each pixel  
- Uses modulo operation to keep pixel values in valid range (0–255)

Example:

```
New Pixel = (Old Pixel + Key) % 256
```

For decryption:

```
Original Pixel = (Encrypted Pixel - Key) % 256
```

---

## 🧠 How It Works

Images are made up of pixels. Each pixel contains color values:

- RGB → Red, Green, Blue  
- RGBA → Red, Green, Blue, Alpha (Transparency)

The program modifies these pixel values to encrypt the image and reverses them during decryption.

---

## ⚠️ Limitations

- Basic encryption only (not production-grade security)  
- Metadata may not be preserved  
- Requires correct key for decryption  
- Intended for learning purposes  

---

## 🚀 Future Improvements

- GUI Interface  
- Password-Based Encryption  
- Support for More Image Formats  
- Stronger Cryptographic Techniques  
- Drag-and-Drop Image Upload  

---

## 📸 Example Workflow

```
input.png → Encryption → encrypted.png  
encrypted.png → Decryption → decrypted.png  
```

---

## 🎓 Learning Outcomes

- Understanding image pixel structure  
- Basics of encryption & decryption  
- Image processing using Python  
- Working with files and binary data  

---

## 🤝 Contribution

Contributions are welcome. Fork the repository and submit a pull request.

---

## 📜 License

This project is open-source and intended for educational use only.

---

## 👨‍💻 Author

**Anish Kumar**  
B.Tech CSE (Cyber Security)
