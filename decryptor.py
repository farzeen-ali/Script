import os

def recover_files():
    files = [f for f in os.listdir() if f.endswith(".locked")]
    
    for file in files:
        with open(file, "rb") as f:
            reversed_data = f.read()
            
        with open(file, "wb") as f:
            f.write(reversed_data[::-1])
            
        new_name = file.replace(".locked", "")
        os.rename(file, new_name)
        print(f"[*] Recovered: {new_name}")

    if os.path.exists("README.txt"):
        os.remove("README.txt")

if __name__ == "__main__":
    recover_files()
    print("\n[V] RECOVERY SUCCESSFUL!")
