@echo off
python -m pip install --upgrade pip
pip install setuptools
python setup.py install
echo Les dépendances ont été installées avec succès !
pause