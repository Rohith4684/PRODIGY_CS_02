from PIL import Image
def encrypt_image(image_path, key):
    # Open the image
    img = Image.open(image_path)
    width, height = img.size

    # Convert the image to RGB mode
    img_rgb = img.convert("RGB")

    # Create a new image for encryption
    encrypted_img = Image.new("RGB", (width, height))

    for x in range(width):
        for y in range(height):
            r, g, b = img_rgb.getpixel((x, y))
            # Perform encryption operation (for example, bitwise XOR)
            r_encrypted = r ^ key
            g_encrypted = g ^ key
            b_encrypted = b ^ key
            # Set the encrypted pixel value in the new image
            encrypted_img.putpixel((x, y), (r_encrypted, g_encrypted, b_encrypted))

    # Save the encrypted image
    encrypted_img.save("encrypted_image.png")
    print("Image encrypted successfully!")


def decrypt_image(image_path, key):
    # Open the encrypted image
    encrypted_img = Image.open(image_path)
    width, height = encrypted_img.size

    # Create a new image for decryption
    decrypted_img = Image.new("RGB", (width, height))

    for x in range(width):
        for y in range(height):
            r, g, b = encrypted_img.getpixel((x, y))
            # Perform decryption operation (in this case, the same operation as encryption)
            r_decrypted = r ^ key
            g_decrypted = g ^ key
            b_decrypted = b ^ key
            # Set the decrypted pixel value in the new image
            decrypted_img.putpixel((x, y), (r_decrypted, g_decrypted, b_decrypted))

    # Save the decrypted image
    decrypted_img.save("decrypted_image.png")
    print("Image decrypted successfully!")


# Example usage:
# Encrypt image
encrypt_image("input_image.png", 128)

# Decrypt image
decrypt_image("encrypted_image.png", 128)
