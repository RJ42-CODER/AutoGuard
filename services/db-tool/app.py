from http.server import BaseHTTPRequestHandler, HTTPServer

class Handler(BaseHTTPRequestHandler):
    def do_GET(self):
        if self.path == "/health":
            self.send_response(200)
            self.end_headers()
            self.wfile.write(b"DB tool service is healthy")
        else:
            self.send_response(404)
            self.end_headers()

server = HTTPServer((
    "0.0.0.0",
    8000
),Handler)
print("[DB Tool] on port 8000...")
server.serve_forever()
