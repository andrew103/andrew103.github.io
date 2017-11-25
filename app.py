
""" Module summary:
"""

from project import app

############################################################################

if __name__ == "__main__":
  app.secret_key = "secret_key"
  app.debug = True
  app.run()
