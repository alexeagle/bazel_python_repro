# Python requirements

Defines third-party package dependencies.

Note that the "runtime" dependencies are those that appear in pyproject.toml#dependencies.

> Follow https://peps.python.org/pep-0735/ for pyproject.toml support for "test" and other dependency groups.

Uses the solution for runtime dependencies to constrain the others, following
https://pip-tools.readthedocs.io/en/stable/#workflow-for-layered-requirements
