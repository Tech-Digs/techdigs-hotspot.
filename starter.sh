#! /bin/bash

set -e


if ! command -v python3 &> /dev/null
then 
    echo "pthon not found. installing"
    sudo apt update
    sudo apt install -y python3 python3-venv python3-pip
else 
    echo "python3 is already installed"
fi

echo "creating virtual environment"
python3 -m venv venv

echo "Activating virtual env"
source venv/bin/activate

if [ -f requirements.txt ]; then
    echo "installign dependencies please wait.."
    pip install -r requirements.txt
else
    echo "no such file"

fi

echo "setup complete'

#for ubuntu. tumia na ubuntu.