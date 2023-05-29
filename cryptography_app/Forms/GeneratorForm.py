from tkinter import Tk, Button, Label, Entry, filedialog
import os
from tkinter import messagebox


class GeneratorForm:
    def __init__(self, encrypting_manager):
        self.encrypting_manager = encrypting_manager
        self.root = Tk()
        self.root.title("Generator Form")

        # Etykiety
        Label(self.root, text="Common name:").grid(row=0, column=0)
        Label(self.root, text="Organization name:").grid(row=1, column=0)
        Label(self.root, text="Country name:").grid(row=2, column=0)
        Label(self.root, text="Output Folder:").grid(row=3, column=0)

        # Entry
        self.common_name_entry = Entry(self.root, width=30)
        self.common_name_entry.grid(row=0, column=1)
        self.organization_name_entry = Entry(self.root, width=30)
        self.organization_name_entry.grid(row=1, column=1)
        self.country_name_entry = Entry(self.root, width=30)
        self.country_name_entry.grid(row=2, column=1)
        self.output_folder_entry = Entry(self.root, width=30)
        self.output_folder_entry.grid(row=3, column=1)

        # Przyciski
        output_folder_button = Button(self.root, text="Browse", command=self.choose_output_folder)
        output_folder_button.grid(row=3, column=2)
        encrypt_button = Button(self.root, text="Generate", command=self.generate)
        encrypt_button.grid(row=5, column=0, columnspan=3)



    def choose_output_folder(self):
        folder_path = filedialog.askdirectory()
        self.output_folder_entry.delete(0, 'end')
        self.output_folder_entry.insert(0, folder_path)

    def generate(self):
        common_name = self.common_name_entry.get()
        organization_name = self.organization_name_entry.get()
        country_name = self.country_name_entry.get()
        output_folder = self.output_folder_entry.get()

        public_key_path = os.path.join(output_folder, 'public_key.pem')
        private_key_path = os.path.join(output_folder, 'private_key.pem')
        certificate_path = os.path.join(output_folder, 'certificate.pem')

        self.encrypting_manager.generate_keys(public_key_path, private_key_path)
        self.encrypting_manager.generate_certificate(public_key_path, private_key_path, certificate_path, common_name,
                                                     organization_name, country_name)

        messagebox.showinfo("OK", "OK")
        self.root.destroy()

    def open_form(self):
        self.root.mainloop()

