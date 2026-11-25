# ==============================================================================
# SUPERCLASS: Menu
# Merepresentasikan entitas dasar menu restoran dengan penerapan Encapsulation
# ==============================================================================

class Menu:
    # Constructor untuk menginisialisasi atribut private
    def __init__(self, kode_menu, nama_menu, harga, tersedia=True):
        self.__kode_menu = kode_menu
        self.__nama_menu = nama_menu
        self.__harga = harga
        self.__tersedia = tersedia

    # GETTER (Mengambil nilai atribut private)
    def get_kode_menu(self):
        return self.__kode_menu

    def get_nama_menu(self):
        return self.__nama_menu

    def get_harga(self):
        return self.__harga

    def is_tersedia(self):
        return self.__tersedia

    # SETTER (Mengubah nilai atribut private dengan validasi)
    def set_harga(self, harga_baru):
        if harga_baru > 0:
            self.__harga = harga_baru
            return True
        return False

    def set_tersedia(self, status):
        if isinstance(status, bool):
            self.__tersedia = status
            return True
        return False

    # METHOD TAMBAHAN
    def cek_status(self):
        return "Tersedia" if self.__tersedia else "Habis"

    def tampilkan_info(self):
        print(f"[{self.__kode_menu}] {self.__nama_menu} - Rp {self.__harga:,} ({self.cek_status()})")
