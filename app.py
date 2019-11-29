"""
      file app: entry point for project gaz
"""

from run import create_app
from flask_limiter import Limiter
from flask_limiter.util import get_remote_address

app = create_app()

limiter = Limiter(
    app,
    key_func=get_remote_address,
    default_limits=["20 per minute", "1 per second"],
)

@limiter.limit("1 per day")
def slow():
    return "24"
