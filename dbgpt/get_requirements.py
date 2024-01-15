import platform
import socket
import sys
import subprocess
import multiprocessing
import os


def __get_git_root():
    """获取项目的根目录"""
    # 获取当前目录
    try:
        cwd = os.getcwd()
    # 返回包含.git的目录
        while cwd != '/':
            if '.git' in os.listdir(cwd):
                return cwd
            else:
                cwd = os.path.dirname(cwd)
        return cwd
    except Exception as e:
        print(f"An error occurred when getting root working directory: {e}")
        return None


def get_reqs() -> str:
    """调用pipreqs获取当前项目根目录下的全部Python环境，是1个很长的、带换行的文件列表，建议后续存储在swanlog目录下"""
    try:
        rwd=__get_git_root()
        result = subprocess.run(["pipreqs", "--print", "--encoding=utf8",rwd], stdout=subprocess.PIPE, text=True)
         # 检查命令是否成功运行
        if result.returncode == 0:
            return result.stdout
        else:
            print(f"An error occurred when getting requirements:{result.stderr}")
            return None
    except Exception as e:
        print(f"An error occurred: {e}")
        return None



if __name__ == '__main__':

   p=get_reqs()  # pragma: no cover
   
   print("输出的结果是")
   print(__get_git_root())
   print(os.getcwd())
   print(p)
   
   