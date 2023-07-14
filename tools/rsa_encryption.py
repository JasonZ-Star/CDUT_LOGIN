"""
rsa_encryption

这个库提供了使用RSA公钥加密密码的功能。

Usage:
------
from rsa_encryption import encrypt_password

public_key = '''
-----BEGIN PUBLIC KEY-----
<YOUR_PUBLIC_KEY_HERE>
-----END PUBLIC KEY-----
'''

password = '12345678'
encrypted_password = encrypt_password(password, public_key)
print('Encrypted Password:', encrypted_password)
"""

import base64
from Crypto.Cipher import PKCS1_v1_5 as Cipher_pksc1_v1_5
from Crypto.PublicKey import RSA


def encrypt_password(p):
    """
    使用RSA公钥对密码进行加密。

    Parameters:
    -----------
    password : str
        需要加密的密码。

    public_key : str
        RSA公钥字符串。

    Returns:
    --------
    str
        加密后的密码。

    Example:
    --------
    from rsa_encryption import encrypt_password

    public_key = '''
    -----BEGIN PUBLIC KEY-----
    <YOUR_PUBLIC_KEY_HERE>
    -----END PUBLIC KEY-----
    '''

    password = '12345678'
    encrypted_password = encrypt_password(password, public_key)
    print('Encrypted Password:', encrypted_password)
    """
    key = 'MIIBIjANBgkqhkiG9w0BAQEFAAOCAQ8AMIIBCgKCAQEAyor3CX6A6U4EoSHawtALiJoB0CkJnb/wmVkcVT5EmNupGVrVSeJo80ZAxsgd9S1CZVXxTXtJ7XjsqnzR64Qvrn+tdvj9Ck5k/6Tnp6HoKU/AQxA3tQ5Zqw6D6ihPOyVV4z4cdK5wjzEBNPhJuTjjzP4VQ4h4VseWNbfhXGK3vSes8oNn5Wwor9r1UbEJP/ZMHrDJxAcwe0GPvebAqEp4O5ZcTtWnq+/qkoUB6z/52EnCMltoPmuMC+o3fWdICBf4q70oSDClfuhLVi4mRT2K5UUH8fsxEe6oPtkvk9vVCCOZRmo0MXpXZiIqdZOtgcBzn/0mzoNd58KxeIy0ginjfwIDAQAB'
    public_key = '-----BEGIN PUBLIC KEY-----\n' + key + '\n-----END PUBLIC KEY-----'
    rsa_key = RSA.importKey(public_key)
    cipher = Cipher_pksc1_v1_5.new(rsa_key)
    cipher_text = base64.b64encode(cipher.encrypt(p.encode()))
    return "__RSA__" + cipher_text.decode()


if __name__ == '__main__':
    # 在这里替换成你自己的RSA公钥
    password = input()
    encrypted_password = encrypt_password(password)
    print('Encrypted Password:'  + encrypted_password)
