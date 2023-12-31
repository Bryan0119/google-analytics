# encoding: utf-8

import pkg_resources
import re

from . import auth, commands, tests, utils, account, auth, blueprint, columns, errors, query, segments
# Authorize and Revoke no longer do anything.
from .auth import authenticate, authorize, revoke
from .blueprint import Blueprint

__version__ = pkg_resources.get_distribution("googleanalytics").version
