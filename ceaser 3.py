import tkinter as tk

from tkinter import messagebox

def caesar_cipher_encrypt(plaintext, shift):
    encrypted_text = ""
    for char in plaintext:
        if char.isalpha():  # Check if character is a letter
            # Shift character
            shifted = ord(char) + shift
            # Handle wrap-around for uppercase letters
            if char.isupper():
                if shifted > ord('Z'):
                    shifted -= 26
                elif shifted < ord('A'):
                    shifted += 26
            # Handle wrap-around for lowercase letters
            elif char.islower():
                if shifted > ord('z'):
                    shifted -= 26
                elif shifted < ord('a'):
                    shifted += 26
            encrypted_text += chr(shifted)
        else:
            encrypted_text += char  # Append unchanged character (not a letter)
    return encrypted_text

def caesar_cipher_decrypt(ciphertext, shift):
    decrypted_text = ""
    for char in ciphertext:
        if char.isalpha():  # Check if character is a letter
            # Shift character
            shifted = ord(char) - shift
            # Handle wrap-around for uppercase letters
            if char.isupper():
                if shifted < ord('A'):
                    shifted += 26
                elif shifted > ord('Z'):
                    shifted -= 26
            # Handle wrap-around for lowercase letters
            elif char.islower():
                if shifted < ord('a'):
                    shifted += 26
                elif shifted > ord('z'):
                    shifted -= 26
            decrypted_text += chr(shifted)
        else:
            decrypted_text += char  # Append unchanged character (not a letter)
    return decrypted_text

def open_encrypt_window():
    encrypt_window = tk.Toplevel()
    encrypt_window.title("Encryption Result")

    plaintext = plaintext_entry.get()
    shift = int(shift_entry.get())
    encrypted_message = caesar_cipher_encrypt(plaintext, shift)

    result_label = tk.Label(encrypt_window, text="Encrypted Message:")
    result_label.pack(padx=10, pady=5)

    result_text = tk.Text(encrypt_window, height=5, width=50)
    result_text.insert(tk.END, encrypted_message)
    result_text.pack(padx=10, pady=5)

def open_decrypt_window():
    decrypt_window = tk.Toplevel()
    decrypt_window.title("Decryption Result")

    ciphertext = plaintext_entry.get()  # Retrieve ciphertext
    shift = int(shift_entry.get())
    decrypted_message = caesar_cipher_decrypt(ciphertext, shift)

    result_label = tk.Label(decrypt_window, text="Decrypted Message:")
    result_label.pack(padx=10, pady=5)

    result_text = tk.Text(decrypt_window, height=5, width=50)
    result_text.insert(tk.END, decrypted_message)
    result_text.pack(padx=10, pady=5)

# Create main window
window = tk.Tk()
window.title("Caesar Cipher Encryption/Decryption")

# Create widgets
plaintext_label = tk.Label(window, text="Message:")
plaintext_label.grid(row=0, column=0, padx=10, pady=10)

plaintext_entry = tk.Entry(window, width=50)
plaintext_entry.grid(row=0, column=1, columnspan=2, padx=10, pady=5)

shift_label = tk.Label(window, text="Shift Value:")
shift_label.grid(row=1, column=0, padx=10, pady=5)

shift_entry = tk.Entry(window, width=10)
shift_entry.grid(row=1, column=1, padx=10, pady=5)

encrypt_button = tk.Button(window, text="Encrypt", width=15, command=open_encrypt_window)
encrypt_button.grid(row=2, column=1, padx=10, pady=5)

decrypt_button = tk.Button(window, text="Decrypt", width=15, command=open_decrypt_window)
decrypt_button.grid(row=2, column=2, padx=10, pady=5)

# Start the GUI
window.mainloop()
