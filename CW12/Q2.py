from http.server import HTTPServer , SimpleHTTPRequestHandler

def run(server_class=HTTPServer, handler_class=SimpleHTTPRequestHandler):
    server_address = ('', 1080 )
    httpd = server_class(server_address, handler_class)
    httpd.serve_forever()

run()

#http://www.youtube.com/watch?v=DeFST8tvtuI