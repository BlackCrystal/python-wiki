# python-wiki

Wiki pages in python

## How to start

Clone project

```shell
git clone https://github.com/BlackCrystal/python-wiki.git
cd python-wiki
```

Optional, create virtual python environment and activate it

```shell
pip install --user virtualenv
virtualenv venv
```

Install requirements

```shell
pip install -r requirements.txt
```

Start "HelloWorld" server

```shell
python server.py
```

Open webpage [http://localhost:8080/](http://localhost:8080/) and You will see `Show what you can. Learn what you don't` message.

Now try to build something more incredible, like things we listed [here in the project](https://github.com/BlackCrystal/python-wiki/projects/1).

GL & HF.

## Something more incredible

Wiki folder contains application with TurboGears full framweork.

To set it up, execute these commands

```shell
cd wiki
python setup.py develop
gearbox setup-app
```

Then start server in development mode

```shell
gearbox serve --reload --debug
```

Or in production mode

```shell
gearbox serve
```


## Useful links

- [Virtualenv](https://docs.python-guide.org/dev/virtualenvs/#lower-level-virtualenv)
- [TurboGears documentation](https://turbogears.readthedocs.io/en/latest/index.html)
- [Git guide](https://rogerdudler.github.io/git-guide/)