from dataclasses import dataclass
from .sampah import Sampah


@dataclass
class ItemSetoran:
    sampah: Sampah

    def poin(self) -> int:
        return self.sampah.hitung_poin()

    def __str__(self) -> str:
        return f"{self.sampah.jenis}: {self.sampah.berat} kg ({self.poin()} poin)"