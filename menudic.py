import tkinter as tk
from tkinter import messagebox
from cryptography.fernet import Fernet

# Create the main window
window = tk.Tk()
window.title("Data Encryption/Decryption Tool")

# Generate a key for encryption/decryption
key = Fernet.generate_key()
cipher_suite = Fernet(key)

# Function to encrypt the entered data
def encrypt():
    plaintext = input_text.get("1.0", "end-1c")  # Get the input text
    if plaintext:
        try:
            encrypted_text = cipher_suite.encrypt(plaintext.encode())  # Encrypt the text
            output_text.delete("1.0", "end")  # Clear the output text
            output_text.insert("1.0", encrypted_text.decode())  # Display the encrypted text
        except Exception as e:
            messagebox.showerror("Error", str(e))
    else:
        messagebox.showwarning("Warning", "Please enter some text.")

# Function to decrypt the entered data
def decrypt():
    encrypted_text = input_text.get("1.0", "end-1c")  # Get the input text
    if encrypted_text:
        try:
            decrypted_text = cipher_suite.decrypt(encrypted_text.encode())  # Decrypt the text
            output_text.delete("1.0", "end")  # Clear the output text
            output_text.insert("1.0", decrypted_text.decode())  # Display the decrypted text
        except Exception as e:
            messagebox.showerror("Error", str(e))
    else:
        messagebox.showwarning("Warning", "Please enter some text.")

# Create the input text box
input_text = tk.Text(window, height=10, width=50)
input_text.pack(pady=10)

# Create the encryption button
encrypt_button = tk.Button(window, text="Encrypt", command=encrypt)
encrypt_button.pack(pady=5)

# Create the decryption button
decrypt_button = tk.Button(window, text="Decrypt", command=decrypt)
decrypt_button.pack(pady=5)

# Create the output text box
output_text = tk.Text(window, height=10, width=50)
output_text.pack(pady=10)

# Run the main loop
window.mainloop()
