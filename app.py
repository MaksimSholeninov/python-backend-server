import http.server
import socket
import os

class MyHandler(http.server.BaseHTTPRequestHandler):
    def do_GET(self):
        pod_ip = socket.gethostbyname(socket.gethostname())

        self.send_response(200)
        self.send_header("Content-type", "text/plain")
        self.end_headers()

        response = f"Hello! I am a Python backend.\nMy Pod IP is: {pod_ip}\nStatus: 200 OK\n"
        self.wfile.write(response.encode())

if __name__ == "__main__":
    server = http.server.HTTPServer(('0.0.0.0', 8080), MyHandler)
    print("Server started on port 8080...")
    server.serve_forever()