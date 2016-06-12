# -*- coding: utf-8 -*-

from BaseHTTPServer import HTTPServer, BaseHTTPRequestHandler
from SocketServer import ThreadingMixIn
import os.path
from urlparse import parse_qs, urlparse


class Handler(BaseHTTPRequestHandler):

    def do_GET(self):
        self.send_response(200)
        self.end_headers()
        self.wfile.write(self.get_server_result())
        return

    def get_factors(self, x):
        result = []
        for i in range(1, x + 1):
            if x % i == 0:
                result.append(str(i))
        return result


    def get_server_result(self):
        ''' Обрабатываем Запросы  '''
        file_name = 'index.html'
        params = parse_qs(urlparse(self.path).query, keep_blank_values=True)

        if 'number' in params:
            number = params['number'][0]
            return ', '.join(self.get_factors(int(number)))

        if os.path.isfile(file_name):
            with open(file_name) as index_file:
                return index_file.read()


class ThreadedHTTPServer(ThreadingMixIn, HTTPServer):
    HOST = 'localhost'
    PORT = 8080

def run_server():
    server = ThreadedHTTPServer((ThreadedHTTPServer.HOST, ThreadedHTTPServer.PORT), Handler)
    print('Сервер ... http://{}:{}, нажмите <Ctrl-C> чтобы остановить его').format(server.HOST, server.PORT)
    server.serve_forever()


if __name__ == '__main__':
    run_server()
