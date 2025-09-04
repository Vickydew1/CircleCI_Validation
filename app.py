import hashlib

# ❌ Hardcoded secret (SAST should flag this)
SECRET_KEY = "my-plaintext-secret"
ls = "code"
def insecure_md5(data: str) -> str:
    return hashlib.md5(data.encode()).hexdigest()  # ❌ Weak hash

if __name__ == "__main__":
    print("MD5 of test:", insecure_md5("accuknox"))



