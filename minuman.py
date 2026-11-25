from menu import Menu

# ==============================================================================
# SUBCLASS 2: Minuman (Mewarisi class Menu)
# ==============================================================================
class Minuman(Menu):
    # Constructor berparameter yang memanggil constructor superclass via super()
    def __init__(self, kode_menu, nama_menu, harga, ukuran_gelas, suhu, tingkat_gula, tersedia=True):
        super().__init__(kode_menu, nama_menu, harga, tersedia)
        self.__ukuran_gelas = ukuran_gelas      # Atribut private 1: Regular / Large
        self.__suhu = suhu                      # Atribut private 2: Dingin / Panas
        self.__tingkat_gula = tingkat_gula      # Atribut private 3: Normal / Less Sugar

    # --- GETTER & SETTER ---
    def get_ukuran_gelas(self):
        return self.__ukuran_gelas

    def get_suhu(self):
        return self.__suhu

    def get_tingkat_gula(self):
        return self.__tingkat_gula

    def set_suhu(self, suhu_baru):
        if isinstance(suhu_baru, str) and suhu_baru.lower() in ["dingin", "panas"]:
            self.__suhu = suhu_baru.capitalize()
            return True
        return False

    # --- METHOD TAMBAHAN ---
    # Method 1: Menampilkan detail penyajian minuman
    def info_penyajian(self):
        return f"{self.__suhu}, Ukuran {self.__ukuran_gelas}, Gula: {self.__tingkat_gula}"

    # Method 2: Override method tampilkan_info() dari superclass
    def tampilkan_info(self):
        print(f"[{self.get_kode_menu()}] {self.get_nama_menu()} (Minuman) "
              f"| Rp {self.get_harga():,} | {self.info_penyajian()} "
              f"| Status: {self.cek_status()}")