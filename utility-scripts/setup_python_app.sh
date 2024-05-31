#!/bin/bash
# This will setup the virtual environment for a python project and install the packages for the first time
script_dir="$( cd "$( dirname "${BASH_SOURCE[0]}" )" &> /dev/null && pwd )"
deactivate 2>/dev/null || true
current_dir=$PWD
project_name=$(basename "$current_dir")
rm -rf ~/venvs/"$project_name"
set -e # make sure we exit if this fails, otherwise we may corrupt the main environment
python_exe="${PYTHON:-python3}"
$python_exe -m venv ~/venvs/"$project_name"
source ~/venvs/"$project_name"/bin/activate
set +e
python -m pip install --upgrade pip
pip install --upgrade setuptools
pip install pre-commit
pip install black
pip install pip-tools
pip install ruff

req_installed=0
# install project requirements.txt if it exists
if [ $req_installed = "0" ] && [ -f "requirements.txt" ]; then
    pip install -r requirements.txt
    req_installed=1
fi

if [ $req_installed = "0" ] && [ -f "setup.py" ]; then
    pip install -e .
    req_installed=1
fi

if [ -f ".pre-commit-config.yaml" ]; then
    pre-commit install
    pre-commit autoupdate
fi

echo "Project setup complete"
echo "Run 'source ~/venvs/$project_name/bin/activate' to activate your virtual environment"
