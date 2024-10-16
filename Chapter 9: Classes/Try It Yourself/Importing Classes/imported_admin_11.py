# 9-11. Imported Admin:     Start with your work from Exercise 9-8. Store the classes 'User', 'Privileges', and 'Admin' in one module.
#                           Create a separate file, making an 'Admin' instance, and call 'show_privileges()' to show that everything is working correctly.

from privileges import User, Privileges, Admin


admin_1 = Admin('Tim', 'Lex', 37, 'Male', 'British', 0,)
admin_1.privileges.show_privileges()