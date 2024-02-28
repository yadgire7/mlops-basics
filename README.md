create virtual env
```bash
conda create -n winequality python=3.8 -y
```

activate the virtual env
```bash
conda activate winequality
```

create requirements.txt

install the required libraries
```bash
pip install -r requirements.txt
```

create template.py 
(contains code to create required project structure)

initialize git repo
```bash
git init
```
initialize dvc
```bash
dvc init  
```

add files to dvc
```bash
dvc add data_given/winequality-red.csv
dvc add data_given\winequality-white.csv
```

add all the files to git
```bash
git add .
```

commit changes with a message
```bash
git commit -m "initial commit"
```

add a remote origin
```bash
git remote add origin https://github.com/yadgire7/mlops-basics.gi
```

change from master branch to main branch
```bash
git branch -M main
```

push the changes to the main branch
```bash
git push origin main
```

one line command to add and commit simultaneously
```bash
git add . && git commit -m "your message" 
```

create get_gata.py file
```bash
touch src/get_gata.py
```

add and commit changes
```bash
git add . && git commit -m "your message"
```

create load_data.py file
```bash
touch src/load_gata.py
```

update the dvc.yaml file

reproduce the changes made to dvc.yaml file
```bash
dvc repro
```

dvc.lock file will be created

add and commit changes
```bash
git add . && git commit -m "completed stage 1"
```

