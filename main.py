
from makanan import Makanan
from minuman import Minuman
from pesanan import Pesanan

# ==============================================================================
# PROGRAM UTAMA (CLI): Aplikasi Kasir Restoran
# ==============================================================================

# List untuk menyimpan seluruh objek Menu dan Pesanan selama program berjalan
daftar_menu = []
daftar_pesanan = []


# Fungsi bantuan untuk mengisi data awal agar program siap diuji
def inisialisasi_data_awal():
    m1 = Makanan("MK01", "Nasi Goreng Spesial", 25000, "MAIN COURSE", 2, 10, True)
    m2 = Makanan("MK02", "Ayam Geprek Sambal Matah", 22000, "MAIN COURSE", 4, 12, True)
    mn1 = Minuman("MN01", "Es Teh Manis", 6000, "Regular", "Dingin", "Normal", True)
    mn2 = Minuman("MN02", "Kopi Susu Gula Aren", 18000, "Large", "Dingin", "Less Sugar", False)

    daftar_menu.extend([m1, m2, mn1, mn2])

    # Contoh 1 data pesanan awal
    p1 = Pesanan("PS01", "Andi", "05")
    p1.tambah_menu(m1, 2)
    p1.tambah_menu(mn1, 2)
    daftar_pesanan.append(p1)


# Fungsi helper mencari objek menu berdasarkan kode
def cari_objek_menu(kode):
    for menu in daftar_menu:
        if menu.get_kode_menu().lower() == kode.lower():
            return menu
    return None


# Fungsi helper mencari objek menu berdasarkan kode atau nama
def cari_menu_kode_atau_nama(kata_kunci):
    for menu in daftar_menu:
        if (menu.get_kode_menu().lower() == kata_kunci.lower()
                or menu.get_nama_menu().lower() == kata_kunci.lower()):
            return menu
    return None


# Fungsi helper mencari objek pesanan berdasarkan kode
def cari_objek_pesanan(kode):
    for pesanan in daftar_pesanan:
        if pesanan.get_kode_pesanan().lower() == kode.lower():
            return pesanan
    return None


# Fungsi bantuan untuk meminta menu sampai ditemukan atau pengguna kembali
def minta_menu(pesan):
    while True:
        kata_kunci = input(pesan + " (0 untuk kembali): ").strip()

        if kata_kunci == "0":
            return None

        menu = cari_menu_kode_atau_nama(kata_kunci)

        if menu:
            return menu

        print("Menu tidak ditemukan! Silakan masukkan kode atau nama menu yang benar.")


# Fungsi bantuan untuk meminta pesanan sampai ditemukan atau pengguna kembali
def minta_pesanan(pesan):
    while True:
        kode = input(pesan + " (0 untuk kembali): ").strip()

        if kode == "0":
            return None

        pesanan = cari_objek_pesanan(kode)

        if pesanan:
            return pesanan

        print("Pesanan tidak ditemukan! Silakan masukkan kode pesanan yang benar.")


# 1. MENU TAMBAH DATA
def menu_tambah_data():
    print("\n--- TAMBAH DATA ---")
    print("1. Tambah Menu Makanan")
    print("2. Tambah Menu Minuman")
    print("3. Buat Pesanan Baru / Tambah Item ke Pesanan")
    pilih = input("Pilih sub-menu (1-3): ")

    if pilih == "1":
        kode = input("Kode Makanan (cth: MK03): ").strip().upper()

        if cari_objek_menu(kode):
            print("Gagal! Kode menu sudah terdaftar.")
            return

        nama = input("Nama Makanan: ")
        harga = int(input("Harga (Rp): "))

        # Memilih kategori makanan
        while True:
            print("\nKategori Makanan:")
            print("1. MAIN COURSE")
            print("2. DESSERT")
            print("0. Kembali")

            kategori_input = input("Pilih kategori: ").strip().upper()

            if kategori_input == "1" or kategori_input == "MAIN COURSE":
                kategori = "MAIN COURSE"
                break
            elif kategori_input == "2" or kategori_input == "DESSERT":
                kategori = "DESSERT"
                break
            elif kategori_input == "0":
                print("Penambahan makanan dibatalkan.")
                return
            else:
                print("Kategori tidak valid! Pilih MAIN COURSE atau DESSERT.")

        pedas = int(input("Level Pedas (0-5): "))
        estimasi = int(input("Estimasi Masak (menit): "))

        makanan_baru = Makanan(kode, nama, harga, kategori, pedas, estimasi)
        daftar_menu.append(makanan_baru)
        print("Berhasil menambahkan menu makanan!")

    elif pilih == "2":
        kode = input("Kode Minuman (cth: MN03): ").strip().upper()

        if cari_objek_menu(kode):
            print("Gagal! Kode menu sudah terdaftar.")
            return

        nama = input("Nama Minuman: ")
        harga = int(input("Harga (Rp): "))
        ukuran = input("Ukuran Gelas (Regular/Large): ")
        suhu = input("Suhu (Dingin/Panas): ")
        gula = input("Tingkat Gula (Normal/Less Sugar): ")

        minuman_baru = Minuman(kode, nama, harga, ukuran, suhu, gula)
        daftar_menu.append(minuman_baru)
        print("Berhasil menambahkan menu minuman!")

    elif pilih == "3":
        kode_ps = input("Masukkan Kode Pesanan (cth: PS02): ").strip().upper()
        pesanan = cari_objek_pesanan(kode_ps)

        # Jika kode pesanan belum ada, minta data pelanggan terlebih dahulu
        if not pesanan:
            pelanggan = input("Nama Pelanggan: ")
            meja = input("Nomor Meja: ")

        # Mencari menu berdasarkan kode atau nama
        menu = minta_menu("Masukkan Kode atau Nama Menu yang dipesan")

        if not menu:
            print("Penambahan item dibatalkan.")
            return

        # Memastikan menu tersedia sebelum ditambahkan
        if not menu.is_tersedia():
            print("Menu sedang habis dan tidak bisa dipesan!")
            return

        # Memastikan jumlah pesanan berupa bilangan bulat positif
        jumlah = int(input("Jumlah porsi/gelas: "))

        if jumlah <= 0:
            print("Jumlah pesanan harus lebih dari 0!")
            return

        # Jika kode pesanan belum ada, buat objek Pesanan baru
        if not pesanan:
            pesanan = Pesanan(kode_ps, pelanggan, meja)
            daftar_pesanan.append(pesanan)
            print(f"Pesanan baru {kode_ps} dibuat.")

        # Tambahkan item menu ke pesanan
        if pesanan.tambah_menu(menu, jumlah):
            print(f"Berhasil menambahkan {jumlah}x {menu.get_nama_menu()} ke pesanan {kode_ps}.")
        else:
            print("Gagal menambahkan item (Pesanan sudah lunas atau data tidak valid).")

    else:
        print("Pilihan tidak valid.")


# 2. MENU TAMPILKAN DATA
def menu_tampilkan_data():
    print("\n--- TAMPILKAN DATA ---")
    print("1. Tampilkan Semua Daftar Menu")
    print("2. Tampilkan Semua Daftar Pesanan")
    pilih = input("Pilih sub-menu (1-2): ")

    if pilih == "1":
        print("\n=== DAFTAR MENU RESTORAN ===")

        for menu in daftar_menu:
            menu.tampilkan_info()

    elif pilih == "2":
        print("\n=== DAFTAR PESANAN RESTORAN ===")

        for pesanan in daftar_pesanan:
            pesanan.tampilkan_rincian()

    else:
        print("Pilihan tidak valid.")


# 3. MENU CARI DATA
def menu_cari_data():
    print("\n--- CARI DATA ---")
    print("1. Cari Menu (berdasarkan Kode/Nama)")
    print("2. Cari Pesanan (berdasarkan Kode Pesanan)")
    pilih = input("Pilih sub-menu (1-2): ")

    if pilih == "1":
        while True:
            kata_kunci = input(
                "Masukkan Kode atau Nama Menu (0 untuk kembali): "
            ).strip()

            if kata_kunci == "0":
                return

            ditemukan = False

            # Pencarian berdasarkan kode atau sebagian nama menu
            for menu in daftar_menu:
                if (kata_kunci.lower() in menu.get_kode_menu().lower()
                        or kata_kunci.lower() in menu.get_nama_menu().lower()):
                    menu.tampilkan_info()
                    ditemukan = True

            if ditemukan:
                break
            else:
                print("Menu tidak ditemukan! Silakan coba lagi.")

    elif pilih == "2":
        pesanan = minta_pesanan("Masukkan Kode Pesanan")

        if pesanan:
            pesanan.tampilkan_rincian()

    else:
        print("Pilihan tidak valid.")


# 4. MENU UBAH DATA
def menu_ubah_data():
    print("\n--- UBAH DATA ---")
    print("1. Ubah Harga Menu")
    print("2. Ubah Status Ketersediaan Menu (Tersedia / Habis)")
    print("3. Proses Pembayaran Pesanan (Checkout)")
    pilih = input("Pilih sub-menu (1-3): ")

    if pilih == "1":
        menu = minta_menu("Masukkan Kode atau Nama Menu")

        if menu:
            harga_baru = int(input("Masukkan Harga Baru (Rp): "))

            if menu.set_harga(harga_baru):
                print("Harga menu berhasil diperbarui!")
            else:
                print("Harga tidak valid.")

    elif pilih == "2":
        menu = minta_menu("Masukkan Kode atau Nama Menu")

        if menu:
            status_input = input("Set tersedia? (y/n): ").lower()

            if status_input == "y":
                menu.set_tersedia(True)
            elif status_input == "n":
                menu.set_tersedia(False)
            else:
                print("Input tidak valid! Masukkan y atau n.")
                return

            print(f"Status {menu.get_nama_menu()} diubah menjadi: {menu.cek_status()}")

    elif pilih == "3":
        pesanan = minta_pesanan("Masukkan Kode Pesanan yang akan dibayar")

        if pesanan:
            if pesanan.proses_pembayaran():
                print(f"Pembayaran pesanan {pesanan.get_kode_pesanan()} BERHASIL! Total: Rp {pesanan.hitung_total():,}")
            else:
                print("Gagal membayar (Pesanan kosong atau sudah dibayar sebelumnya).")

    else:
        print("Pilihan tidak valid.")


# 5. MENU CEK STATUS DATA
def menu_cek_status():
    print("\n=== CEK STATUS KETERSEDIAAN MENU ===")

    for menu in daftar_menu:
        print(f"- {menu.get_kode_menu()} | {menu.get_nama_menu()} : {menu.cek_status()}")

    print("\n=== CEK STATUS PEMBAYARAN PESANAN ===")

    for pesanan in daftar_pesanan:
        print(f"- {pesanan.get_kode_pesanan()} (Pelanggan: {pesanan.get_nama_pelanggan()}) "
              f"| Total: Rp {pesanan.hitung_total():,} | Status: {pesanan.cek_status_pesanan()}")


# JALANKAN PROGRAM UTAMA
if __name__ == "__main__":
    inisialisasi_data_awal()

    while True:
        print("\n==========================================")
        print("   APLIKASI KASIR RESTORAN (OOP PYTHON)   ")
        print("==========================================")
        print("1. Tambah Data (Menu / Pesanan)")
        print("2. Tampilkan Data")
        print("3. Cari Data")
        print("4. Ubah Data & Pembayaran")
        print("5. Cek Status Data")
        print("6. Keluar dari Program")

        pilihan = input("Pilih menu utama (1-6): ")

        try:
            if pilihan == "1":
                menu_tambah_data()
            elif pilihan == "2":
                menu_tampilkan_data()
            elif pilihan == "3":
                menu_cari_data()
            elif pilihan == "4":
                menu_ubah_data()
            elif pilihan == "5":
                menu_cek_status()
            elif pilihan == "6":
                print("Terima kasih telah menggunakan Aplikasi Kasir Restoran.")
                break
            else:
                print("Pilihan tidak valid, silakan masukkan angka 1-6.")

        except ValueError:
            print("Input error: Pastikan Anda memasukkan angka untuk harga/jumlah!")
