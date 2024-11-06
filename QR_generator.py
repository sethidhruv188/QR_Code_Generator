import pyqrcode as qr
from PIL import Image

# Input QR code link and title
link = input("Enter QR Code Link: ")
file_title = input("Enter the title for the QR code file: ")
qr_code = qr.create(link)
qr_code_path = f"{file_title}.png"
qr_code.png(qr_code_path, scale=5)

# Open the QR code image
image = Image.open(qr_code_path)

# Optionally show the QR code image
image.show()

print(f"QR Code saved as {qr_code_path}")
