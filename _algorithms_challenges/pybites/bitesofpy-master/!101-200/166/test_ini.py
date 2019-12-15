import pytest

from ini import ToxIniParser

cookiecutter = """[tox]
envlist = py27, py34, py35, py36, pypy, flake8

[testenv]
passenv = LC_ALL, LANG, HOME
commands = pytest --cov=cookiecutter {posargs:tests}
deps = -rtest_requirements.txt

[testenv:flake8]
deps =
    flake8==3.5.0
commands =
    flake8 cookiecutter tests setup.py

[testenv:cov-report]
commands = pytest --cov=cookiecutter --cov-report=term --cov-report=html"""

django = """# Tox (https://tox.readthedocs.io/) is a tool for running tests in multiple
# virtualenvs. This configuration file helps to run the test suite on all
# supported Python versions. To use it, "pip install tox" and then run "tox"
# from this directory.
#
# copied from: https://github.com/django/django/blob/master/tox.ini

[tox]
skipsdist = true
envlist =
    py3
    flake8
    docs
    isort

# Add environment to use the default python3 installation
[testenv:py3]
basepython = python3

[testenv]
usedevelop = true
passenv = DJANGO_SETTINGS_MODULE PYTHONPATH HOME DISPLAY
setenv =
    PYTHONDONTWRITEBYTECODE=1
deps =
    py{3,35,36,37}: -rtests/requirements/py3.txt
    postgres: -rtests/requirements/postgres.txt
    mysql: -rtests/requirements/mysql.txt
    oracle: -rtests/requirements/oracle.txt
changedir = tests
commands =
    {envpython} runtests.py {posargs}

[testenv:flake8]
basepython = python3
usedevelop = false
deps = flake8
changedir = {toxinidir}
commands = flake8 .

[testenv:docs]
basepython = python3
usedevelop = false
whitelist_externals =
    make
deps =
    Sphinx
    pyenchant
    sphinxcontrib-spelling
changedir = docs
commands =
    make spelling

[testenv:isort]
basepython = python3
usedevelop = false
deps = isort
changedir = {toxinidir}
commands = isort --recursive --check-only --diff django tests scripts

[testenv:javascript]
usedevelop = false
deps =
changedir = {toxinidir}
whitelist_externals = npm
commands =
    npm install
    npm test"""

oeuvre = """[tox]
minversion=2.3.1
envlist = py27,py33,py34,py35,py36,flake8,linters,docs

[testenv]
deps =
    mock>=2.0.0
    pytest!=3.0.5
    coverage
commands =
    coverage run --parallel-mode -m pytest {posargs}
    coverage combine
    coverage report -m

[testenv:venv]
deps =
    .
commands = {posargs}

# Linters
[testenv:flake8]
basepython = python3
skip_install = true
deps =
    flake8
    flake8-docstrings>=0.2.7
    flake8-import-order>=0.9
commands =
    flake8 src/oeuvre/ tests/ setup.py

[testenv:pylint]
basepython = python3
skip_install = true
deps =
    pyflakes
    pylint
commands =
    pylint src/oeuvre

[testenv:doc8]
basepython = python3
skip_install = true
deps =
    sphinx
    doc8
commands =
    doc8 docs/source/

[testenv:bandit]
basepython = python3
skip_install = true
deps =
    bandit
commands =
    bandit -r src/oeuvre/ -c .bandit.yml

[testenv:linters]
basepython = python3
skip_install = true
deps =
    {[testenv:flake8]deps}
    {[testenv:pylint]deps}
    {[testenv:doc8]deps}
    {[testenv:readme]deps}
    {[testenv:bandit]deps}
commands =
    {[testenv:flake8]commands}
    {[testenv:pylint]commands}
    {[testenv:doc8]commands}
    {[testenv:readme]commands}
    {[testenv:bandit]commands}

# Documentation
[testenv:docs]
basepython = python3
deps =
    sphinx>=1.3.0
    sphinx_rtd_theme
commands =
    sphinx-build -E -W -c docs/source/ -b html docs/source/ docs/build/html
    sphinx-build -E -W -c docs/source/ -b man docs/source/ docs/build/man

[testenv:serve-docs]
basepython = python3
skip_install = true
changedir = docs/build/html
deps =
commands =
    python -m http.server {posargs}

[testenv:readme]
basepython = python3
deps =
    readme_renderer
commands =
    python setup.py check -r -s

# Release tooling
[testenv:build]
basepython = python3
skip_install = true
deps =
    wheel
    setuptools
commands =
    python setup.py -q sdist bdist_wheel

[testenv:release]
basepython = python3
skip_install = true
deps =
    {[testenv:build]deps}
    twine >= 1.5.0
commands =
    {[testenv:build]commands}
    twine upload --skip-existing dist/*

# Flake8 Configuration
[flake8]
# Ignore some flake8-docstrings errors
ignore = D203
exclude =
    .tox,
    .git,
    __pycache__,
    docs/source/conf.py,
    build,
    dist,
    *.pyc,
    *.egg-info,
    .cache,
    .eggs
max-complexity = 10
import-order-style = google
application-import-names = oeuvre"""

pyramid = """[tox]
envlist =
    lint,
    py34,py35,py36,py37,pypy3,
    docs,py36-cover,coverage,

[testenv]
commands =
    cover: coverage run \
    {envbindir}/nosetests --with-xunit --xunit-file=...
extras =
    testing
deps =
    cover: coverage
setenv =
    COVERAGE_FILE=.coverage.{envname}

[testenv:lint]
skip_install = true
basepython = python3.6
commands =
    flake8 src/pyramid tests setup.py
    black --check --diff src/pyramid tests setup.py
    python setup.py check -r -s -m
    check-manifest
deps =
    flake8
    black
    readme_renderer
    check-manifest

[testenv:docs]
# pin to 3.5 to match what RTD uses
basepython = python3.5
whitelist_externals = make
commands =
    make -C docs doctest html epub BUILDDIR={envdir} "SPHINXOPTS=-W -E"
extras =
    docs

[testenv:pdf]
basepython = python3.5
whitelist_externals = make
commands =
    make -C docs latexpdf BUILDDIR={envdir} "SPHINXOPTS=-W -E"
extras =
    docs

[testenv:coverage]
skip_install = true
basepython = python3.6
commands =
    coverage combine
    coverage xml
    coverage report --fail-under=100
deps =
    coverage
setenv =
    COVERAGE_FILE=.coverage

[testenv:black]
skip_install = true
basepython = python3.6
commands =
    black src/pyramid tests setup.py
deps =
    black

[testenv:build]
skip_install = true
basepython = python3.6
commands =
    # clean up build/ and dist/ folders
    python -c 'import shutil; shutil.rmtree("dist", ignore_errors=True)'
    python setup.py clean --all
    # build sdist
    python setup.py sdist --dist-dir {toxinidir}/dist
    # build wheel from sdist
    pip wheel -v --no-deps --no-index --no-build-isolation ...
deps =
    setuptools
    wheel"""

ini_files = (cookiecutter, django, oeuvre, pyramid)


@pytest.mark.parametrize("ini_file, num_sections, envs, base_pys", [
    (cookiecutter, 4,
     ['flake8', 'py34', 'py35', 'py36', 'pypy', 'py27'],
     []),
    (django, 7,
     ['docs', 'flake8', 'isort', 'py3'],
     ['python3']),
    (pyramid, 8,
     ['coverage', 'docs', 'lint', 'py34', 'py35', 'py36', 'py36-cover',
      'py37', 'pypy3'],
     ['python3.5', 'python3.6']),
    (oeuvre, 14,
     ['docs', 'flake8', 'linters', 'py27', 'py33', 'py34',
      'py35', 'py36'],
     ['python3']),
])
def test_tox_ini_parser(ini_file, num_sections, envs, base_pys, tmp_path):
    f = tmp_path / "some_file.txt"
    f.write_bytes(ini_file.encode())  # https://bugs.python.org/issue17271

    tip = ToxIniParser(f.resolve())

    assert tip.number_of_sections == num_sections
    assert sorted(tip.environments) == sorted(envs)
    assert sorted(tip.base_python_versions) == sorted(base_pys)