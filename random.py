import random

def load_keywords(filename):
    try:
        with open(filename, "r", encoding="utf-8") as f:
            # Mengambil setiap baris yang tidak kosong dan menghilangkan spasi di awal/akhir
            return [line.strip() for line in f if line.strip()]
    except FileNotFoundError:
        print(f"Error: File '{filename}' tidak ditemukan.")
        return []

templates = [
    "how to {}",
    "where is {}",
    "why does {}",
    "give me {}",
    "what is {}",
    "explain {}",
    "describe {}",
    "tell me {}"
]

subjects = [
    "crypto", "blockchain", "web3", "nft", "airdrop",
    "bitcoin", "ethereum", "solana", "defi", "token"
]

actions = [
    "invest", "learn", "download", "sign in", "register",
    "apply", "join", "explore", "update", "trade", "analyze"
]

def generate_question():
    tmpl = random.choice(templates)
    subj = random.choice(subjects)
    act = random.choice(actions)
    return tmpl.format(f"{act} {subj}")

def main():
    original_keywords = load_keywords("keyword.txt")
    count_original = len(original_keywords)
    print(f"Keyword asli: {count_original} baris.")

    TARGET = 100000
    generated_keywords = []

    while count_original + len(generated_keywords) < TARGET:
        new_q = generate_question()
        generated_keywords.append(new_q)

    print(f"Keyword tambahan yang dihasilkan: {len(generated_keywords)} baris.")
    all_keywords = original_keywords + generated_keywords
    total = len(all_keywords)
    print(f"Total keyword: {total}")

    # Menulis keyword gabungan ke file output dengan nama "keywords.txt"
    output_filename = "keywords.txt"  # Output file sekarang menjadi "keywords.txt"
    with open(output_filename, "w", encoding="utf-8") as f:
        for kw in all_keywords:
            f.write(kw + "\n")

    print(f"Berhasil menulis {total} keyword ke file '{output_filename}'.")

if __name__ == "__main__":
    main()
