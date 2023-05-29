import tkinter as tk
from tkinter import Tk, Button, filedialog, Toplevel
from encrypting_manager import EncryptingManager

from Forms.EncryptForm import *
from Forms.DecryptForm import *
from Forms.GeneratorForm import *

class Window:
    def __init__(self):
        self.encrypting_manager = EncryptingManager()
        self.start()

    def start(self):
        self.root = Tk()
        self.root.geometry("400x200")
        button_certificate_generation = Button(self.root, text="Generate new certificate", command=self.generate)
        button_certificate_generation.pack()
        button_read_certificate = Button(self.root, text="Read certificate", command=self.read_certificate)
        button_read_certificate.pack()
        button_encrypt = Button(self.root, text="Encrypt file", command=self.encrypt)
        button_encrypt.pack()
        button_decrypt = Button(self.root, text="Decrypt file", command=self.decrypt)
        button_decrypt.pack()
        self.root.mainloop()

    def generate(self):
        form = GeneratorForm(self.encrypting_manager)
        form.open_form()

    def read_certificate(self):
        certificate_path = filedialog.askopenfilename()
        txt = self.encrypting_manager.read_certificate(certificate_path)
        new_window = Toplevel(self.root)
        new_window.geometry("400x200")
        label = tk.Label(new_window, text=txt)
        label.pack()

    def encrypt(self):
        form = EncryptForm(self.encrypting_manager)
        form.open_form()

    def decrypt(self):
        form = DecryptForm(self.encrypting_manager)
        form.open_form()