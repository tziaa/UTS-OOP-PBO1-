
from menu import Menu

# ==============================================================================
# SUBCLASS 1: Makanan (Mewarisi class Menu)
# ==============================================================================
class Makanan(Menu):
    # Constructor berparameter yang memanggil constructor superclass via super()
    def __init__(self, kode_menu, nama_menu, harga, kategori, level_pedas, estimasi_masak, tersedia=True):
        super().__init__(kode_menu, nama_menu, harga, tersedia)
        self.__kategori = kategori.strip().upper()  # Atribut private 1: MAIN COURSE / DESSERT
        self.__level_pedas = level_pedas            # Atribut private 2: skala 0 - 5
        self.__estimasi_masak = estimasi_masak      # Atribut private 3: waktu masak (menit)

    # --- GETTER & SETTER ---
    def get_kategori(self):
        return self.__kategori

    def get_level_pedas(self):
        return self.__level_pedas

    def get_estimasi_masak(self):
        return self.__estimasi_masak

    def set_kategori(self, kategori_baru):
        if isinstance(kategori_baru, str):
            kategori_baru = kategori_baru.strip().upper()

            if kategori_baru in ["MAIN COURSE", "DESSERT"]:
                self.__kategori = kategori_baru
                return True

        return False

    def set_level_pedas(self, level_baru):
        if 0 <= level_baru <= 5:
            self.__level_pedas = level_baru
            return True
        return False

    # --- METHOD TAMBAHAN ---
    # Method 1: Memberikan keterangan tingkat kepedasan
    def info_kepedasan(self):
        if self.__level_pedas == 0:
            return "Tidak Pedas"
        elif self.__level_pedas <= 2:
            return f"Pedas Sedang (Level {self.__level_pedas})"
        else:
            return f"Ekstra Pedas (Level {self.__level_pedas})"

    # Method 2: Override method tampilkan_info() dari superclass
    def tampilkan_info(self):
        print(f"[{self.get_kode_menu()}] {self.get_nama_menu()} (Makanan - {self.__kategori}) "
              f"| Rp {self.get_harga():,} | {self.info_kepedasan()} "
              f"| Est: {self.__estimasi_masak} mnt | Status: {self.cek_status()}")
