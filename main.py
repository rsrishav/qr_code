"""
This program generates QR Code that can be used for link, profile sharing and some more use cases.
"""
import pyqrcode


def code_generate(encoding_string):
    """
    Function generates the QR code.
    :param encoding_string: String which can be enclosed in QR Code. String can even in Japanese characters.
    :type encoding_string: str
    :return: QR Code in base64 string.
    :rtype:str
    """
    qr_code = pyqrcode.create(encoding_string)
    qr_code.png("QR_code.png", scale=10)     # in PNG
    # qr_code.svg("QR_code.svg", scale=10)     # in SVG
    return qr_code.png_as_base64_str(scale=10)


if __name__ == "__main__":
    code_base64 = code_generate("こんにちは！")     # こんにちは means "Hello!"
