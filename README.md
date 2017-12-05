[![](https://travis-ci.org/Lucas-C/pre-commit-hooks-lxml.svg?branch=master)](https://travis-ci.org/Lucas-C/pre-commit-hooks-lxml)
[![Known Vulnerabilities](https://snyk.io/test/github/lucas-c/pre-commit-hooks-lxml/badge.svg)](https://snyk.io/test/github/lucas-c/pre-commit-hooks-lxml)

Useful [pre-commit](http://pre-commit.com) hooks to check your CSS / HTML pages / templates.


## Usage

```
-   repo: https://github.com/Lucas-C/pre-commit-hooks-lxml
    sha: v1.1.0
    hooks:
    -   id: forbid-html-img-without-alt-text
    -   id: forbid-non-std-html-attributes
    -   id: detect-missing-css-classes
        args:
        - --css-files-dir
        - .
        - --html-files-dir
        - .
    -   id: html-tags-blacklist
    -   id: html-attributes-blacklist
```

### [FR] Accessibilité RGAA

Les hooks `html-tags-blacklist` & `html-attributes-blacklist` sont configurés par défaut pour interdire les élements et attributs nuisant à l'accessibilité,
selon les recommendations d'[Access42](https://access42.net).

cf. [issue #2](https://github.com/Lucas-C/pre-commit-hooks-lxml/issues/2)


## Dependencies needed to use lxml

Under [Cygwin](//www.cygwin.com), with [apt-cyg](//github.com/transcode-open/apt-cyg):

    apt-cyg install git python3 gcc-g++ python3-devel libxml2-devel libxslt-devel

With [MSYS2](//msys2.github.io) :

    pacman -S git python3 gcc python3-devel libxml2-devel libxslt-devel tar

The package names must be very similar under Linux.
