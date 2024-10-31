import os.path
from classpath.Entry import Entry
from classpath.WildcardEntry import WildcardEntry

class ClassPath:
    def __init__(self):
        self.boot_classpath = None
        self.ext_classpath = None
        self.user_classpath = None

    @staticmethod
    def parse(jre_option, cp_option):
        cp = ClassPath()
        cp.parse_boot_ext_classpath(jre_option)
        cp.parse_user_classpath(cp_option)
        return cp

    @staticmethod
    def __exists(path):
        if os.path.isdir(path):
            return True
        return False

    @staticmethod
    def __get_jre_dir(jre_option):
        if jre_option and ClassPath.__exists(jre_option):
            return jre_option

        if ClassPath.__exists("./jre"):
            return "./jre"

        java_home = os.environ.get("JAVA_HOME")
        if java_home and ClassPath.__exists(java_home):
            return os.path.join(java_home, "jre")

        raise RuntimeError("Can not find jre folder!")


    def parse_boot_ext_classpath(self, jre_option):

        jre_path = ClassPath.__get_jre_dir(jre_option)

        jre_lib_path = os.path.join(jre_path, "lib", "*")
        self.boot_classpath = WildcardEntry(jre_lib_path)

        jre_ext_path = os.path.join(jre_path, "lib", "ext", "*")
        self.ext_classpath = WildcardEntry(jre_ext_path)

    def parse_user_classpath(self, cp_option):

        if not cp_option or not ClassPath.__exists(cp_option):
            cp_option = "."
        self.user_classpath = Entry.new_entry(cp_option)

    def read_class(self, class_name):
        global data, entry, error
        class_name = class_name + ".class"
        if self.boot_classpath:
            data, entry, error = self.boot_classpath.read_class(class_name)
            if not data and self.ext_classpath:
                data, entry, error = self.ext_classpath.read_class(class_name)
                if not data and self.user_classpath:
                    return self.user_classpath.read_class(class_name)
        return data, entry, error

    def __str__(self):
        return self.user_classpath.__str__()