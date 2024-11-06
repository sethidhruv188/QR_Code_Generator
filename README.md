# QR Code Generator

This is a simple Python script that generates a QR code from a user-provided link and saves it as a PNG file with a user-specified title.

## Requirements

- Python 3.6 or higher
- `pyqrcode` library
- `pypng` library
- `Pillow` library

## Installation

First, ensure you have Python installed. Then, install the required libraries using `pip`:

```bash
pip install pyqrcode pypng pillow
```
## Usage

1. Clone or download this repository to your local machine.

2. Open a terminal or command prompt and navigate to the directory containing the script.

3. Run the script:

   ```bash
   python QR_generator.py
   ```
4. Enter the QR Code when prompted
5. Enter the title for the QR Code file when prompted
6. The QR code will be generated and saved as a PNG file with the specified title. The script will also display the QR code image and print a confirmation message

## Example
Here's an example interaction with the script:
```bash
Enter QR Code Link: https://www.example.com
Enter the title for the QR code file: ExampleQRCode
```
The script will save the QR code as ExampleQRCode.png in the current directory and display the QR code image.

## License
This project is licensed under the GPL-3.0 License. See the [LICENSE](LICENSE) file for more details.
 
