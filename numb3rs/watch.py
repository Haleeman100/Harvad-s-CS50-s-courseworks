"""
In a file called watch.py, implement a function called parse that expects a str of HTML as input, 
extracts any YouTube URL that’s the value of a src attribute of an iframe element therein, and
returns its shorter, shareable youtu.be equivalent as a str. Expect that any such URL will be in 
one of the formats below. Assume that the value of src will be surrounded by double quotes. 
And assume that the input will contain no more than one such URL. If the input does not contain
any such URL at all, return None.
"""
#<iframe src="http://www.youtube.com/embed/xvFZjo5PgG0"></iframe>
import re

def main():
    s = input("HTML: ").strip()
    r = parse(s)
    print(r)

def parse(s):
    iframe_pattern = r'<iframe[^>]*src="https?://(?:www\.)?youtube\.com/embed/([^"]*)"[^>]*>'
    matches = re.search(iframe_pattern, s, re.IGNORECASE)
    if matches:
        capture = matches.group(1)
        #youtu_be_url = re.sub(r'www\.youtube\.com/', 'https://youtu.be/', youtube_code)
        short_url = f"https://youtu.be/{capture}"
        return short_url
    else:
        return None
    ...


...

if __name__ == "__main__":
    main()
