# FastAPI basics

A repo containing a basic http server created by following FastAPI documentation.
This README also contains steps to set up a local python environment for
development using `pyenv` and `poetry`.

## Running the application:

1. Clone the repo:

```bash
git clone https://github.com/narayanan-gokul/fastapi-basics.git
```

2. Navigate to the repo:

```bash
cd fastapi-basics
```

3. Ensure `pyenv` and `poetry` (by extension `pipx` are installed.
4. Ensure that the local python version matches the version specified in 
`pyproject.toml`.
5. Run:

```bash
poetry install --no-root #Installs all dependencies
poetry shell #Actovates the virtual environment
fastapi dev #Starts the server
```


## Setting up a basic python development environment:

1. Install and setup [`pyenv`](https://github.com/pyenv/pyenv?tab=readme-ov-file#installation)

The recommended method to use pyenv is to isolate the project's python binary. 
This can be done using the following command:

```bash
pyenv install <python-version>
cd <project-directory>
pyenv local <python-version>
```

This instructs pyenv to use the `<python-version` for all `python` invocations 
from within the `<project-directory>`

2. Install and activate [`pipx`](https://github.com/pypa/pipx)
3. Install `poetry` using `pipx`:

```bash
pipx install poetry
```

4. Configure `poetry` to create and use virtual environments by adding the
following lines to `poetry.toml` file:

```toml
[virtualenvs]
in-project = true
create = true
```
5. Direct `poetry` to use the python binaries provided by `pyenv`:

```bash
poetry env use $(pyenv which python)
```

6. Install the project using:

```bash
poetry install --no-root
```

7. Activate the virtual environment:

```bash
poetry shell
```

The project is now ready to use.
