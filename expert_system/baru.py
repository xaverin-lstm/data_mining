def get_user_input(gejala_list):
    print("Silakan jawab pertanyaan berikut dengan 'ya' atau 'tidak'.")
    user_gejala = {}
    for gejala in gejala_list:
        jawaban = input(f"Apakah Anda mengalami {gejala}? ").strip().lower()
        user_gejala[gejala] = jawaban == 'ya'
    return user_gejala

def diagnose_penyakit(user_gejala):
    rules = [
        {
            "name": "Flu",
            "conditions": ["demam", "batuk", "sakit tenggorokan"]
        },
        {
            "name": "Masuk Angin",
            "conditions": ["pusing", "mual", "lemas"]
        },
        {
            "name": "Keracunan Makanan",
            "conditions": ["sakit perut", "diare", "muntah"]
        },
        {
            "name": "Infeksi Saluran Pernapasan",
            "conditions": ["batuk kering", "demam", "sesak napas"]
        }
    ]
    
    hasil_diagnosa = []

    for rule in rules:
        if all(user_gejala.get(cond, False) for cond in rule["conditions"]):
            hasil_diagnosa.append(rule["name"])

    if hasil_diagnosa:
        print("\n✅ Hasil Diagnosa:")
        for diagnosis in hasil_diagnosa:
            print(f"- {diagnosis}")
    else:
        print("\n❌ Tidak dapat memastikan penyakit berdasarkan gejala yang Anda alami.")

def main():
    gejala_list = [
        "demam", "batuk", "sakit tenggorokan",
        "pusing", "mual", "lemas",
        "sakit perut", "diare", "muntah",
        "batuk kering", "sesak napas"
    ]
    
    user_gejala = get_user_input(gejala_list)
    diagnose_penyakit(user_gejala)

if __name__ == "__main__":
    main()