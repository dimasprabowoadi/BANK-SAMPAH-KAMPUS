class BankSampah:
    def __init__(self, nama):
        self.nama = nama
        self.__penyetor = []
        self.__setoran = []

    def tambah_penyetor(self, penyetor):
        if self.cari_penyetor(penyetor.nim) is not None:
            raise ValueError("NIM sudah terdaftar.")
        self.__penyetor.append(penyetor)

    def cari_penyetor(self, nim):
        for p in self.__penyetor:
            if p.nim == nim:
                return p
        return None

    def simpan_setoran(self, setoran):
        self.__setoran.append(setoran)

    def nomor_berikutnya(self):
        return len(self.__setoran) + 1