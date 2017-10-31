# pylint:disable=invalid-name
from __future__ import absolute_import
from __future__ import unicode_literals

from pre_commit_hooks.html_tags_blacklist import main as html_tags_blacklist

DEFAULT_FORBIDDEN_TAGS = 'basefont,blink,center,font,marquee,s,strike,tt,u'


def test_detect_forbidden(tmpdir):
    html_path = tmpdir.join('file.html')
    html_path.write('''<!DOCTYPE html>
<html lang="en">
  <head>
    <meta charset="utf-8">
    <meta http-equiv="x-ua-compatible" content="ie=edge">
    <meta name="viewport" content="width=device-width, initial-scale=1, shrink-to-fit=no">
    <title>Page Title</title>
  </head>
  <body>
    <blink>ლ(ಠ_ಠლ)</blink>
  </body>
</html>''')
    assert html_tags_blacklist([
        '--forbidden-tags', DEFAULT_FORBIDDEN_TAGS,
        str(html_path)
    ]) == 1

def test_pass_valid(tmpdir):
    html_path = tmpdir.join('file.html')
    html_path.write('''<!DOCTYPE html>
<html lang="en">
  <head>
    <meta charset="utf-8">
    <meta http-equiv="x-ua-compatible" content="ie=edge">
    <meta name="viewport" content="width=device-width, initial-scale=1, shrink-to-fit=no">
    <title>Page Title</title>
  </head>
  <body>
    <h1>ლ(ಠ_ಠლ)</h1>
  </body>
</html>''')
    assert html_tags_blacklist([
        '--forbidden-tags', DEFAULT_FORBIDDEN_TAGS,
        str(html_path)
    ]) == 0
