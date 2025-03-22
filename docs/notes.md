# Useful commands
python -m venv venv

.\venv\Scripts\activate
----

nano .gitignore
echo venv/ >> .gitignore
----

pip install -r requirements.txt
pip freeze > requirements.txt
----

poetry add <package-name>
poetry add pandas numpy
----

poetry new my_project
cd my_project
----

poetry install
poetry show
