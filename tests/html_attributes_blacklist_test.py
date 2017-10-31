# coding: utf8
# pylint:disable=invalid-name
from __future__ import absolute_import
from __future__ import unicode_literals

from pre_commit_hooks.html_attributes_blacklist import main as html_attributes_blacklist

DEFAULT_FORBIDDEN_ATTRS = 'align,alink,background,basefont,bgcolor,border,color,link,text,vlink'


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
    <p color="red">ლ(ಠ_ಠლ)</p>
  </body>
</html>'''.encode('utf8'), mode='wb')
    assert html_attributes_blacklist([
        '--forbidden-attributes', DEFAULT_FORBIDDEN_ATTRS,
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
    <p style="color: red">ლ(ಠ_ಠლ)</p>
  </body>
</html>'''.encode('utf8'), mode='wb')
    assert html_attributes_blacklist([
        '--forbidden-attributes', DEFAULT_FORBIDDEN_ATTRS,
        str(html_path)
    ]) == 0
