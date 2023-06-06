from models import Category, faker, session_maker

categories = [
    Category(category_name = "Fruit"),
    Category(category_name = "Vegetable"),
    Category(category_name = "Dairy Products"),
    Category(category_name = "Meat")
]

def create_categories():
    with session_maker() as session:
        for category in categories:
            session.add(category)
        session.commit()

create_categories()



