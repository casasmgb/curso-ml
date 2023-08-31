# Python Virtualenv

Install dependencies using *pip*
```
$ pip install virtualenv
```
Create a venv dependencie into project directory

```
$ cd data_preprocesing
```

```
$ virtualenv venv
```

Launc the virtual enviroment
```
$ venv\Scripts\activate.bat
```

On the virtualenv we can install any package

```
$ pip install pandas
$ pip install numpy
```

And we can save the package and exact version in a file called **requirements.txt** for future usages

```
$ pip freeze -l > requirements.txt
```

Install packages from **requirements.txt** file

```
$ pip install -r requirements.txt 
```