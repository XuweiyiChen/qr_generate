import qrcode


def generate_qr_code(link, filename="qrcode.png"):
    """
    Generate a QR code for the given website link and save it as an image.

    :param link: The website link to encode in the QR code.
    :param filename: The filename for saving the QR code image.
    """
    qr = qrcode.QRCode(
        version=1,
        error_correction=qrcode.constants.ERROR_CORRECT_L,
        box_size=10,
        border=4,
    )
    qr.add_data(link)
    qr.make(fit=True)

    img = qr.make_image(fill="black", back_color="white")
    img.save(filename)
    print(f"QR Code saved as {filename}")


if __name__ == "__main__":
    website_link = input("Enter the website link: ")
    generate_qr_code(website_link)
