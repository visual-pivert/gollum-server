import os

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

    def send(self, project_path: str, project_dist: str):
        project_path = os.path.normpath(project_path)
        # os.chdir(project_path)

        basename = os.path.basename(project_path)
        element_dist = os.path.join(project_dist, basename)
        print(f'--> {element_dist}')

        if os.path.isdir(project_path):

            print(f'create {element_dist}')
            self.ftp.mkd(element_dist)

            for element in os.listdir(project_path):
                element_source = os.path.join(project_path, element)
                self.send(element_source, element_dist)

        else:
            print(f'send {project_path} --> {element_dist}')
            with open(project_path, 'rb') as file:
                self.ftp.storbinary(f'STOR {element_dist}', file)


class ProjectDeployment(IProjectDeployment):
    host = '192.168.200.136'
    user = 'gollum'
    password = 'gollum'
    dist_tmp = 'project_tmp'
    project_dist = 'prod/'

    def __init__(self, compression: ICompression, ftp: IFtp):
        self.compression = compression
        self.ftp = ftp

    def deployProject(self, project_path: str):
        project_path = os.path.normpath(project_path)
        dist_tmp = os.path.join(self.dist_tmp, os.path.basename(project_path))
        os.mkdir(dist_tmp)

        compressed_project = self.compression.compressProject(project_path, dist_tmp)

        self.ftp.connectFTP(self.host, self.user, self.password)
        self.ftp.send(os.path.dirname(compressed_project), self.project_dist)
        self.ftp.disconnectFTP()
