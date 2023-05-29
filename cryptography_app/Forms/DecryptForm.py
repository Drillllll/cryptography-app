from tkinter import Tk, Button, Label, Entry, filedialog
import os
from tkinter import messagebox

class DecryptForm:
    def __init__(self, encrypting_manager):
        self.encrypting_manager = encrypting_manager
        self.root = Tk()
        self.root.title("Decrypt Form")

        # Etykiety
        Label(self.root, text="Input File:").grid(row=0, column=0)
        Label(self.root, text="Private Key File:").grid(row=1, column=0)
        Label(self.root, text="Output File Name:").grid(row=2, column=0)
        Label(self.root, text="Output Folder:").grid(row=3, column=0)

        # Entry
        self.input_file_entry = Entry(self.root, width=30)
        self.input_file_entry.grid(row=0, column=1)
        self.private_key_file_entry = Entry(self.root, width=30)
        self.private_key_file_entry.grid(row=1, column=1)
        self.output_file_entry = Entry(self.root, width=30)
        self.output_file_entry.grid(row=2, column=1)
        self.output_file_entry.insert(0, "Decrypted.txt")
        self.output_folder_entry = Entry(self.root, width=30)
        self.output_folder_entry.grid(row=3, column=1)

        # Przyciski
        input_file_button = Button(self.root, text="Browse", command=self.choose_input_file)
        input_file_button.grid(row=0, column=2)
        private_key_button = Button(self.root, text="Browse", command=self.choose_private_key)
        private_key_button.grid(row=1, column=2)
        output_folder_button = Button(self.root, text="Browse", command=self.choose_output_folder)
        output_folder_button.grid(row=3, column=2)
        dencrypt_button = Button(self.root, text="Dencrypt", command=self.dencrypt)
        dencrypt_button.grid(row=5, column=0, columnspan=3)

    def choose_output_folder(self):
        folder_path = filedialog.askdirectory()
        self.output_folder_entry.delete(0, 'end')
        self.output_folder_entry.insert(0, folder_path)

    def choose_input_file(self):
        file_path = filedialog.askopenfilename()
        self.input_file_entry.delete(0, 'end')
        self.input_file_entry.insert(0, file_path)

    def choose_private_key(self):
        file_path = filedialog.askopenfilename()
        self.private_key_file_entry.delete(0, 'end')
        self.private_key_file_entry.insert(0, file_path)

    def dencrypt(self):
        input_file = self.input_file_entry.get()
        private_key_file = self.private_key_file_entry.get()
        output_file = self.output_file_entry.get()
        output_folder = self.output_folder_entry.get()
        output_path = os.path.join(output_folder, output_file)

        # Wywołanie funkcji encrypt_with_hybrid z przekazanymi wartościami
        result = self.encrypting_manager.decrypt_with_hybrid(input_file, private_key_file, output_path)
        if result is True:
            messagebox.showinfo("OK", "OK")
        else:
            messagebox.showinfo("NO GOOD", "VERY BAD")
        self.root.destroy()

    def open_form(self):
        self.root.mainloop()

