import os
import numpy as np
import time


class FileEngine:
    def __init__(self, count):
        # Default dir for the generated files
        self._filedir_path = './engineDir/'

        # Number of file to be generated
        self._count = count

    # Create the files to be transferred
    def start(self):
        # Check if Dir exists, if not, creat one.
        if not os.path.exists(self._filedir_path):
            os.mkdir(self._filedir_path)

        # start creating files into it
        for index in range(0, self._count):
            f = open(os.path.join(self._filedir_path, str(index)), "wb")
            f.write(bytes(os.urandom(1024 * np.random.randint(1, 1000))))
            f.close()
            time.sleep(np.random.randint(1, 1000) / 1000)

    # Return the list of files generated in the folder.
    def status(self):
        fileList = os.listdir(self._filedir_path)
        return fileList