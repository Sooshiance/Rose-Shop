import pyotp 


def otpToken(user, phone):
    totp = pyotp.TOTP(pyotp.random_base32(), interval=60)

    otp = totp.now()

    print(f"The OTP is : {otp}")
