import random
import string
import time

def generate_fake_code():
    return '-'.join(
        ''.join(random.choices(string.ascii_uppercase + string.digits, k=4))
        for _ in range(5)
    )

def main():
    print("🎮 Fake Google Play Code Generator")
    print("🧑‍💻 Created by: Ömer Yiğit Üzümcü")
    print("----------------------------------")

    try:
        count = int(input("How many codes do you want to generate? (e.g. 3): "))
    except ValueError:
        print("❌ Invalid number.")
        return

    save = input("Do you want to save the codes to a file? (yes/no): ").lower().strip()
    codes = []

    for i in range(count):
        code = generate_fake_code()
        codes.append(code)
        print(f"\nCode #{i+1}: {code}")
        time.sleep(0.5)
        print("🛑 Note: This code is already used.")

    if save == "yes":
        with open("fake_google_play_codes.txt", "w") as f:
            for i, code in enumerate(codes, start=1):
                f.write(f"Code #{i}: {code} (used)\n")
        print("\n✅ Codes saved to 'fake_google_play_codes.txt'.")

if __name__ == "__main__":
    main(