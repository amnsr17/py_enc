"""Key generation, storing, Encrypt using the key, Derypt and read using the key"""
from Crypto.Random import get_random_bytes
from Crypto.Cipher import AES

def key_gen(key_name):
    """generates a 256 bit key and saves in a binary file
    :param key_name: path and name of the key containing file
    """
    key = get_random_bytes(32)
    print(key)
    # Save the key to a file
    key_file = open(key_name, "wb")
    key_file.write(key)
    key_file.close()

def crypter(in_file, key):
    """reads a file, encrypts its contents in AES
    :param in_file: file to be encrypted
    :param key: already generated key encryption
    """
    inp_f = open(in_file, "rb")
    out_f = open(in_file+".enc", "wb")

    # 64kb buffer in bytes
    read_buffer =  65536
    # cipher object to encrypt file/buffer contents
    cipher = AES.new(key, AES.MODE_CFB)

    # writing iv first
    out_f.write(cipher.iv)
    # then encrypting the whole stream buffer by buffer
    buffer = inp_f.read(read_buffer)
    while len(buffer) > 0:
        encrypted_buffer = cipher.encrypt(buffer)
        out_f.write(encrypted_buffer)
        buffer = inp_f.read(read_buffer)

    inp_f.close()
    out_f.close()


def de_crypter(in_file, key):
    """decrypts the file's contents using the provided key and saves the decrypted file
    :param in_file: file to be decrypted
    :param key: already generated key for decryption
    """
    inp_f = open(in_file, "rb")
    # out_f = open(in_file+".txt", "w", encoding="utf-8")
    out_f = open(in_file + ".decoded", "wb")

    # Read in the iv
    iv = inp_f.read(16)
    cipher = AES.new(key, AES.MODE_CFB, iv=iv)

    read_buffer =  65536
    buffer = inp_f.read(read_buffer)
    while len(buffer) > 0:
        decrypted_bytes = cipher.decrypt(buffer)
        out_f.write(decrypted_bytes)
        buffer = inp_f.read(read_buffer)
      

    inp_f.close()
    out_f.close()

def main():
    key_gen("enc_key2")
    with open("enc_key2", "rb") as key_f:
        key = key_f.read()
        print(key)

    crypter("dummy_data_img_multi4", key)
    de_crypter("dummy_data_img_multi4.enc", key)


if __name__ == '__main__':
    main()

