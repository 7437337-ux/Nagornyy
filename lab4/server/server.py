#!/usr/bin/env python3
import http.server
import socketserver

handler = http.server.SimpleHTTPRequestHandler

with socketserver.TCPServer(("", 1234), handler) as httpd:
    print("Server started on port 1234...")
    httpd.serve_forever()
