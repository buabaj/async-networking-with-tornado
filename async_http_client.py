from tornado import gen
from tornado.ioloop import IOLoop
from tornado.httpclient import AsyncHTTPClient
import ssl
ssl._create_default_https_context = ssl._create_unverified_context


@gen.coroutine
def async_fetch_gen():
    http_client = AsyncHTTPClient()
    response = yield http_client.fetch('http://oval.so')
    raise gen.Return(response.body)


if __name__ == '__main__':
    IOLoop.current().run_sync(async_fetch_gen)
