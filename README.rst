Syncer
======

.. image:: https://img.shields.io/pypi/v/syncer.svg
        :target: https://pypi.python.org/pypi/syncer

.. image:: https://img.shields.io/pypi/pyversions/syncer.svg
        :target: https://pypi.python.org/pypi/syncer

.. image:: https://img.shields.io/travis/miyakogi/syncer.svg
        :target: https://travis-ci.org/miyakogi/syncer

.. image:: https://codecov.io/github/miyakogi/syncer/coverage.svg?branch=master
    :target: https://codecov.io/github/miyakogi/syncer?branch=master


Syncer is an async-to-sync converter for python.

* PyPI: https://pypi.python.org/pypi/syncer/
* Documentation: https://miyakogi.github.io/syncer/
* Source code: https://github.com/miyakogi/syncer/

Features
========

Sometimes (mainly in test) we need to convert asynchronous functions to normal,
synchronous functions and run them synchronously. It can be done by
``ayncio.get_event_loop().run_until_complete()``, but it's quite long...

Syncer makes this conversion easy.

* Convert coroutine-function (defined by ``aync def``) to normal (synchronous) function
* Run coroutines synchronously
* Support both ``async def`` and decorator (``@asyncio.coroutine``) style

Install
=======

At the command line::

    $ pip install syncer

Usage
=====

This module has only one function: ``syncer.sync``.

.. code-block:: py

    from syncer import sync
    async def async_fun():
        ...
        return 1
    b = sync(async_fun)  # now b is synchronous
    assert 1 == b()

To test the above ``async_fun`` in asynchronous test functions:

.. code-block:: py

    import unittest

    class TestA(unittest.TestCase):
        # ``sync`` can be used as decorator.
        # The decorated function becomes synchronous.
        @sync
        async def test_async_fun(self):
            self.assertEqual(await async_fun(), 1)

Or, keep test functions synchronous and get results synchronously:

.. code-block:: py

    class TestA(unittest.TestCase):
        def test_async_fun(self):
            # run coroutine and return the result
            self.assertEqual(sync(async_fun()), 1)
            # This is equivalent to below, just a shortcut
            self.assertEqual(
                asyncio.get_event_loop().run_until_complete(async_fun()), 1)

More examples/use-cases will be found in `test <https://github.com/miyakogi/syncer/blob/master/test_syncer.py>`_.

License
=======

`MIT license <https://github.com/miyakogi/syncer/blob/master/LICENSE>`_

Credits
=======

This package was created with Cookiecutter_ and the `audreyr/cookiecutter-pypackage`_ project template.

.. _Cookiecutter: https://github.com/audreyr/cookiecutter
.. _`audreyr/cookiecutter-pypackage`: https://github.com/audreyr/cookiecutter-pypackage
