import BaseHTTPServer


HOST_NAME = "localhost"
PORT_NUMBER = 8080


class MyHandler(BaseHTTPServer.BaseHTTPRequestHandler):
	def do_HEAD(s):
		s.send_response(418)
		s.send_header("Content-type", "text/html")
		s.end_headers()
	def do_GET(s):
		s.send_response(418)
		s.send_header("Content-type", "text/html")
		s.end_headers()
		s.wfile.write("<html><head><title></title></head>")
		s.wfile.write("<body><p>ERROR: 418 I'm a teapot</p>")
		s.wfile.write("</body></html>")

if __name__ == '__main__':
	server_class = BaseHTTPServer.HTTPServer
	httpd = server_class((HOST_NAME, PORT_NUMBER), MyHandler)
	try:
		httpd.serve_forever()
	except KeyboardInterrupt:
		pass
	httpd.server_close()
