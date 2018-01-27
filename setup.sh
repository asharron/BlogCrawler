if [ ! -d venv ]
then
  virtualenv -p python3 venv
fi

. venv/bin/activate

sudo apt-get install python3-dev libmysqlclient-dev

pip install Flask
pip install sqlalchemy
pip install flask_sqlalchemy
pip install mysqlclient
pip install sqlalchemy-migrate
pip install flask_wtf
pip install Flask-Mail