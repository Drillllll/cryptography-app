import tkinter as tk
from tkinter import Tk, Button, filedialog, Toplevel
from encrypting_manager import EncryptingManager
import os
from tkinter import messagebox

class Window:
    def __init__(self):
        self.encrypting_manager = EncryptingManager()
        self.start()

    def start(self):
        self.root = Tk()
        self.root.geometry("400x200")
        button_certificate_generation = Button(self.root, text="Generate new certificate", command=self.open_generate_certificate_window)
        button_certificate_generation.pack()
        button_read_certificate = Button(self.root, text="Read certificate", command=self.read_certificate)
        button_read_certificate.pack()
        button_encrypt = Button(self.root, text="Encrypt file", command=self.encrypt)
        button_encrypt.pack()
        button_decrypt = Button(self.root, text="Decrypt file", command=self.decrypt)
        button_decrypt.pack()
        self.root.mainloop()

    def open_generate_certificate_window(self):
        # Tworzenie nowego okna
        file_window = Toplevel(self.root)
        file_window.geometry("400x200")

        # Dodawanie przycisków w nowym oknie
        button_choose_folder = Button(file_window, text="Generate", command=self.generate_certificate)
        button_choose_folder.pack()

    def select_file(self):
        filepath = filedialog.askopenfilename()
        print("Wybrano plik:", filepath)
        # Tutaj można dodać kod do obsługi wybranego pliku

    def generate_certificate(self):
        # folder_path = filedialog.askdirectory()
        folder_path = self.create_folder("Test")
        self.encrypting_manager.generate_keys('public_key.pem', 'private_key.pem')
        self.encrypting_manager.generate_certificate('public_key.pem', 'private_key.pem', 'certificate.pem')
        # Tutaj można dodać kod do obsługi wybranego folderu

    def create_folder(self, folder_name):
        project_path = os.getcwd()  # Pobranie ścieżki bieżącego katalogu projektu
        folder_path = os.path.join(project_path, folder_name)  # Tworzenie ścieżki do nowego folderu

        if not os.path.exists(folder_path):  # Sprawdzenie, czy folder nie istnieje
            os.makedirs(folder_path)  # Tworzenie nowego folderu

        return folder_path  # Zwracanie ścieżki nowego folderu

    def create_file(self, folder_path, file_name):
        file_path = os.path.join(folder_path, file_name)

        with open(file_path, "w") as file:
            pass  # Brak zawartości do zapisania

        return file_path

    def read_certificate(self):
        txt = self.encrypting_manager.read_certificate('certificate.pem')
        new_window = Toplevel(self.root)
        new_window.geometry("400x200")
        label = tk.Label(new_window, text=txt)
        label.pack()

    def encrypt(self):
        self.encrypting_manager.encrypt_with_hybrid("input.txt", "public_key.pem", "encrypted.bin")

    def decrypt(self):
        self.encrypting_manager.decrypt_with_hybrid("encrypted.bin", "private_key.pem", "decrypted.txt")