import pyotp
import time

class OTPGenerator:
    def __init__(self, secret: str):
        """Initialize the OTPGenerator with a secret."""
        self.secret = secret
        self.totp = pyotp.TOTP(secret)

    def generate_otp(self) -> str:
        """Generate a new OTP."""
        return self.totp.now()

    def validate_otp(self, otp: str) -> bool:
        """Validate the provided OTP against the current one."""
        return self.totp.verify(otp)

    def get_secret(self) -> str:
        """Return the secret key."""
        return self.secret
