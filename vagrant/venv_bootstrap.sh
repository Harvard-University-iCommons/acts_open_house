#!/bin/bash
# Set up virtualenv and migrate project
export HOME=/home/vagrant
export WORKON_HOME=$HOME/.virtualenvs
source /usr/local/bin/virtualenvwrapper.sh
mkvirtualenv -a /home/vagrant/acts_open_house -r /home/vagrant/acts_open_house/acts_open_house/requirements/local.txt acts_open_house 
workon acts_open_house
python manage.py migrate
