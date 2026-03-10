import qrcode
import argparse
import sys
import os

def generate_qr(data: str, output_path: str = "output.png"):
    """
    Generates a QR code and saves it as an image.
   
    """
    try:
        qr = qrcode.QRCode(
            version=1,
            error_correction=qrcode.constants.ERROR_CORRECT_L,
            box_size=10,
            border=4,
        )
        qr.add_data(data)
        qr.make(fit=True)

        img = qr.make_image(fill_color="black", back_color="white")
        img.save(output_path)
        # Using absolute path for clarity in Windows
        print(f"Success: QR code saved to {os.path.abspath(output_path)}")
    except Exception as e:
        print(f"Error generating QR code: {e}")
        sys.exit(1)

if __name__ == "__main__":
    # If no arguments are passed, ask for input (useful for double-clicking the EXE)
    if len(sys.argv) == 1:
        data_input = input("Enter the URL or text for the QR code: ")
        if data_input:
            generate_qr(data_input)
            input("Press Enter to exit...")
    else:
        parser = argparse.ArgumentParser(description="Generate a QR Code.")
        parser.add_argument("data", help="URL or string to encode")
        parser.add_argument("-o", "--output", default="output.png", help="Output path")
        args = parser.parse_args()
        generate_qr(args.data, args.output)
