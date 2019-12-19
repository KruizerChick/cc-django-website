""" 
Django production project settings using Django 2.2.9.

PythonAnywhere (PA) Production Configurations:
 - Use Mailgun to send emails
 - Use Sentry for error logging
 - Use PythonAnywhere settings for Media/Static file locations
   and Allowed Hosts

"""

from .base import *  # noqa
import os

env_path = Path('.') / '.envs/.local'

load_dotenv(dotenv_path=env_path)
