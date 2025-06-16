# personality_app.py

def run_personality_quiz():
    """
    Menjalankan Kalkulator Kepribadian (Mini Tes Psikologi) sederhana.
    """
    print("====================================")
    print("  Kalkulator Kepribadian Sederhana  ")
    print("           (Mini Tes Psikologi)     ")
    print("====================================")
    print("\nJawablah pertanyaan-pertanyaan berikut dengan jujur ya!\n")

    scores = {'A': 0, 'B': 0, 'C': 0, 'D': 0}

    questions = [
        {
            "question": "Ketika ada masalah, kamu cenderung...",
            "options": {
                "a": "Menganalisis data dan mencari solusi logis.",
                "b": "Mencari ide-ide baru dan pendekatan yang tidak biasa.",
                "c": "Berdiskusi dengan orang lain dan mencari konsensus.",
                "d": "Langsung bertindak dan mencari solusi yang cepat."
            },
            "answers": {"a": 'A', "b": 'B', "c": 'C', "d": 'D'}
        },
        {
            "question": "Di waktu luang, kamu lebih suka...",
            "options": {
                "a": "Membaca buku atau belajar hal baru.",
                "b": "Melukis, menulis, atau kegiatan seni.",
                "c": "Berkumpul dengan teman atau keluarga.",
                "d": "Aktivitas fisik atau proyek praktis."
            },
            "answers": {"a": 'A', "b": 'B', "c": 'C', "d": 'D'}
        },
        {
            "question": "Dalam sebuah tim, peran favoritmu adalah...",
            "options": {
                "a": "Perencana dan pemecah masalah.",
                "b": "Pencetus ide dan inovator.",
                "c": "Penengah dan pembangun hubungan.",
                "d": "Pelaksana dan pengambil keputusan."
            },
            "answers": {"a": 'A', "b": 'B', "c": 'C', "d": 'D'}
        },
        {
            "question": "Saat menghadapi perubahan, kamu merasa...",
            "options": {
                "a": "Tertarik memahami dampaknya secara detail.",
                "b": "Antusias dengan kemungkinan baru.",
                "c": "Beradaptasi dan menjaga keharmonisan.",
                "d": "Siap hadapi tantangan dan bertindak."
            },
            "answers": {"a": 'A', "b": 'B', "c": 'C', "d": 'D'}
        },
        {
            "question": "Gaya belajarmu yang paling efektif adalah...",
            "options": {
                "a": "Melalui logika dan pemikiran kritis.",
                "b": "Eksperimen dan eksplorasi.",
                "c": "Diskusi dan interaksi sosial.",
                "d": "Praktik langsung dan pengalaman."
            },
            "answers": {"a": 'A', "b": 'B', "c": 'C', "d": 'D'}
        }
    ]

    for i, q in enumerate(questions):
        print(f"\n{i + 1}. {q['question']}")
        for key, value in q['options'].items():
            print(f"   {key}. {value}")
        while True:
            answer = input("Pilihanmu (a/b/c/d): ").lower()
            if answer in q['answers']:
                scores[q['answers'][answer]] += 1
                break
            else:
                print("Pilihan tidak valid. Coba lagi.")

    main_personality = max(scores, key=scores.get)

    print("\n====================================")
    print("         Hasil Kepribadianmu        ")
    print("====================================")
    if main_personality == 'A':
        print("Kamu ANALITIS: logis, detail, pemikir kritis.")
    elif main_personality == 'B':
        print("Kamu KREATIF: inovatif, imajinatif, suka ide baru.")
    elif main_personality == 'C':
        print("Kamu SOSIAL: komunikatif, empatis, suka kerja tim.")
    elif main_personality == 'D':
        print("Kamu PRAKTIS: realistis, langsung bertindak.")
    else:
        print("Oops, terjadi kesalahan.")

    print("\nTerima kasih sudah mencoba!")

if __name__ == "__main__":
    run_personality_quiz()
