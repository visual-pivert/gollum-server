import unittest
from domain.ftp.adapters.FileOperations import Compression, FileManipulation
from domain.ftp.adapters.ProjectDeployement import Ftp, ProjectDeployment


class TestCompression(unittest.TestCase):
    # def testCompressProject(self):
    #     to_compress = "/home/nyr/Pictures/New_Folder/New"
    #     res = Compression.compressProject(to_compress)
    #     print(res)
    #     self.assertTrue(res)

    # def testRemove(self):
    #     dir_to_del = "/home/nyr/Pictures/New_Folder"
    #     FileManipulation.remove(dir_to_del)
    #     self.assertTrue(True)

    # def testConnectFTP(self):
    #     ftp = Ftp()
    #     ftp = ftp.connectFTP('192.168.200.136', 'gollum', 'gollum')
    #     print(ftp)
    #     ftp.disconnectFTP()
    #     self.assertTrue(ftp)

    # def testSend(self):
    #     ftp = Ftp()
    #     ftp = ftp.connectFTP('192.168.200.136', 'gollum', 'gollum')
    #     ftp.send('/home/nyr/Pictures/New_Folder/New', 'prod/')
    #     ftp.disconnectFTP()
    #     self.assertTrue(True)

    def testDeployProject(self):
        deploy = ProjectDeployment(Compression(FileManipulation()), Ftp())
        path = deploy.deployProject('/home/nyr/Pictures/digikam')
        print(path)
        self.assertTrue(True)

    # def testCreateDecompressScript(self):
    #     deploy = ProjectDeployment(Compression(FileManipulation()), Ftp())
    #     deploy.createDecompressScript('/home/nyr/snap/script.php', 'snap.tar.zx')
    #     self.assertTrue(True)


if __name__ == "__main__":
    unittest.main()
