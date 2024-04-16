import os
import shutil

from domain.ftp.IFileOperations import IFileManipulation, IFilePermission, ICompression


class FileManipulation(IFileManipulation):
    @staticmethod
    def createDir(dir_name: str, permission: int):
        os.mkdir(dir_name, permission)


class FilePermission(IFilePermission):
    permission_code = 0o700

    @staticmethod
    def changePermission(file_path: str, permission: int):
        os.chmod(file_path, permission)


class Compression(ICompression):
    file_manipulation = None
    compressed_project_dist = "compressed_dist/"
    archive_format = "xztar"
    message = ""

    def __init__(self, file_manipulation: IFileManipulation):
        Compression.file_manipulation = file_manipulation

    @staticmethod
    def compressProject(project_path: str):
        if not os.path.exists(Compression.compressed_project_dist):
            FileManipulation.createDir(
                Compression.compressed_project_dist,
                FilePermission.permission_code
            )

        # FilePermission.changePermission(
        #     Compression.compressed_project_dist,
        #     FilePermission.permission_code
        # )

        if not os.path.exists(project_path):
            raise Exception('No such file or directory')

        compressed_project_name = os.path.basename(os.path.normpath(project_path))
        compressed_project_path = Compression.compressed_project_dist + compressed_project_name

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
