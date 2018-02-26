"""This file provides the post generation hook"""

from __future__ import print_function

from os import getcwd
from subprocess import check_call

ROOT_DIR = getcwd()

check_call(['git', 'init'])
check_call(['git', 'add', 'LICENSE'])
check_call(['git', 'commit', '-m', 'Initial commit'])
check_call(['git', 'add', '.editorconfig'])
check_call(['git', 'commit', '-m', 'Define Editor Config'])
check_call(['git', 'flow', 'init', '-d'])
