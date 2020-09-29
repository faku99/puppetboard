from __future__ import absolute_import
from __future__ import unicode_literals

from collections import OrderedDict

from flask_wtf import FlaskForm
from wtforms import (BooleanField, HiddenField, PasswordField, RadioField,
    SelectField, StringField, TextAreaField, validators)

from puppetboard.core import get_app

app = get_app()
QUERY_ENDPOINTS = OrderedDict([
    # PuppetDB API endpoint, Form name
    ('pql', 'PQL'),
    ('nodes', 'Nodes'),
    ('resources', 'Resources'),
    ('facts', 'Facts'),
    ('factsets', 'Fact Sets'),
    ('fact-paths', 'Fact Paths'),
    ('fact-contents', 'Fact Contents'),
    ('reports', 'Reports'),
    ('events', 'Events'),
    ('catalogs', 'Catalogs'),
    ('edges', 'Edges'),
    ('environments', 'Environments'),
])
ENABLED_QUERY_ENDPOINTS = app.config.get(
    'ENABLED_QUERY_ENDPOINTS', list(QUERY_ENDPOINTS.keys()))


class QueryForm(FlaskForm):
    """The form used to allow freeform queries to be executed against
    PuppetDB."""
    query = TextAreaField('Query', [validators.DataRequired(
        message='A query is required.')])
    endpoints = SelectField('API endpoint', choices=[
        (key, value) for key, value in QUERY_ENDPOINTS.items()
        if key in ENABLED_QUERY_ENDPOINTS], default='pql')
    rawjson = BooleanField('Raw JSON')


class LoginForm(FlaskForm):
    """The form used to login to Puppetboard"""
    username = StringField('Username', [validators.DataRequired(message='Username is required')])
    password = PasswordField('Password', [validators.DataRequired(message='Password is required')])
    remember = BooleanField('Remember me')
