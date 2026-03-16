# -*- coding: utf-8 -*-
import base64

from Crypto.Cipher import PKCS1_v1_5
from Crypto.PublicKey import RSA


def encryption(public_key, data_to_encryption):
    """
    加密
    :param public_key: key
    :param data_to_encryption: data
    :return:
    """
    try:
        rsa_key = RSA.import_key(base64.b64decode(public_key))
        cipher = PKCS1_v1_5.new(rsa_key)
        encrypted_data = cipher.encrypt(data_to_encryption.encode())
        encoded_encrypted_data = base64.b64encode(encrypted_data).decode()
        return encoded_encrypted_data
    except Exception as e:
        print('encryption failed:', e)


def decrypt(private_key, data_to_decrypt):
    """
    解密
    :param private_key: key
    :param data_to_decrypt:data
    :return:
    """
    try:
        rsa_key = RSA.import_key(private_key)
        cipher = PKCS1_v1_5.new(rsa_key)
        encrypted_data = base64.b64decode(data_to_decrypt)
        decrypted_data = cipher.decrypt(encrypted_data, None).decode()
        return decrypted_data
    except Exception as e:
        print('decrypt failed:', e)
