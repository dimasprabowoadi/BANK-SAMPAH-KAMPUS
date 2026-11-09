from models.bank_sampah import BankSampah
from models.jenis_sampah import SampahPlastik, SampahKertas, SampahLogam
from models.penyetor import Penyetor
from services.layanan_setoran import LayananSetoran
from utils.format import format_poin


def main():
    bank = BankSampah("Bank Sampah Kampus")
    bank.tambah_penyetor(Penyetor("24001", "Dimas"))
    bank.tambah_penyetor(Penyetor("24002", "Raffi"))
    bank.tambah_penyetor(Penyetor("24003", "Grace"))

    layanan = LayananSetoran(bank)

    setoran1 = layanan.catat_setoran(
        "24001",
        [SampahPlastik(2), SampahKertas(3), SampahLogam(1)],
    )

    setoran2 = layanan.catat_setoran(
        "24002",
        [SampahPlastik(1), SampahKertas(2)],
    )

    setoran3 = layanan.catat_setoran(
        "24003",
        [SampahLogam(4)],
    )

    for setoran in (setoran1, setoran2, setoran3):
        print(
            f"Setoran ID: {setoran.nomor}, "
            f"Penyetor: {setoran.penyetor.nama}, "
            f"Total Poin: {format_poin(setoran.total_poin())}"
        )


if __name__ == "__main__":
    main()