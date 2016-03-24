#!/usr/bin/env python
# -*- coding: utf-8 -*-

"""
test_syncer
----------------------------------

Tests and examples
"""

import asyncio

import pytest

from syncer import sync


def test_wrap_async():
    async def a():
        return 1
    b = sync(a)
    assert b() == 1

def test_wrap_async_args():
    async def a(b, c, d=2):
        return d
    b = sync(a)
    assert b(1, 2) == 2
    assert b(1, 2, 3) == 3

def test_deco_async():
    @sync
    async def a():
        return 1
    assert a() == 1

def test_deco_async_args():
    @sync
    async def a(b, c, d=2):
        return d
    assert a(1, 2) == 2
    assert a(1, 2, 3) == 3

@sync
async def test_deco_testmethod():
    async def a():
        return 1
    b = await a()
    assert b == 1

@pytest.mark.xfail(strict=True, raises=AssertionError)
@sync
async def test_failure():
    '''This test must fail.
    Without the @sync decorator, this test passes unexpectedly.
    '''
    assert False

def test_wrap_method():
    class A:
        async def a(self):
            return 1
    a = A()
    sync_a = sync(a.a)
    assert sync_a() == 1

def test_wrap_method_args():
    class A:
        async def a(self, b, c, d=2):
            return d
    a = A()
    sync_a = sync(a.a)
    assert sync_a(1, 2) == 2
    assert sync_a(1, 2, 3) == 3

def test_deco_method():
    class A:
        @sync
        async def a(self):
            return 1
    a = A()
    assert a.a() == 1

def test_deco_method_args():
    class A:
        @sync
        async def a(self, b, c, d=2):
            return d
    a = A()
    assert a.a(1, 2) == 2
    assert a.a(1, 2, 3) == 3

def test_wrap_aioco():
    @asyncio.coroutine
    def a():
        return 1
    b = sync(a)
    assert b() == 1

def test_deco_aioco():
    @sync
    @asyncio.coroutine
    def a():
        return 1
    assert a() == 1

def test_coro():
    async def a():
        return 1
    assert sync(a()) == 1

def test_coro_aioco():
    @asyncio.coroutine
    def a():
        yield from asyncio.sleep(0.0)
        return 1
    assert sync(a()) == 1

def test_func_error():
    def a():
        return 1
    with pytest.raises(TypeError):
        sync(a)
    with pytest.raises(TypeError):
        sync(a())

def test_gen_error():
    def a():
        yield 1
    with pytest.raises(TypeError):
        sync(a)
    with pytest.raises(TypeError):
        sync(a())


if __name__ == '__main__':
    import sys
    sys.exit(pytest.main())
