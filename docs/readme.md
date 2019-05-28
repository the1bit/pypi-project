Empty example PYPI package by The1bit
--------------------------------------

Change log 
----------

* version 0.0.1.9
    * Basic unittest for Core module
* version 0.0.1.6
    * Execute this from command-line (pypr -v)
* version 0.0.0.1
    * Init files and directory structure



Requirements
------------

* Linux OS or Windows OS
* Python (2.7)


Basic install
-------------

pip install pypi-project --upgrade

(install without cache: pip install pypi-project --no-cache-dir  )


You can find the detailed documentation in https://github.com/the1bit/pypi-project.

Usage
-----

## From command line

```
pypr -v
```
Result: 

```


## From Python

```
import pypiproject
```

Known issues
------------

* **Permission denied on /usr/bin/pypr**
Sometimes you are facing the following issue when you execute the **pypr** command:

```bash
-bash: /usr/bin/pypr: Permission denied
```

Solution to execute the following command:

```
sudo chmod +x /usr/bin/pypr
```

* **Command not found on /usr/bin/pypr**
Although the package is well prepared sometimes you are facing the following issue after a package update when you execute the **pypr** command:

```
    /usr/bin/pypr: line 2: $'\r': command not found
    /usr/bin/pypr: line 19: syntax error: unexpected end of file
```

Solution to execute the following command:

```
    sudo dos2unix /usr/bin/pypr
```


LICENSE
-------

Copyright (c) 2019

Permission is hereby granted, free of charge, to any person obtaining a copy of
this software and associated documentation files (the "Software"), to deal in
the Software without restriction, including without limitation the rights to
use, copy, modify, merge, publish, distribute, sublicense, and/or sell copies
of the Software, and to permit persons to whom the Software is furnished to do
so, subject to the following conditions:

The above copyright notice and this permission notice shall be included in all
copies or substantial portions of the Software.

THE SOFTWARE IS PROVIDED "AS IS", WITHOUT WARRANTY OF ANY KIND, EXPRESS OR
IMPLIED, INCLUDING BUT NOT LIMITED TO THE WARRANTIES OF MERCHANTABILITY,
FITNESS FOR A PARTICULAR PURPOSE AND NONINFRINGEMENT. IN NO EVENT SHALL THE
AUTHORS OR COPYRIGHT HOLDERS BE LIABLE FOR ANY CLAIM, DAMAGES OR OTHER
LIABILITY, WHETHER IN AN ACTION OF CONTRACT, TORT OR OTHERWISE, ARISING FROM,
OUT OF OR IN CONNECTION WITH THE SOFTWARE OR THE USE OR OTHER DEALINGS IN THE
SOFTWARE.
