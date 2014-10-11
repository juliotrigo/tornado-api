# -*- coding: utf-8 -*-

"""Tornado HTTP server."""

from tornado.ioloop import IOLoop
from tornado.web import RequestHandler, Application, url
from tornado.httpserver import HTTPServer


class MainHandler(RequestHandler):
    def get(self):
        self.write("Hello, world: get")

    def post(self):
        self.write("Hello, world: post")


def make_app():
    return Application([
        url(r"/", MainHandler),
        ])


def main():
    app = make_app()
    http_server = HTTPServer(app)
    http_server.listen(8888)
    IOLoop.instance().start()

if __name__ == "__main__":
    main()
