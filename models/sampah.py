from abc import ABC, abstractmethod


class Sampah(ABC):

    def __init__(self, jenis: str, berat: float):
        if berat <= 0:
            raise ValueError("Berat sampah harus lebih dari nol.")
        self._jenis = jenis
        self._berat = float(berat)

    @property
    def jenis(self) -> str:
        return self._jenis

    @property
    def berat(self) -> float:
        return self._berat

    @abstractmethod
    def hitung_poin(self) -> int:
        pass

    def __str__(self) -> str:
        return f"{self.jenis} ({self.berat} kg) - {self.hitung_poin()} poin"