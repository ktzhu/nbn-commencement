#!/usr/bin/env python

"""
Project-wide application configuration.

DO NOT STORE SECRETS, PASSWORDS, ETC. IN THIS FILE.
They will be exposed to users. Use environment variables instead.
See get_secrets() below for a fast way to access them.
"""

import os

"""
NAMES
"""
# Project name used for display
PROJECT_NAME = 'Goodbye from the Class of 2013'

# Project name used for paths on the filesystem and in urls
# Use dashes, not underscores
PROJECT_SLUG = 'commencement2013'

# The name of the repository containing the source
REPOSITORY_NAME = 'nbn-commencement'

"""
DEPLOYMENT
"""
PRODUCTION_S3_BUCKETS = ['apps.northbynorthwestern.com']
PRODUCTION_SERVERS = ['cron.nprapps.org']

STAGING_S3_BUCKETS = ['apps.northbynorthwestern.com']
STAGING_SERVERS = ['50.112.92.131']

# Should code be deployed to the web/cron servers?
DEPLOY_TO_SERVERS = False

# Should the crontab file be installed on the servers?
# If True, DEPLOY_TO_SERVERS must also be True
DEPLOY_CRONTAB = False

# Should the service configurations be installed on the servers?
# If True, DEPLOY_TO_SERVERS must also be True
DEPLOY_SERVICES = False

# These variables will be set at runtime. See configure_targets() below
S3_BUCKETS = []
SERVERS = []
DEBUG = True

"""
COPY EDITING
"""
COPY_GOOGLE_DOC_KEY = '0AiINjEdvBDPadG5JQ0NJdWdDX3EwRFdvRi1ERUR4Rnc'
# COPY_GOOGLE_DOC_KEY = '0AiINjEdvBDPadDBqT0h6QWJDamZ6OUtXNE5GYVlhRkE'

"""
SHARING
"""
PROJECT_DESCRIPTION = "Northwestern's Class of 2013 looks back on their time in Evanston."
SHARE_URL = 'http://%s/%s/' % (PRODUCTION_S3_BUCKETS[0], PROJECT_SLUG)


TWITTER = {
    'TEXT': PROJECT_NAME,
    'URL': SHARE_URL
}

FACEBOOK = {
    'TITLE': PROJECT_NAME,
    'URL': SHARE_URL,
    'DESCRIPTION': PROJECT_DESCRIPTION,
    'IMAGE_URL': '',
    'APP_ID': '138837436154588'
}

"""
SERVICES
"""
GOOGLE_ANALYTICS_ID = 'UA-15143352-1'

"""
Utilities
"""
def get_secrets():
    """
    A method for accessing our secrets.
    """
    env_var_prefix = PROJECT_SLUG.replace('-', '')

    secrets = [
        '%s_TUMBLR_APP_KEY' % env_var_prefix,
        '%s_TUMBLR_OAUTH_TOKEN' % env_var_prefix,
        '%s_TUMBLR_OAUTH_TOKEN_SECRET' % env_var_prefix,
        '%s_TUMBLR_APP_SECRET' % env_var_prefix
    ]

    secrets_dict = {}

    for secret in secrets:
        # Saves the secret with the old name.
        secrets_dict[secret.replace('%s_' % env_var_prefix, '')] = os.environ.get(secret, None)

    return secrets_dict

def configure_targets(deployment_target):
    """
    Configure deployment targets. Abstracted so this can be
    overriden for rendering before deployment.
    """
    global S3_BUCKETS
    global SERVERS
    global DEBUG

    if deployment_target == 'production':
        S3_BUCKETS = PRODUCTION_S3_BUCKETS
        SERVERS = PRODUCTION_SERVERS
        DEBUG = False
    else:
        S3_BUCKETS = STAGING_S3_BUCKETS
        SERVERS = STAGING_SERVERS
        DEBUG = True

"""
Run automated configuration
"""
DEPLOYMENT_TARGET = os.environ.get('DEPLOYMENT_TARGET', None)

configure_targets(DEPLOYMENT_TARGET)

