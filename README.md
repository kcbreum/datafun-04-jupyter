# datafun-04-jupyter

Professional analytics project using Git, Python, venv, pip, Markdown and VS Code to demonstrate the creation of an initial data story in Jupyter Notebook. This project utilizes a virtual environment with popular libraries for data analytics, including pandas, matplotlib, and seaborn.
Commands were used on a Windows machine running PowerShell.

## Create Project Virtual Environment

On Windows, create a project virtual environment in the .venv folder. 

```shell

py -m venv .venv
.venv\Scripts\Activate
py -m pip install -r requirements.txt

```

## How to Installa nd Run the Project
In the project folder, install the following packages:
```shell
py -m pip install jupyterlab
py -m pip install numpy
py -m pip install pandas
py -m pip install matplotlib 
py -m pip install seaborn
py -m pip install scipy
```


## Freeze Requirements

```shell
py -m pip freeze > requirements.txt
```

## Git add and commit 

```shell
git add .
git commit -m "add .gitignore, cmds to readme"
git push origin main
```

## Specification

This project was built to the following specification:

- [datafun-03-spec](https://github.com/denisecase/datafun-04-spec)
