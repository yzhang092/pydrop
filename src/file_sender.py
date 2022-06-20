import aiofiles
from aiofiles.os import stat as aio_stat
import os
from multidict import CIMultiDict
import datetime
from aiohttp import web


def to_UTC_string(a: float):
    return datetime.datetime.utcfromtimestamp(a).strftime('%a, %d %b %Y %H:%M:%S GMT')


class FileSender:
    def __init__(self, file, request):
        self._filename = file
        self._filedir_path = './engineDir/'
        self._request = request

    async def file_stats(self):
        r = await aio_stat(os.path.join(self._filedir_path, self._filename))
        return r.st_mtime, r.st_size

    async def set_header(self):
        file_st_mtime, file_st_size = await self.file_stats()
        return_headers = CIMultiDict()
        return_headers['Content-Length'] = str(file_st_size)
        return_headers['Last-Modified'] = to_UTC_string(file_st_mtime)
        return_headers['Cache-Control'] = ', '.join(['max-age=0', ])
        return return_headers

    # Set response header and stream write to the other server
    async def send_file(self):
        return_headers = await self.set_header()
        file_path = os.path.join(self._filedir_path, self._filename)
        read_step = 1024
        resp = web.StreamResponse(status=200, headers=return_headers)
        await resp.prepare(self._request)
        async with aiofiles.open(file_path, mode='rb', buffering=True) as f:
            while True:
                b = await f.read(read_step)
                if b:
                    await resp.write(b)
                else:
                    break
        return resp
