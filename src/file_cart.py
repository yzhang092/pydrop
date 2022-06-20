import asyncio
import os
import aiofiles
import aiohttp





class FileCart:
    def __init__(self,filelist):
        self._filelist = filelist
        self._clientDir = './clientDir/'
        self._base_file_url = 'http://localhost:5000/fetch/'

    async def fetch_and_save(self, file, session):
        async with session.get(self._base_file_url + file, timeout=None) as resp:
            async with aiofiles.open(os.path.join(self._clientDir, str(file)), mode='wb') as f:
                await f.write(await resp.content.read())
                await f.close()

    # Return the file name list that needed to be transferred
    def find_missing_file(self):
        if not os.path.exists(self._clientDir):
            os.mkdir(self._clientDir)

        fileList = os.listdir(self._clientDir)
        file_to_fetch = list(set(self._filelist) - set(fileList))
        return file_to_fetch

    # Calling API to fetch files with asynchronous method
    async def fetch_missing(self):
        missing_files = self.find_missing_file()
        async with aiohttp.ClientSession() as session:
            task_list = []
            for file in missing_files:
                task = asyncio.create_task(
                    self.fetch_and_save(file, session)
                )
                task_list.append(task)
            await asyncio.gather(*task_list)

    def get_client_file_list(self):
        if not os.path.exists(self._clientDir):
            os.mkdir(self._clientDir)

        file_list = os.listdir(self._clientDir)
        return file_list


