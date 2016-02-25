#!/usr/bin/env python3
# -*- coding: utf-8 -*-

import functools
import asyncio
import inspect
from types import FunctionType, MethodType, CoroutineType, GeneratorType

__author__ = 'Hiroyuki Takagi'
__email__ = 'miyako.dev@gmail.com'
__version__ = '0.1.0'


@functools.singledispatch
def sync(co):
    raise TypeError('Called with unsupported argument: {}'.format(co))


@sync.register(GeneratorType)
@sync.register(CoroutineType)
def sync_co(co):
    if not inspect.isawaitable(co):
        raise TypeError('Called with unsupported argument: {}'.format(co))
    return asyncio.get_event_loop().run_until_complete(co)


@sync.register(FunctionType)
@sync.register(MethodType)
def sync_fu(f):
    if not asyncio.iscoroutinefunction(f):
        raise TypeError('Called with unsupported argument: {}'.format(f))
    @functools.wraps(f)
    def run(*args, **kwargs):
        return asyncio.get_event_loop().run_until_complete(f(*args, **kwargs))
    return run
