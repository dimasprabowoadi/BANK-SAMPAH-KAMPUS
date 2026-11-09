import unittest

from models.jenis_sampah import SampahPlastik, SampahKertas, SampahLogam


class TestBankSampah(unittest.TestCase):
    def test_poin_per_jenis(self):
        self.assertEqual(SampahPlastik(2).hitung_poin(), 20)
        self.assertEqual(SampahKertas(2).hitung_poin(), 10)
        self.assertEqual(SampahLogam(2).hitung_poin(), 40)


if __name__ == "__main__":
    unittest.main()