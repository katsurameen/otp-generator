# OTP Generator

A simple One-Time Password (OTP) generator using `pyotp`.

## Installation

You can install the package using pip:

```bash
pip install otp_generator
```

## Usage

### Step 1: Generate a Secret Key

Before you can generate OTPs, you need a base32-encoded secret key. You can generate one using the `pyotp` library.

1. **Open Python Shell**:
   Open a terminal or command prompt and start Python:

   ```bash
   python
   ```

2. **Generate a Secret Key**:
   Run the following commands in the Python shell:

   ```python
   import pyotp

   secret = pyotp.random_base32()
   print("Your secret key:", secret)
   ```

   Save this secret key, as you'll need it to generate and validate OTPs.

### Step 2: Generate an OTP

To generate a new OTP, use the following command:

```bash
otp-generator --secret YOUR_SECRET --generate
```

**Example**:

```bash
otp-generator --secret JBSWY3DPEHPK3PXP --generate
```

You should see the generated OTP displayed in the terminal.

### Step 3: Validate an OTP

To validate an OTP, you'll need the OTP generated by the command above or by a compatible app (like Google Authenticator).

Run the validation command:

```bash
otp-generator --secret YOUR_SECRET --validate YOUR_OTP
```

**Example**:

```bash
otp-generator --secret JBSWY3DPEHPK3PXP --validate 123456
```

- If the OTP is valid, you'll see:
  ```
  OTP is valid.
  ```
- If the OTP is invalid, you'll see:
  ```
  OTP is invalid.
  ```

### Troubleshooting Common Issues

1. **Invalid OTP Error**:
   - **Clock Sync Issue**: Ensure that the system time on both the device generating the OTP and the device validating the OTP are synchronized. OTPs are time-sensitive.
   - **Incorrect Secret**: Double-check that you are using the correct secret key for both generating and validating the OTP.

2. **Installation Issues**:
   - **Dependency Errors**: Ensure that you have the `pyotp` library installed. You can install it using:

     ```bash
     pip install pyotp
     ```

3. **Command Not Found**:
   - If you receive a "command not found" error when running `otp-generator`, ensure your Python Scripts directory is in your system’s PATH, or use the full path to the script.

## License

This project is licensed under the MIT License - see the [LICENSE](LICENSE) file for details.