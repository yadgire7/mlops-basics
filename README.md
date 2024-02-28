create virtual env
command: conda create -n winequality python=3.8 -y

activate the virtual env
command: conda activate winequality

create requirements.txt

install the required libraries
command: pip install -r requirements.txt

create template.py 
(contains code to create required project structure)

initialize git repo

dvc init  

dvc add data_given/winequality-red.csv
dvc add data_given\winequality-white.csv

git add .

