from .sampah import Sampah


class SampahPlastik(Sampah):
    POIN_PER_KG = 10

    def __init__(self, berat: float):
        super().__init__("Plastik", berat)

    def hitung_poin(self) -> int:
        return int(self.berat * self.POIN_PER_KG)


class SampahKertas(Sampah):
    POIN_PER_KG = 5

    def __init__(self, berat: float):
        super().__init__("Kertas", berat)

    def hitung_poin(self) -> int:
        return int(self.berat * self.POIN_PER_KG)


class SampahLogam(Sampah):
    POIN_PER_KG = 20

    def __init__(self, berat: float):
        super().__init__("Logam", berat)

    def hitung_poin(self) -> int:
        return int(self.berat * self.POIN_PER_KG)