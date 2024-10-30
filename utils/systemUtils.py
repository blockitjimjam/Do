import os
import sys
class SystemUtils:
    @staticmethod
    def add_to_sys_path(dir_path):
        abs_path = os.path.abspath(dir_path)
        if abs_path not in sys.path:
            sys.path.append(abs_path)
            print(f"Added {abs_path} to sys.path")
        else:
            print(f"{abs_path} is already in sys.path")
