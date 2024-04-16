import unittest
from domain.ftp.adapters.FileOperations import Compression


class TestCompression(unittest.TestCase):
    def testCompressProject(self):
        to_compress = "/home/nyr/Pictures/New_Folder"
        res = Compression.compressProject(to_compress)
        self.assertTrue(res)


if __name__ == "__main__":
    unittest.main()
