import os
import shutil

from domain.ftp.IFileOperations import IFileManipulation, IFilePermission, ICompression


class FileManipulation(IFileManipulation):
    @staticmethod
    def createDir(dir_name: str, permission: int):
        os.mkdir(dir_name, permission)

    @staticmethod
    def remove(path: str):
        path = os.path.normpath(path)

        if os.path.isdir(path) and len(os.listdir(path)) > 0:
            for element in os.listdir(path):
                element = os.path.join(path, element)
                FileManipulation.remove(element)
                if len(os.listdir(path)) == 0:
                    os.rmdir(path)
            pass
        elif not os.path.isdir(path):
            os.remove(path)
        else:
            os.rmdir(path)


class FilePermission(IFilePermission):
    permission_code = 0o700

    @staticmethod
    def changePermission(file_path: str, permission: int):
        os.chmod(file_path, permission)


class Compression(ICompression):
    file_manipulation = None
    compressed_project_dist = "project_tmp"
    archive_format = "xztar"
    message = ""

    def __init__(self, file_manipulation: IFileManipulation):
        Compression.file_manipulation = file_manipulation

    @staticmethod
    def compressProject(project_path: str, dist: str = compressed_project_dist):
        if not os.path.exists(dist):
            FileManipulation.createDir(dist, FilePermission.permission_code)

        # FilePermission.changePermission(
        #     Compression.compressed_project_dist,
        #     FilePermission.permission_code
        # )

        if not os.path.exists(project_path):
            raise Exception('No such file or directory')

        compressed_project_name = os.path.basename(os.path.normpath(project_path))
        compressed_project_path = os.path.join(dist, compressed_project_name)

        try:
            res = shutil.make_archive(
                compressed_project_path,
                Compression.archive_format,
                os.path.dirname(project_path),
                compressed_project_name
            )
            Compression.message = "Compression successfully"
            print(Compression.message)
            return res
        except Exception as e:
            Compression.message = e.args
            print(Compression.message)

    @staticmethod
    def decompressProject():
        pass
