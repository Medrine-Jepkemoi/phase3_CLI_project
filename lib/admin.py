from models import Admin, session_maker

admins =  Admin(admin_fname = "Medrine", admin_lname = "Jepkemoi"),

# Creating an admin
with session_maker() as session:
    for admin in admins:
        session.add(admin)
    session.commit()

# function to check if admin is valid. There can only be one admin
