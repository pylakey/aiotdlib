from typing import Any

import pytest
from pytest_asyncio import is_async_test

from shared_client import authorizer, client

__all__ = ['authorizer', 'client']


# https://github.com/pytest-dev/pytest-asyncio/issues/983
def pytest_collection_modifyitems(items: Any) -> None:
    """
    Make all tests run on the same event loop.

    This is necessary because our TDLib needs to be configured/authenticated
    as a fixture from the same event loop where we send messages within a test,
    otherwise the update thread hangs.
    See: https://pytest-asyncio.readthedocs.io/en/latest/how-to-guides/run_session_tests_in_same_loop.html
    """
    pytest_asyncio_tests = (item for item in items if is_async_test(item))
    session_scope_marker = pytest.mark.asyncio(loop_scope="session")
    for async_test in pytest_asyncio_tests:
        async_test.add_marker(session_scope_marker, append=False)
