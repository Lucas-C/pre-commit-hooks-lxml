Useful [pre-commit](http://pre-commit.com) hooks to check your HTML pages / templates.

## Usage

```
-   id: forbid-html-img-without-alt-text
-   id: forbid-non-std-html-attributes
```

## Dependencies

Under [Cygwin](//www.cygwin.com), with [apt-cyg](//github.com/transcode-open/apt-cyg):

    apt-cyg install git python3 gcc-g++ python3-devel libxml2-devel libxslt-devel

With [MSYS2](//msys2.github.io) :

    pacman -S git python3 gcc python3-devel libxml2-devel libxslt-devel tar

The package names must be very similar under Linux.
