# QR Code Generator

This is a simple Python program that generates a QR code from a website link and saves it as an image.

## Installation

First, install the required dependencies:

```bash
pip install "qrcode[pil]"
```

If you face issues with the above command, try:

```bash
pip install qrcode pillow
```

## Usage

Run the script:

```bash
python qr_generator.py
```

Enter a website link when prompted, and the QR code will be saved as `qrcode.png`.

## Example

```bash
Enter the website link: https://example.com
QR Code saved as qrcode.png
```

You can then scan the generated `qrcode.png` using a mobile device to open the website.