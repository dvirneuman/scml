# scml

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
    