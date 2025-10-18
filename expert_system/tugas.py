def sistem_diagnosa(gejala):
    # Inference engine: evaluasi aturan
    if 'demam' in gejala and 'batuk' in gejala and 'sakit tenggorokan' in gejala:
        return "Diagnosa: Kemungkinan besar pasien mengalami FLU"
    elif 'demam' in gejala and 'ruam kulit' in gejala:
        return "Diagnosa: Kemungkinan besar pasien mengalami CAMPAK"
    elif 'batuk' in gejala and 'sesak napas' in gejala:
        return "Diagnosa: Kemungkinan besar pasien mengalami ASMA"
    elif not gejala:
        return "Diagnosa: Pasien dalam kondisi SEHAT"
    else:
        return "Diagnosa: Gejala tidak dikenali, perlu pemeriksaan lebih lanjut oleh dokter"

# Antarmuka untuk pasien
print("=== PUSKESMAS DIGITAL SEHAT SENTOSA ===")
print("Sistem Diagnosa Awal Berdasarkan Gejala")
print("Masukkan gejala yang dialami pasien, pisahkan dengan koma (,)")
print("Contoh: demam, batuk, sakit tenggorokan\n")

# Input dari pengguna (pasien)
input_gejala = input("Gejala: ")
list_gejala = [g.strip().lower() for g in input_gejala.split(",")]

# Diagnosa
hasil = sistem_diagnosa(list_gejala)

# Output
print("\n=== HASIL DIAGNOSA AWAL ===")
print(hasil)
