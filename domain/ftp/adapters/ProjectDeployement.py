from domain.ftp.IFileOperations import ICompression
from domain.ftp.IProjectDeployment import IFtp, IProjectDeployment
from ftplib import FTP


class Ftp(IFtp):
    ftp = ""

    def connectFTP(self, host: str, user: str, password: str):
        try:
            self.ftp = FTP(host, user, password)
            return self
        except Exception as e:
            print(e)

    def disconnectFTP(self):
        self.ftp.quit()

    def send(self, project_path: str):
        # self.ftp.storbinary()
        pass


class ProjectDeployment(IProjectDeployment):
    def __init__(self, compression: ICompression, ftp: IFtp):
        self.compression = compression
        self.ftp = ftp

    def deployProject(self, project_path: str):
        # compressed_project = self.compression.compressProject(project_path)
        # self.ftp.send()
        # self.compression.decompressProject()
        pass
