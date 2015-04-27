"""

This file supports vendoring, i.e. adding external packages to this project.

See: https://cloud.google.com/appengine/docs/python/tools/libraries27

"""

from google.appengine.ext import vendor

# Add any libraries installed in the "vendor" folder.
vendor.add('vendor')
