from menu import Menu

# ==============================================================================
# CLASS RELASI (ASSOCIATION): Pesanan
# Menghubungkan transaksi pesanan pelanggan dengan beberapa objek Menu
# ==============================================================================
class Pesanan:
    # Constructor berparameter untuk membuat transaksi pesanan baru
    def __init__(self, kode_pesanan, nama_pelanggan, nomor_meja):
        self.__kode_pesanan = kode_pesanan      # Atribut private 1: ID pesanan
        self.__nama_pelanggan = nama_pelanggan  # Atribut private 2: nama pemesan
        self.__nomor_meja = nomor_meja          # Atribut private 3: nomor meja
        self.__daftar_item = []                 # Atribut private 4: list berisi [objek_menu, jumlah]
        self.__sudah_bayar = False              # Atribut private 5: status pembayaran

    # --- GETTER ---
    def get_kode_pesanan(self):
        return self.__kode_pesanan

    def get_nama_pelanggan(self):
        return self.__nama_pelanggan

    def get_nomor_meja(self):
        return self.__nomor_meja

    def is_sudah_bayar(self):
        return self.__sudah_bayar

    # --- METHOD TAMBAHAN ---
    # Method 1: Menambahkan objek Menu ke dalam daftar pesanan (Association)
    def tambah_menu(self, menu, jumlah):
        # Tolak jika objek bukan Menu atau turunannya
        if not isinstance(menu, Menu):
            return False

        # Tolak jika jumlah bukan bilangan bulat positif
        if not isinstance(jumlah, int) or isinstance(jumlah, bool) or jumlah <= 0:
            return False

        # Tolak jika pesanan sudah dibayar atau menu sedang habis
        if self.__sudah_bayar or not menu.is_tersedia():
            return False

        # Jika menu yang sama sudah ada di pesanan, tambahkan jumlahnya saja
        for item in self.__daftar_item:
            if item[0].get_kode_menu() == menu.get_kode_menu():
                item[1] += jumlah
                return True

        # Jika belum ada, masukkan pasangan [objek_menu, jumlah] ke daftar
        self.__daftar_item.append([menu, jumlah])
        return True

    # Method 2: Menghitung total seluruh harga menu dalam pesanan
    def hitung_total(self):
        total = 0
        for menu, jumlah in self.__daftar_item:
            total += menu.get_harga() * jumlah
        return total

    # Method 3: Mengubah status pesanan menjadi lunas/sudah dibayar
    def proses_pembayaran(self):
        if not self.__daftar_item or self.__sudah_bayar:
            return False
        self.__sudah_bayar = True
        return True

    # Method 4: Mengecek teks status pembayaran pesanan
    def cek_status_pesanan(self):
        return "Lunas (Sudah Dibayar)" if self.__sudah_bayar else "Belum Dibayar"

    # Method 5: Menampilkan rincian lengkap struk pesanan
    def tampilkan_rincian(self):
        print("=" * 55)
        print(f"Kode Pesanan   : {self.__kode_pesanan}")
        print(f"Nama Pelanggan : {self.__nama_pelanggan} (Meja {self.__nomor_meja})")
        print(f"Status Bayar   : {self.cek_status_pesanan()}")
        print("-" * 55)
        if not self.__daftar_item:
            print("Belum ada item menu yang dipesan.")
        else:
            for menu, jumlah in self.__daftar_item:
                subtotal = menu.get_harga() * jumlah
                print(f"- {menu.get_nama_menu()} ({jumlah}x @ Rp {menu.get_harga():,}) = Rp {subtotal:,}")
        print("-" * 55)
        print(f"TOTAL BAYAR    : Rp {self.hitung_total():,}")
        print("=" * 55)
