# feedlink

## Usage

You can try feedlink before install if the PYTHONPATH is extended with the 
src directory

```bash
PYTHONPATH=./src:$PYTHONPATH ./bin/feedlink < doc.html > link.json
```

## Install

```bash
python setup.py install
```

## Test

Run all the test

```bash
python -m unittest discover -s test -p test_*.py
```

