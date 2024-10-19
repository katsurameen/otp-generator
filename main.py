import argparse
from otp import OTPGenerator

def main():
    parser = argparse.ArgumentParser(description="One-Time Password (OTP) Generator")
    parser.add_argument('--secret', required=True, help='Secret key for OTP generation')
    parser.add_argument('--generate', action='store_true', help='Generate a new OTP')
    parser.add_argument('--validate', type=str, help='Validate a provided OTP')

    args = parser.parse_args()

    otp_gen = OTPGenerator(args.secret)

    if args.generate:
        print(f"Generated OTP: {otp_gen.generate_otp()}")
    elif args.validate:
        if otp_gen.validate_otp(args.validate):
            print("OTP is valid.")
        else:
            print("OTP is invalid.")
    else:
        print("Please specify either --generate or --validate.")

if __name__ == "__main__":
    main()