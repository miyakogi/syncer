#!/usr/bin/env python
# -*- coding: utf-8 -*-

"""
test_syncer
----------------------------------

Tests and examples
"""

import asyncio
import unittest

from xfail import xfail

from syncer import sync


class TestSyncer(unittest.TestCase):
    def test_wrap_async(self):
        async def a():
            return 1
        b = sync(a)
        self.assertEqual(b(), 1)

    def test_wrap_async_args(self):
        async def a(b, c, d=2):
            return d
        b = sync(a)
        self.assertEqual(b(1, 2), 2)
        self.assertEqual(b(1, 2, 3), 3)

    def test_deco_async(self):
        @sync
        async def a():
            return 1
        self.assertEqual(a(), 1)

    def test_deco_async_args(self):
        @sync
        async def a(b, c, d=2):
            return d
        self.assertEqual(a(1, 2), 2)
        self.assertEqual(a(1, 2, 3), 3)

    @sync
    async def test_deco_testmethod(self):
        async def a():
            return 1
        b = await a()
        self.assertEqual(b, 1)

    @xfail(AssertionError, strict=True)
    @sync
    async def test_failure(self):
        '''This test must fail.
        Without the @sync decorator, this test passes unexpectedly.
        '''
        assert False

    def test_wrap_method(self):
        class A:
            async def a(self):
                return 1
        a = A()
        sync_a = sync(a.a)
        self.assertEqual(sync_a(), 1)

    def test_wrap_method_args(self):
        class A:
            async def a(self, b, c, d=2):
                return d
        a = A()
        sync_a = sync(a.a)
        self.assertEqual(sync_a(1, 2), 2)
        self.assertEqual(sync_a(1, 2, 3), 3)

    def test_deco_method(self):
        class A:
            @sync
            async def a(self):
                return 1
        a = A()
        self.assertEqual(a.a(), 1)

    def test_deco_method_args(self):
        class A:
            @sync
            async def a(self, b, c, d=2):
                return d
        a = A()
        self.assertEqual(a.a(1, 2), 2)
        self.assertEqual(a.a(1, 2, 3), 3)

    def test_wrap_aioco(self):
        @asyncio.coroutine
        def a():
            return 1
        b = sync(a)
        self.assertEqual(b(), 1)

    def test_deco_aioco(self):
        @sync
        @asyncio.coroutine
        def a():
            return 1
        self.assertEqual(a(), 1)

    def test_coro(self):
        async def a():
            return 1
        self.assertEqual(sync(a()), 1)

    def test_coro_aioco(self):
        @asyncio.coroutine
        def a():
            yield from asyncio.sleep(0.0)
            return 1
        self.assertEqual(sync(a()), 1)

    def test_func_error(self):
        def a():
            return 1
        with self.assertRaises(TypeError):
            sync(a)
        with self.assertRaises(TypeError):
            sync(a())

    def test_gen_error(self):
        def a():
            yield 1
        with self.assertRaises(TypeError):
            sync(a)
        with self.assertRaises(TypeError):
            sync(a())
