#!/usr/bin/env python3
# -*- coding: utf-8 -*-

import logging; logging.basicConfig(level=logging.INFO)

import asyncio

# aiohttp第三方库：基于asyncio的异步http框架
from aiohttp import web  # 用于实现web服务器


# 不加requests的情况：TypeError: index() takes 0 positional arguments but 1 was given
def index(requests):
    return web.Response(body=b'<h1>Awesome</h1>', content_type='text/html')
    # return web.Response(body=b'<h1>Awesome</h1>', headers={'content-type':'text/html'})


# 初始化web app
@asyncio.coroutine
# @asyncio.coroutine 可以用 async await 写法替换 - python 3.5 以上
# async def init(loop)
def init(loop):
    app = web.AppRunner(loop=loop)  # 创建app对象
    app.router.add_route('GET', '/', index)
    # 调用子协程:创建一个TCP服务器,绑定到"127.0.0.1:9000"socket,并返回一个服务器对象
    # srv = await loop.create_server(app.make_handler(), '127.0.0.1', 9000)
    srv = yield from loop.create_server(app.make_handler(), '127.0.0.1', 9000)
    logging.info('server started at http://127.0.0.1:9000...')
    return srv


loop = asyncio.get_event_loop()  # loop是一个消息循环对象
loop.run_until_complete(init(loop))  # 在消息循环中执行协程
loop.run_forever()


