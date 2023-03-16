import platform
import cpuinfo
import socket
import os


class SystemInfo:
    # Initialisation de la classe avec les infos
    def __init__(self):
        self.system = platform.system() + " " + platform.release()
        self.processor = platform.processor()
        self.hostname = socket.gethostname()
        self.username = os.getlogin()
        self.cpu_brand = cpuinfo.get_cpu_info()['brand_raw']
        self.architecture = platform.architecture()[0]
        self.python_version = platform.python_version()

    def to_dict(self):
        return {
            'system': self.system,
            'processor': self.processor,
            'hostname': self.hostname,
            'username': self.username,
            'cpu_brand': self.cpu_brand,
            'architecture': self.architecture,
            'python_version': self.python_version,
        }
