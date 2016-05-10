#!/usr/bin/env python3
# -*- coding: utf-8 -*-

import sys
import functools
import asyncio
import inspect
import types


PY35 = sys.version_info >= (3, 5)


def _is_awaitable(co):
    if PY35:
        return inspect.isawaitable(co)
    else:
        return isinstance(co, types.GeneratorType)


@functools.singledispatch
def sync(co):
    raise TypeError('Called with unsupported argument: {}'.format(co))


@sync.register(types.GeneratorType)
def sync_co(co):
    if not _is_awaitable(co):
        raise TypeError('Called with unsupported argument: {}'.format(co))
    return asyncio.get_event_loop().run_until_complete(co)


@sync.register(types.FunctionType)
@sync.register(types.MethodType)
def sync_fu(f):
    if not asyncio.iscoroutinefunction(f):
        raise TypeError('Called with unsupported argument: {}'.format(f))

    @functools.wraps(f)
    def run(*args, **kwargs):
        return asyncio.get_event_loop().run_until_complete(f(*args, **kwargs))
    return run


if PY35:
    sync.register(types.CoroutineType)(sync_co)
