# 9-12. Multiple Modules:       Store the 'User' class in one module, and store the 'Privileges' and 'Admin' classes in a separate module.
#                               In a separate file, create an 'Admin' instance and call 'show_privileges()' to show that everything is still working correctly.

#   privileges_user.py
#   privileges_admin.py

from privileges_user import User
from privileges_admin import Privileges, Admin

admin_1 = Admin('Tim', 'Lex', 37, 'Male', 'British', 0,)
admin_1.privileges.show_privileges()