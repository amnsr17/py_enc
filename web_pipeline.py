from Crypto.Cipher import AES
from crypton import crypter
from io import StringIO
import re


def web_de_crypter(in_file, key):
    """decrypts the file's contents using the provided key and saves the decrypted file
    :param in_file: file to be decrypted
    :param key: already generated key for decryption
    :return StringIO object containing decrypted data
    """
    inp_f = open(in_file, "rb")
    # out_f = open(in_file + ".decoded", "wb")

    # Read in the iv
    iv = inp_f.read(16)
    cipher = AES.new(key, AES.MODE_CFB, iv=iv)

    read_buffer = 65536
    buffer = inp_f.read(read_buffer)

    decrypted_buffer = StringIO("")

    while len(buffer) > 0:
        decrypted_bytes = cipher.decrypt(buffer)
        decrypted_buffer.write(decrypted_bytes.decode())

        buffer = inp_f.read(read_buffer)

    # moving pointer to the buffer's start
    decrypted_buffer.seek(0)
    inp_f.close()
    return decrypted_buffer


def main():
    key = b'\xae\xee\x81T /1\xbd\xba2Y\xa7\x85e=\xd7D;\x85;\xd0\xcc\xb9N\xc6\x91&\xc8\x95\x1a4\xed'
    crypter("dummy_data_img_multi4", key)
    data = web_de_crypter("dummy_data_img_multi4.enc", key)
    data = data.read()
    # print(data)
    data = data.splitlines()

    full_path = data[0]
    marker_string = data[1]
    marker_string = re.sub("\(", '', marker_string)
    marker_string = re.sub("\)", '', marker_string)
    marker_list = marker_string.split(',')

    image_string = data[2]
    image_list = image_string.split('#')

    marker_class_desc = data[3]
    marker_class_desc_list = marker_class_desc.split(',')

    print(full_path,"\n",marker_list,"\n",image_list,"\n", marker_class_desc_list)


if __name__ == '__main__':
    main()

