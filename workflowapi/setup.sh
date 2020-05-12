#!/bin/sh
#:<< comment
#install pip3
echo "Installing pip3:"
sudo apt-get -y install python3-pip

#delete pip
echo "Deleting pip:"
sudo rm -r ~/.local/lib/python3.6/site-packages/pip

#install all dependecies from requirements.py
echo "Upgrading pip:"
pip3 install --upgrade pip --user

#delete pip
echo "Deleting pip:"
sudo rm -r ~/.local/lib/python3.6/site-packages/pip


echo "Installing requirements:"
pip3 install -r requirements.txt --user
pip3 install drf-nested-routers

# create database from model
echo "Make Migrations:"
python3 manage.py migrate
python3 manage.py makemigrations workflowapp

#start django server
echo "Start Server:"
#start django server on Port accessible from everyone
python3 manage.py runserver 0:8000
