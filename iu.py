class Karyawan:
    def __init__(self, nama, posisi, gaji):
        self.nama = nama
        self.posisi = posisi
        self.gaji = gaji

    def info_karyawan(self):
        print(f"Nama: {self.nama}, Posisi: {self.posisi}, Gaji: {self.gaji}")

    def naik_gaji(self, persentase):
        kenaikan = self.gaji * persentase / 100
        self.gaji += kenaikan
        print(f"Gaji {self.nama} naik sebesar {persentase}%. Gaji baru: {self.gaji}")

class Manager(Karyawan):
    def __init__(self, nama, gaji, departemen):
        super().__init__(nama, "Manager", gaji)
        self.departemen = departemen

    def info_karyawan(self):
        print(f"Nama: {self.nama}, Posisi: {self.posisi}, Gaji: {self.gaji}, Departemen: {self.departemen}")

class Staf(Karyawan):
    def __init__(self, nama, gaji, spesialisasi):
        super().__init__(nama, "Staf", gaji)
        self.spesialisasi = spesialisasi

    def info_karyawan(self):
        print(f"Nama: {self.nama}, Posisi: {self.posisi}, Gaji: {self.gaji}, Spesialisasi: {self.spesialisasi}")

# Membuat objek karyawan
manager1 = Manager("Budi", 15000000, "IT")
staf1 = Staf("Sari", 7000000, "Sistem Keamanan")

# Menampilkan informasi karyawan
manager1.info_karyawan()
staf1.info_karyawan()

# Naik gaji
manager1.naik_gaji(10)
staf1.naik_gaji(5)
