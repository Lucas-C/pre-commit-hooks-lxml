[![](https://travis-ci.org/Lucas-C/pre-commit-hooks-lxml.svg?branch=master)](https://travis-ci.org/Lucas-C/pre-commit-hooks-lxml)

Useful [pre-commit](http://pre-commit.com) hooks to check your CSS / HTML pages / templates.


## Usage

```
-   repo: https://github.com/Lucas-C/pre-commit-hooks-lxml
    sha: v1.0.2
    hooks:
    -   id: forbid-html-img-without-alt-text
    -   id: forbid-non-std-html-attributes
    -   id: detect-missing-css-classes
        args:
        - --css-files-dir
        - .
        - --html-files-dir
        - .
```


## Dependencies

Under [Cygwin](//www.cygwin.com), with [apt-cyg](//github.com/transcode-open/apt-cyg):

    apt-cyg install git python3 gcc-g++ python3-devel libxml2-devel libxslt-devel

With [MSYS2](//msys2.github.io) :

    pacman -S git python3 gcc python3-devel libxml2-devel libxslt-devel tar

The package names must be very similar under Linux.
