"""QR Code Generator with limited customization"""

import qrcode

def get_user_input():
    data = input("Enter the text or url: ").strip()
    filename = input("Enter desired filename (include .jpg extension): ").strip()
    return data, filename

def create_qr_code(data):
    qr = qrcode.QRCode(box_size=10, border=4)
    qr.add_data(data)
    return qr

def create_qr_image(qr, filename):
    image = qr.make_image(fill_color="black", back_color="white")
    image.save(filename)


def generate_final_qr_code():
    data, filename = get_user_input()

    qr = create_qr_code(data)

    create_qr_image(qr, filename)

    print(f"QR code saved as {filename}")

generate_final_qr_code()