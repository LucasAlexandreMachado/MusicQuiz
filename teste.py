from http.server import BaseHTTPRequestHandler, HTTPServer
import json
import random
import webbrowser
import time
import os

class SimpleServer(BaseHTTPRequestHandler):
    def do_GET(self):
        if self.path == '/':
            self.send_response(200)
            self.send_header('Content-type', 'text/html')
            self.end_headers()
            with open("index.html", "rb") as file:
                self.wfile.write(file.read())
        elif self.path.startswith('/random_anime'):
            self.send_response(200)
            self.send_header('Content-type', 'application/json')
            self.end_headers()
            random_anime = random.choice(["Naruto", "One Piece", "Attack on Titan"]) # Aqui você implementará a lógica para buscar um anime aleatório do usuário
            response = {"anime": random_anime}
            self.wfile.write(json.dumps(response).encode())
        else:
            self.send_response(404)
            self.send_header('Content-type', 'text/plain')
            self.end_headers()
            self.wfile.write("404 Not Found".encode())

def play_opening(anime_title):
    query = f"{anime_title} opening"
    url = f"https://www.youtube.com/results?search_query={query}"
    webbrowser.open(url)

def run(server_class=HTTPServer, handler_class=SimpleServer, port=8000):
    server_address = ('', port)
    httpd = server_class(server_address, handler_class)
    print(f"Starting server on port {port}...")
    httpd.serve_forever()

if __name__ == "__main__":
    run()
