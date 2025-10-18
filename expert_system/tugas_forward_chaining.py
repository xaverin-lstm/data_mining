def forward_chaining(gejala_input):
    gejala = [g.strip().lower() for g in gejala_input]

    rules = [
        {
            "gejala": {"demam", "batuk", "sakit tenggorokan"},
            "diagnosa": "FLU"
        },
        {
            "gejala": {"demam", "ruam kulit"},
            "diagnosa": "CAMPAK"
        },
        {
            "gejala": {"batuk", "sesak napas"},
            "diagnosa": "ASMA"
        }
    ]

    for rule in rules:
        if rule["gejala"].issubset(set(gejala)):
            return f"Diagnosa: Kemungkinan pasien mengalami {rule['diagnosa']}"

    if not gejala:
        return "Diagnosa: Pasien dalam kondisi SEHAT"

    return "Diagnosa: Gejala tidak dikenali, perlu pemeriksaan lanjutan"

# Contoh pemakaian
print("=== SISTEM PAKAR (FORWARD CHAINING) ===")
input_gejala = input("Masukkan gejala (pisahkan dengan koma): ").split(",")
hasil = forward_chaining(input_gejala)
print("\n" + hasil)
