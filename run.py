import http.server
import socketserver
import sys
import os

PORT = 8000
Handler = http.server.SimpleHTTPRequestHandler

os.chdir(os.path.dirname(os.path.abspath(__file__)))

if "darwin" in sys.platform :
    print("OS is macOS")
    os.system("open http://localhost:%d" % PORT)
elif "win" in sys.platform :
    print("OS is win")
    os.system("start http://localhost:%d" % PORT)
else:
    print("未実装")

with socketserver.TCPServer(("", PORT), Handler) as httpd:
    print("serving at port", PORT)
    httpd.serve_forever()
