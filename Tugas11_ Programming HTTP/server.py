from http.server import HTTPServer, BaseHTTPRequestHandler

class CustomHandler(BaseHTTPRequestHandler):
    def do_GET(self):
        self.send_response(200)
        self.send_header('Content-type','text/html')
        self.end_headers()
        self.wfile.write("Hello from server!".encode())

httpd = HTTPServer(('localhost', 8000), CustomHandler)
print("Server running on port 8000...")
httpd.serve_forever()
