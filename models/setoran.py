from models.item_setoran import ItemSetoran


class Setoran:
    def __init__(self, nomor, penyetor):
        self.nomor = nomor
        self.penyetor = penyetor
        self.__items = []

    def tambah_item(self, sampah):
        item = ItemSetoran(sampah)
        self.__items.append(item)

    def total_poin(self):
        return sum(item.poin() for item in self.__items)

    def __str__(self):
        return f"Setoran {self.nomor} oleh {self.penyetor.nama} | Total poin: {self.total_poin()}"