# scml

## scml website
https://scml.cs.brown.edu/

## details and rules
http://www.yasserm.com/scml/scml2020.pdf
http://web.tuat.ac.jp/~katfuji/ANAC2020/cfp/scml_cfp.pdf

## strategy doc
https://docs.google.com/document/d/1Ip_anncBNpUhVasV7ClLyWpnM8BCL5sT04_5sp7GBdQ/edit?ts=5e80bd61

## tutorials
https://www.youtube.com/playlist?list=PLqvs51K2Mb8IJe5Yz5jmYrRAwvIpGU2nF
http://www.yasserm.com/scml/scml2020docs/tutorials.html

## example agent

create virtual environment

```python3 -m venv venv```

activate it:

```source venv/bin/activate```

try installing using:

```pip install scml```

for me the PyQt5 package at pypi server is broken,
if you get an error about it, run:

```pip install PyQt5==5.14 && pip install scml```

download and run test agent:

```bash
wget www.yasserm.com/scml/scml2020.zip
unzip scml2020.zip
python scml2020/myagent/myagent.py
```
