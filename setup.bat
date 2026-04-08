@echo off
python -m pip install --upgrade pip
pip install setuptools
python setup.py install
echo Les dependances ont ete installees avec succes !
pause