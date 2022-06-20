from aiohttp import web
import aiohttp_jinja2
import jinja2
from src.file_sender import FileSender

routes = web.RouteTableDef()


# The only purpose of this server is to send file
@routes.get('/fetch/{filename}')
async def hello(request):
    filename = request.match_info['filename']
    send_file = FileSender(filename, request)
    await send_file.send_file()


app = web.Application()
app.add_routes(routes)
aiohttp_jinja2.setup(app, loader=jinja2.FileSystemLoader('./templates'))
web.run_app(app)
