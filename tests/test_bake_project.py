"""
This file provides tests for the template.

Basically everything came from cookiecutter-pypackage:
https://github.com/audreyr/cookiecutter-pypackage/blob/master/tests/test_bake_project.py
"""

from contextlib import contextmanager
import datetime
from cookiecutter.utils import rmtree


@contextmanager
def bake_in_temp_dir(cookies, *args, **kwargs):
    """
    Bakes cookies in a temporary directory. Cleans up after itself (I think)
    """
    result = cookies.bake(*args, **kwargs)
    try:
        yield result
    finally:
        rmtree(str(result.project))


def test_bake_with_defaults(cookies):
    """Tests the default run (I think)"""
    with bake_in_temp_dir(cookies) as result:
        assert result.project.isdir()
        assert result.exit_code == 0
        assert result.exception is None

        found_toplevel_files = [f.basename for f in result.project.listdir()]
        assert '.editorconfig' in found_toplevel_files
        assert '.gitignore' in found_toplevel_files
        assert 'LICENSE' in found_toplevel_files
        assert 'README.md' in found_toplevel_files
        assert 'wotw-project.sublime-project' in found_toplevel_files


def test_year_compute_in_license_file(cookies):  # pylint: disable=invalid-name
    """Ensures the current year is in the license"""
    with bake_in_temp_dir(cookies) as result:
        license_file_path = result.project.join('LICENSE')
        now = datetime.datetime.now()
        assert str(now.year) in license_file_path.read()


def test_name_in_readme(cookies):
    """Ensures the project name is in the README"""
    with bake_in_temp_dir(cookies) as result:
        readme_file_path = result.project.join('README.md')
        assert 'wotw-project' in readme_file_path.read()


def test_name_in_gitignore(cookies):
    """Ensures the project name is in the .gitignore"""
    with bake_in_temp_dir(cookies) as result:
        gitignore_file_path = result.project.join('.gitignore')
        assert '!wotw-project.sublime-project' in gitignore_file_path.read()
