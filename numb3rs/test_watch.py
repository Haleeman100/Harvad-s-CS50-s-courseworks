import pytest

from watch import parse


def test_valid_youtube_links_http():
    html_input = '<iframe src="http://youtube.com/embed/xvFZjo5PgG0"></iframe>'
    expected_output = 'https://youtu.be/xvFZjo5PgG0'
    assert parse(html_input) == expected_output

def test_valid_youtube_links_https():
    html_input = '<iframe src="https://www.youtube.com/embed/xvFZjo5PgG0"></iframe>'
    expected_output = 'https://youtu.be/xvFZjo5PgG0'
    assert parse(html_input) == expected_output

def test_no_valid_youtube_link():
    html_input = '<iframe src="https://example.com"></iframe>'
    assert parse(html_input) is None

if __name__ == "__main__":
    pytest.main()

