from ch02.classpath.Entry import Entry
import os.path
import zipfile


class DirEntry(Entry):
    def __init__(self, path):
        self.absPath = os.path.abspath(path)

    # 从ZIP文件中提取class文件，返回16进制格式的数据
    def read_class(self, class_name):
        error, data = None, None
        file_path = os.path.join(self.absPath, class_name)
        try:
            data = open(file_path, 'rb').read()
        except IOError as e:
            error = e
            return None, None, error
        return data, self, error

    def __str__(self):
        return self.absPath
