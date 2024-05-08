import os
import requests
from domain.ftp.IFileOperations import ICompression
from domain.ftp.IProjectDeployment import IFtp, IProjectDeployment
from ftplib import FTP


class Ftp(IFtp):
    ftp = None

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

            if element_dist not in self.ftp.nlst(os.path.dirname(element_dist)):
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
    host = None
    user = None
    password = None
    project_dist = None
    dist_tmp = 'project_tmp'

    def __init__(self, compression: ICompression, ftp: IFtp):
        self.compression = compression
        self.ftp = ftp

    def settingFtpServer(self, host: str, user: str, password: str, directory_dest: str):
        self.host = host
        self.user = user
        self.password = password
        self.project_dist = directory_dest

    def createDecompressScript(self, file_path: str, archive_path: str):
        script = \
            f"""<?php
            echo "decompression...\\n";
            shell_exec('tar -xf {archive_path}');
            echo "decompression successfully!!!";
        ?>
        """
        with open(file_path, 'w') as file:
            file.write(script)

    def deployProject(self, project_path: str):
        project_path = os.path.normpath(project_path)
        dist_tmp = os.path.join(self.dist_tmp, os.path.basename(project_path))
        if not os.path.exists(dist_tmp):
            os.makedirs(dist_tmp)

        compressed_project_path = self.compression.compressProject(project_path, dist_tmp)
        compressed_project = os.path.basename(compressed_project_path)

        to_send_path = os.path.dirname(compressed_project_path)
        script_local_path = os.path.join(to_send_path, 'decompress.php')
        self.createDecompressScript(script_local_path, compressed_project)
        t = script_local_path.split('/')
        script_remote_path = os.path.join(t[-2], t[-1])

        self.ftp.connectFTP(self.host, self.user, self.password)
        self.ftp.send(os.path.dirname(compressed_project_path), self.project_dist)
        self.ftp.disconnectFTP()

        self.decompressDeployedProject(script_remote_path)

    def decompressDeployedProject(self, script: str):
        try:
            r = requests.get(f'http://192.168.200.136/golllum/{script}')
        except Exception as e:
            print(e)
        # pass
