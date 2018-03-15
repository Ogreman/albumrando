# albumrando 

A simple script for posting from an [albumlist](https://github.com/Ogreman/albumlist)'s API to Slack

## Testing locally

Set config variables in `.env` file or export as environment variables then:
```
python random_album.py
```

## Pipenv

Use [Pyenv](https://github.com/pyenv/pyenv) to manage installed Python versions:

```
$ curl -L https://raw.githubusercontent.com/pyenv/pyenv-installer/master/bin/pyenv-installer | bash
$ pyenv versions
* system
  2.7
  3.4.7
  3.5.4
  3.6.3
```

You can then set the default global Python version using:
```
$ pyenv global 3.6.3
$ pyenv versions
  system
  2.7
  3.4.7
  3.5.4
* 3.6.3 (set by /Users/User/.pyenv/version)

# if pip is missing:
$ easy_install pip
```

NB: install Python versions with:
```
$ pyenv install 3.6.3
```

Install dependencies to a new virtual environment using [Pipenv](https://docs.pipenv.org/):

```
$ pip install -U pipenv
$ pipenv install
```

NB: pipenv will try to use pyenv to install a missing version of Python specified in the Pipfile.

Run commands within the new virtual environment with:
```
pipenv run python random_album.py
```
