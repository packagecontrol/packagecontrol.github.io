#!/usr/bin/env python3

import yaml
from io import StringIO

data_str = """
!!omap
- arrow:
    # is actually on pypi, but tags are not inspired from pypi so no use in showing pypi version
    base: https://github.com/douglas-vaz/arrow
- bz2:
    base: https://github.com/codexns/sublime-bz2
- jinja2:
    pypi: yes
    base: https://bitbucket.org/teddy_beer_maniac/sublime-text-dependency-jinja2
- markupsafe:
    pypi: MarkupSafe
    base: https://bitbucket.org/teddy_beer_maniac/sublime-text-dependency-markupsafe
- oauthlib:
    pypi: yes
- ordereddict:
- paramiko:
    pypi: yes
    base: https://github.com/jlegewie/sublime-paramiko
- PyCrypto:
    pypi: pycrypto
    base: https://github.com/jlegewie/sublime-PyCrypto
- pygments:
    pypi: yes
- pytz:
    pypi: yes
- pyyaml:
    pypi: yes
- requests:
    pypi: yes
- requests-oauthlib:
    pypi: yes
- select-windows:
    base: https://github.com/codexns/sublime-select-windows
- ssl-linux:
    base: no
- ssl-windows:
    base: no
- StyledPopup:
    base: https://github.com/huot25/StyledPopup
- tabulate:
    pypi: yes
"""


data = yaml.load(data_str)
# print(data)

fmt = """\
<tr>
    <td><a href="{base}">{name}</a></td>
    <td>{tag_img}</td>
    <td>{pypi_img}</td>
</tr>
"""
io = StringIO()

for name, info in data:
    # normalize data
    info = info or {}
    base = info.get('base', "https://github.com/packagecontrol/" + name) or ""
    pypi_name = info.get('pypi', False)
    if pypi_name is True:
        pypi_name = name

    if base.startswith("https://github.com/"):
        # only supported for github, not bitbucket
        _, org, repo = base.rsplit('/', 2)
        tag_img = '<img src="https://img.shields.io/github/tag/{org}/{repo}.svg" />'.format(org=org, repo=repo)
    else:
        tag_img = ""

    if pypi_name:
        pypi_img = '<img src="https://img.shields.io/pypi/v/{pypi_name}.svg" />'.format(pypi_name=pypi_name)
    else:
        pypi_img = ""

    io.write(fmt.format(**locals()))

print(io.getvalue())
