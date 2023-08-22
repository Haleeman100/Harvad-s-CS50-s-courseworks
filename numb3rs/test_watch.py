import pytest

from watch import parse


def test_valid_youtube_links():
    assert parse("") is True