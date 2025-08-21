class Buku:
    def __init__(self, isbn, judul, pengarang, jumlah, terpinjam=0):
        self.isbn = isbn
        self.judul = judul
        self.pengarang = pengarang
        self.jumlah = jumlah
        self.terpinjam = terpinjam

    def __str__(self):
        return f"ISBN: {self.isbn}, Judul: {self.judul}, Pengarang: {self.pengarang}, Jumlah: {self.jumlah}, Terpinjam: {self.terpinjam}"

books = [
    Buku("9786231800718", "Dasar-Dasar Pengembangan Perangkat Lunak dan Gim Vol. 2", "Okta Purnawirawan", 15, 0),
    Buku("9786237121144", "Kumpulan Solusi Pemrograman Python", "Budi Raharjo", 6, 0),
    Buku("9786026163905", "Analisis dan Perancangan Sistem Informasi", "Adi Sulistyo Nugroho", 2, 1),
    Buku("9786022912828", "Animal Farm", "George Orwell", 4, 0)
]

records = [
    {"isbn":"9786022912828", "status":"Selesai", "tanggal_pinjam":"2025-03-21", "tanggal_kembali":"2025-03-28"},
    {"isbn":"9786026163905", "status":"Belum", "tanggal_pinjam":"2025-07-22", "tanggal_kembali":""},
]

def tampilkan_data():
    print("\n---=== DATA BUKU ===---")
    if not books:
        print("Tidak ada data buku.")
        return
    for book in books:
        print(book)

def tambah_data():
    isbn = input("Masukkan ISBN: ")
    for book in books:
        if book.isbn == isbn:
            print("Buku dengan ISBN ini sudah ada.")
            return
    judul = input("Masukkan Judul: ")
    pengarang = input("Masukkan Pengarang: ")
    jumlah = int(input("Masukkan Jumlah: "))
    books.append(Buku(isbn, judul, pengarang, jumlah, 0))
    print("Buku berhasil ditambahkan.")

def edit_data():
    isbn = input("Masukkan ISBN buku yang ingin diedit: ")
    for book in books:
        if book.isbn == isbn:
            book.judul = input("Masukkan Judul baru: ")
            book.pengarang = input("Masukkan Pengarang baru: ")
            book.jumlah = int(input("Masukkan Jumlah baru: "))
            print("Data buku berhasil diubah.")
            return
    print("Buku dengan ISBN ini tidak ditemukan.")

def hapus_data():
    isbn = input("Masukkan ISBN buku yang ingin dihapus: ")
    for book in books:
        if book.isbn == isbn:
            books.remove(book)
            print("Buku berhasil dihapus.")
            return
    print("Buku dengan ISBN ini tidak ditemukan.")

def tampilkan_peminjaman():
    print("\n---=== DATA PEMINJAMAN ===---")
    if not records:
        print("Tidak ada data peminjaman.")
        return
    for record in records:
        print(f"ISBN: {record['isbn']}, Status: {record['status']}, Tanggal Pinjam: {record['tanggal_pinjam']}, Tanggal Kembali: {record['tanggal_kembali']}")

def tampilkan_belum():
    print("\n---=== PEMINJAMAN BELUM KEMBALI ===---")
    found = False
    for record in records:
        if record['status'] == "Belum":
            found = True
            print(f"ISBN: {record['isbn']}, Tanggal Pinjam: {record['tanggal_pinjam']}")
    if not found:
        print("Tidak ada peminjaman yang belum kembali.")

def peminjaman():
    isbn = input("Masukkan ISBN buku yang ingin dipinjam: ")
    for book in books:
        if book.isbn == isbn:
            if book.jumlah > book.terpinjam:
                book.terpinjam += 1
                records.append({"isbn": isbn, "status": "Belum", "tanggal_pinjam": "2025-03-21", "tanggal_kembali": ""})
                print("Buku berhasil dipinjam.")
            else:
                print("Buku sudah habis dipinjam.")
            return
    print("Buku tidak ditemukan.")

def pengembalian():
    isbn = input("Masukkan ISBN buku yang ingin dikembalikan: ")
    tanggal_kembali = input("Masukkan tanggal pengembalian (YYYY-MM-DD): ")
    for book in books:
        if book.isbn == isbn:
            if book.terpinjam > 0:
                book.terpinjam -= 1
                for record in records:
                    if record['isbn'] == isbn and record['status'] == "Belum":
                        record['status'] = "Selesai"
                        record['tanggal_kembali'] = tanggal_kembali
                        break
                print("Buku berhasil dikembalikan.")
            else:
                print("Buku ini tidak sedang dipinjam.")
            return
    print("Buku tidak ditemukan.")

while True:
    print("\n---=== MENU ===---")
    print("[1] Tampilkan Data Buku")
    print("[2] Tambah Data Buku")
    print("[3] Edit Data Buku")
    print("[4] Hapus Data Buku")
    print("---------------------------")
    print("[5] Tampilkan Semua Peminjaman")
    print("[6] Tampilkan Peminjaman Belum Kembali")
    print("[7] Peminjaman Buku")
    print("[8] Pengembalian Buku")
    print("[X] Keluar")

    menu = input("Pilih menu (1-8 atau X): ")
    if menu == "1":
        tampilkan_data()
    elif menu == "2":
        tambah_data()
    elif menu == "3":
        edit_data()
    elif menu == "4":
        hapus_data()
    elif menu == "5":
        tampilkan_peminjaman()
    elif menu == "6":
        tampilkan_belum()
    elif menu == "7":
        peminjaman()
    elif menu == "8":
        pengembalian()
    elif menu.lower() == "x":
        print("Terima kasih telah menggunakan program ini!")
        break
    else:
        print("Pilihan tidak valid, silakan coba lagi.")

    input("\nTekan Enter untuk melanjutkan...")