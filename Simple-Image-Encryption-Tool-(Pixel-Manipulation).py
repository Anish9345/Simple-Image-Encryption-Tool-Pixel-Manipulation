from PIL import Image

print("===== Image Encryption Tool =====")
print("\n[INFO]")
print("• For encryption → place image as 'input.png' in this folder")
print("• For decryption → place image as 'encrypted.png' in this folder\n")

print("1. Encrypt Image")
print("2. Decrypt Image")

main_choice = int(input("Enter your choice (1 or 2): "))

# =========================
# LOAD IMAGE
# =========================
if main_choice == 1:
    img = Image.open("input.png")

elif main_choice == 2:
    img = Image.open("encrypted.png")

else:
    print("Invalid choice")
    exit()

pixels = img.load()
width, height = img.size
mode = img.mode

print("\nChoose Method:")
print("1. Pixel Swapping")
print("2. Mathematical Operation on Pixels")

method = int(input("Enter method (1 or 2): "))

# =========================
# PIXEL SWAPPING
# =========================
if method == 1:
    for y in range(height):
        for x in range(width // 2):
            left = pixels[x, y]
            right = pixels[width - x - 1, y]

            pixels[x, y] = right
            pixels[width - x - 1, y] = left

    if main_choice == 1:
        img.save("encrypted.png")
        print("Image encrypted using pixel swapping.")
    else:
        img.save("decrypted.png")
        print("Image decrypted using pixel swapping.")

# =========================
# MATHEMATICAL OPERATION
# =========================
elif method == 2:
    key = int(input("Enter key (same key required for decryption): "))

    if main_choice == 2:
        key = -key

    for y in range(height):
        for x in range(width):

            if mode == "RGBA":
                r, g, b, a = pixels[x, y]
                r = (r + key) % 256
                g = (g + key) % 256
                b = (b + key) % 256
                pixels[x, y] = (r, g, b, a)

            else:
                r, g, b = pixels[x, y]
                r = (r + key) % 256
                g = (g + key) % 256
                b = (b + key) % 256
                pixels[x, y] = (r, g, b)

    if main_choice == 1:
        img.save("encrypted.png")
        print("Image encrypted using mathematical operation.")
    else:
        img.save("decrypted.png")
        print("Image decrypted using mathematical operation.")

else:
    print("Invalid method selected.")
