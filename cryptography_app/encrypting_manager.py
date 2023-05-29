from cryptography.x509.oid import NameOID
from datetime import datetime, timedelta
from cryptography.x509 import load_pem_x509_certificate
from cryptography.hazmat.primitives import padding
from cryptography import x509
from cryptography.hazmat.primitives import serialization
from cryptography.hazmat.primitives.asymmetric import rsa, padding
from cryptography.hazmat.primitives.ciphers import Cipher, algorithms, modes
from cryptography.hazmat.backends import default_backend
from cryptography.hazmat.primitives import hashes
import os



class EncryptingManager:
    def __int__(self):
        self.name = "c00oOoOl manager"

    def generate_keys(self, public_key_path, private_key_path):
        # Wygenerowanie pary kluczy
        private_key = rsa.generate_private_key(
            public_exponent=65537,
            key_size=2048
        )

        # Pobranie klucza publicznego z prywatnego klucza
        public_key = private_key.public_key()

        # Serializacja klucza publicznego do formatu PEM
        pem_public_key = public_key.public_bytes(
            encoding=serialization.Encoding.PEM,
            format=serialization.PublicFormat.SubjectPublicKeyInfo
        )

        # Serializacja prywatnego klucza do formatu PEM
        pem_private_key = private_key.private_bytes(
            encoding=serialization.Encoding.PEM,
            format=serialization.PrivateFormat.PKCS8,
            encryption_algorithm=serialization.NoEncryption()
        )

        # Zapis klucza publicznego do pliku
        with open(public_key_path, 'wb') as file:
            file.write(pem_public_key)

        # Zapis klucza prywatnego do pliku
        with open(private_key_path, 'wb') as file:
            file.write(pem_private_key)

    def encrypt_file(self, file_path, symmetric_key, iv, encrypted_file_path):
        cipher = Cipher(algorithms.AES(symmetric_key), modes.CBC(iv), backend=default_backend())
        encryptor = cipher.encryptor()

        with open(file_path, "rb") as file:
            file_data = file.read()

        padder = padding.PKCS7(algorithms.AES.block_size).padder()
        padded_data = padder.update(file_data) + padder.finalize()
        encrypted_data = encryptor.update(padded_data) + encryptor.finalize()

        with open(encrypted_file_path, "wb") as file:
            file.write(encrypted_data)

    def get_public_key_from_certificate(self, certificate_path):
        with open(certificate_path, "rb") as file:
            certificate_data = file.read()

        certificate = x509.load_pem_x509_certificate(certificate_data, default_backend())
        public_key = certificate.public_key()

        return public_key


    def generate_certificate(self, public_key_path, private_key_path, certificate_path, common_name, organization_name, country_name):
        # Odczytanie klucza publicznego
        with open(public_key_path, "rb") as file:
            public_key = serialization.load_pem_public_key(
                file.read(),
                backend=default_backend()
            )

        # Odczytanie klucza prywatnego
        with open(private_key_path, "rb") as file:
            private_key = serialization.load_pem_private_key(
                file.read(),
                password=None,
                backend=default_backend()
            )

        # Utworzenie informacji o właścicielu certyfikatu
        subject = issuer = x509.Name([
            x509.NameAttribute(NameOID.COMMON_NAME, common_name),
            x509.NameAttribute(NameOID.ORGANIZATION_NAME, organization_name),
            x509.NameAttribute(NameOID.COUNTRY_NAME, country_name)
        ])

        # Utworzenie numeru seryjnego certyfikatu
        serial_number = x509.random_serial_number()

        # Określenie okresu ważności certyfikatu
        valid_from = datetime.utcnow()
        valid_to = valid_from + timedelta(days=365)

        # Utworzenie certyfikatu
        builder = (
            x509.CertificateBuilder()
            .subject_name(subject)
            .issuer_name(issuer)
            .public_key(public_key)
            .serial_number(serial_number)
            .not_valid_before(valid_from)
            .not_valid_after(valid_to)
        )

        # Podpisanie certyfikatu przez właściciela
        certificate = builder.sign(
            private_key=private_key, algorithm=hashes.SHA256()
        )

        # Zapis certyfikatu do pliku
        with open(certificate_path, "wb") as file:
            file.write(certificate.public_bytes(serialization.Encoding.PEM))

    def read_certificate(self, certificate_path):
        # Odczytanie certyfikatu
        with open(certificate_path, "rb") as file:
            certificate = load_pem_x509_certificate(file.read())

        # Odczytanie informacji o właścicielu certyfikatu
        subject = certificate.subject

        # Wypisanie informacji o właścicielu
        text = "Nazwa: {}\nOrganizacja: {}\nKraj: {}".format(
            subject.get_attributes_for_oid(NameOID.COMMON_NAME)[0].value,
            subject.get_attributes_for_oid(NameOID.ORGANIZATION_NAME)[0].value,
            subject.get_attributes_for_oid(NameOID.COUNTRY_NAME)[0].value
        )
        return text



    def encrypt_with_hybrid(self, file_path, receiver_certificate_path, output_path):
        public_key = self.get_public_key_from_certificate(receiver_certificate_path)

        def pad_data(data):
            block_size = 16
            padding_size = block_size - (len(data) % block_size)
            padding = bytes([padding_size] * padding_size)
            return data + padding

        """
        # Odczytanie klucza publicznego
        with open(public_key_path, "rb") as file:
            public_key = serialization.load_pem_public_key(
                file.read(),
                backend=default_backend()
            )
        """

        # Wygenerowanie losowego klucza symetrycznego
        symmetric_key = os.urandom(32)  # 32 bajty = 256 bitów

        # Wygenerowanie losowego wektora inicjalizacyjnego (IV)
        iv = os.urandom(16)  # 16 bajtów = 128 bitów

        # Szyfrowanie pliku symetrycznym algorytmem AES w trybie CBC z wygenerowanym kluczem i IV
        cipher = Cipher(algorithms.AES(symmetric_key), modes.CBC(iv), backend=default_backend())
        encryptor = cipher.encryptor()

        with open(file_path, "rb") as file:
            plaintext = file.read()
            padded_plaintext = pad_data(plaintext)
            ciphertext = encryptor.update(padded_plaintext) + encryptor.finalize()

        # Szyfrowanie klucza symetrycznego za pomocą klucza publicznego RSA
        encrypted_symmetric_key = public_key.encrypt(
            symmetric_key,
            padding.OAEP(
                mgf=padding.MGF1(algorithm=hashes.SHA256()),
                algorithm=hashes.SHA256(),
                label=None
            )
        )

        # Zapisanie zaszyfrowanych danych do pliku wyjściowego
        with open(output_path, "wb") as file:
            file.write(iv)
            file.write(encrypted_symmetric_key)
            file.write(ciphertext)

    def decrypt_with_hybrid(self, file_path, private_key_path, output_path):
        # Odczytanie klucza prywatnego
        with open(private_key_path, "rb") as file:
            private_key = serialization.load_pem_private_key(
                file.read(),
                password=None,
                backend=default_backend()
            )

        # Odczytanie zaszyfrowanych danych
        with open(file_path, "rb") as file:
            iv = file.read(16)
            encrypted_symmetric_key = file.read(256)  # Długość klucza RSA w bajtach
            ciphertext = file.read()

        # Odszyfrowanie klucza symetrycznego za pomocą klucza prywatnego RSA
        symmetric_key = private_key.decrypt(
            encrypted_symmetric_key,
            padding.OAEP(
                mgf=padding.MGF1(algorithm=hashes.SHA256()),
                algorithm=hashes.SHA256(),
                label=None
            )
        )

        # Odszyfrowanie pliku symetrycznym algorytmem AES w trybie CBC z użyciem IV
        cipher = Cipher(algorithms.AES(symmetric_key), modes.CBC(iv), backend=default_backend())
        decryptor = cipher.decryptor()

        plaintext = decryptor.update(ciphertext) + decryptor.finalize()

        # Zapisanie odszyfrowanych danych do pliku wyjściowego
        with open(output_path, "wb") as file:
            file.write(plaintext)
