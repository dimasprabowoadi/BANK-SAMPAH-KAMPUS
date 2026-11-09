class Penyetor:
    def __init__(self, nim, nama):
        self.__nim = nim
        self.__nama = nama
        self.__total_poin = 0

    @property
    def nim(self):
        return self.__nim

    @property
    def nama(self):
        return self.__nama

    @property
    def total_poin(self):
        return self.__total_poin

    def tambah_poin(self, poin):
        if poin < 0:
            raise ValueError("Poin tidak boleh negatif.")
        self.__total_poin += poin

    def __str__(self):
        return f"{self.__nim} - {self.__nama} | Total poin: {self.__total_poin}"