import qrcode
import argparse
import sys

def generate_qr(data: str, output_path: str = "output.png"):
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
        print(f"Success: QR code saved to {output_path}")
    except Exception as e:
        print(f"Error generating QR code: {e}")
        sys.exit(1)

if __name__ == "__main__":
    parser = argparse.ArgumentParser(description="Generate a QR Code from a URL or string.")
    parser.add_argument("data", help="URL or string to encode")
    parser.add_argument("-o", "--output", default="output.png", help="Output file path")
    args = parser.parse_args()

    generate_qr(args.data, args.output)
