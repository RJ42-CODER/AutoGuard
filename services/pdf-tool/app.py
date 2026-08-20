from http.server import BaseHTTPRequestHandler, HTTPServer
from urllib.parse import urlparse,parse_qs
import subprocess


class Handler(BaseHTTPRequestHandler):

    def do_GET(self):
        parsed = urlparse(self.path)

        if parsed.path == "/health":
            self.send_response(200)
            self.end_headers()
            self.wfile.write(b"PDF tool service is healthy")
            return 
        
        if parsed.path == "/convert":
            params = parse_qs(parsed.query)
            filename = params.get("file",["document.pdf"])[0]

            result = subprocess.run(
                f"echo Converting {filename}",
                shell = True,
                capture_output = True,
                text=True
            )

            self.send_response(200)
            self.end_headers()
            self.wfile.write(result.stdout.encode())
            return

        self.send_response(404)
        self.end_headers()


server = HTTPServer(("0.0.0.0",8000),Handler)
print("[PDF Tool] on port 8000...")
server.serve_forever()
