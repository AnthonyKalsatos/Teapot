import BaseHTTPServer
from mimetypes import types_map
import os


HOST_NAME = "localhost"
PORT_NUMBER = 8080
mimtypes.init()


class MyHandler(BaseHTTPServer.BaseHTTPRequestHandler):
	def do_HEAD(s):
		s.send_response(200)
		s.send_header("Content-type", "text/html")
		s.end_headers()
	def do_GET(s):
		fname, ext = os.path.splitext(s.path)
		if s.path == "/":
			s.send_response(418)
			s.send_header("Content-type", "text/html")
			s.path = "/index.html"
		elif ext in (".html", ".css", ".js"):
			s.send_response(200)
			s.send_header('Content-type', mimetypes.types_map[ext])
		s.end_headers()
		f = open(s.path[1:])
		s.wfile.write(f.read())
		f.close()


if __name__ == '__main__':
	server_class = BaseHTTPServer.HTTPServer
	httpd = server_class((HOST_NAME, PORT_NUMBER), MyHandler)
	try:
		httpd.serve_forever()
	except KeyboardInterrupt:
		pass
	httpd.server_close()
