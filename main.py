from input_buku import InputBuku
from proses_buku import ProsesBuku


class AplikasiBuku:

    def __init__(self):
        self.input = InputBuku()
        self.proses = ProsesBuku()

    def jalankan(self):
        print("===== APLIKASI DATA BUKU SEDERHANA (OOP) =====")

        nama = self.input.input_nama_petugas()
        daftar_buku = self.input.input_data_buku()

        total = self.proses.hitung_total_halaman(daftar_buku)
        rata = self.proses.hitung_rata_rata(daftar_buku)
        buku_terbanyak = self.proses.cari_buku_terbanyak(daftar_buku)

        print("\n===== HASIL DATA =====")
        print(f"Nama Petugas : {nama}")

        print("\nDaftar Buku:")
        for i, buku in enumerate(daftar_buku, start=1):
            print(f"{i}. {buku['judul']} - {buku['halaman']} halaman")

        print("\nTotal Halaman :", total)
        print("Rata-rata Halaman :", rata)

        print("\nBuku dengan halaman terbanyak:")
        print(f"{buku_terbanyak['judul']} ({buku_terbanyak['halaman']} halaman)")


# menjalankan program
if __name__ == "__main__":
    app = AplikasiBuku()
    app.jalankan()