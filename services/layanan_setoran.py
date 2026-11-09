from models.setoran import Setoran


class LayananSetoran:
    def __init__(self, bank):
        self.bank = bank

    def catat_setoran(self, nomor, daftar_sampah):
        if not daftar_sampah:
            raise ValueError("Daftar sampah tidak boleh kosong.")

        penyetor = self.bank.cari_penyetor(nomor)
        if penyetor is None:
            raise ValueError(f"Penyetor dengan nomor {nomor} tidak ditemukan.")

        setoran = Setoran(self.bank.nomor_berikutnya(), penyetor)
        for sampah in daftar_sampah:
            setoran.tambah_item(sampah)

        self.bank.simpan_setoran(setoran)
        penyetor.tambah_poin(setoran.total_poin())
        return setoran