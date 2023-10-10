"""Init and utils."""
from zope.i18nmessageid import MessageFactory

import logging


PACKAGE_NAME = "docker"

_ = MessageFactory("docker")

logger = logging.getLogger("docker")
