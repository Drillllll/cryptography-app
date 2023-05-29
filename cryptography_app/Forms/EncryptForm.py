from tkinter import Tk, Button, Label, Entry, filedialog
import os
from tkinter import messagebox


class EncryptForm:
    def __init__(self, encrypting_manager):
        self.encrypting_manager = encrypting_manager
        self.root = Tk()
        self.root.title("Encrypt Form")

        # Etykiety
        Label(self.root, text="Input File:").grid(row=0, column=0)
        Label(self.root, text="Receiver Certificate File:").grid(row=1, column=0)
        Label(self.root, text="Output File Name:").grid(row=2, column=0)
        Label(self.root, text="Output Folder:").grid(row=3, column=0)

        # Entry
        self.input_file_entry = Entry(self.root, width=30)
        self.input_file_entry.grid(row=0, column=1)
        self.receiver_certificate_file_entry = Entry(self.root, width=30)
        self.receiver_certificate_file_entry.grid(row=1, column=1)
        self.output_file_entry = Entry(self.root, width=30)
        self.output_file_entry.grid(row=2, column=1)
        self.output_file_entry.insert(0, "Encrypted.bin")
        self.output_folder_entry = Entry(self.root, width=30)
        self.output_folder_entry.grid(row=3, column=1)

        # Przyciski
        input_file_button = Button(self.root, text="Browse", command=self.choose_input_file)
        input_file_button.grid(row=0, column=2)
        receiver_certificate_button = Button(self.root, text="Browse", command=self.choose_receiver_certificate)
        receiver_certificate_button.grid(row=1, column=2)
        output_folder_button = Button(self.root, text="Browse", command=self.choose_output_folder)
        output_folder_button.grid(row=3, column=2)
        encrypt_button = Button(self.root, text="Encrypt", command=self.encrypt)
        encrypt_button.grid(row=5, column=0, columnspan=3)



    def choose_output_folder(self):
        folder_path = filedialog.askdirectory()
        self.output_folder_entry.delete(0, 'end')
        self.output_folder_entry.insert(0, folder_path)

    def choose_input_file(self):
        file_path = filedialog.askopenfilename()
        self.input_file_entry.delete(0, 'end')
        self.input_file_entry.insert(0, file_path)

    def choose_receiver_certificate(self):
        file_path = filedialog.askopenfilename()
        self.receiver_certificate_file_entry.delete(0, 'end')
        self.receiver_certificate_file_entry.insert(0, file_path)

    def encrypt(self):
        input_file = self.input_file_entry.get()
        receiver_certificate_file = self.receiver_certificate_file_entry.get()
        output_file = self.output_file_entry.get()
        output_folder = self.output_folder_entry.get()
        output_path = os.path.join(output_folder, output_file)

        # Wywołanie funkcji encrypt_with_hybrid z przekazanymi wartościami
        self.encrypting_manager.encrypt_with_hybrid(input_file, receiver_certificate_file, output_path)
        messagebox.showinfo("OK", "OK")
        self.root.destroy()

    def open_form(self):
        self.root.mainloop()

