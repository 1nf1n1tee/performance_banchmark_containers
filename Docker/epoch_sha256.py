from subprocess import call

def open_py_file():
    for i in range(10):
        call(["python3", "sha256_dedup.py"])


if __name__ == "__main__":
    open_py_file()