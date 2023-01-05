from app.models import db, Category


def seed_categories():
    dog_food = Category(name='Dog Food')
    dog_toys = Category(name='Dog Toys')
    cat_food = Category(name='Cat Food')
    cat_toys = Category(name='Cat Toys')
    cat_litter = Category(name='Cat Litter')
    bowls_and_feeders = Category(name='Bowls & Feeders')
    grooming = Category(name='Grooming')
    clothing_and_accessories = Category(name='Clothing & Accessories')

    db.session.add(dog_food)
    db.session.add(dog_toys)
    db.session.add(cat_food)
    db.session.add(cat_toys)
    db.session.add(cat_litter)
    db.session.add(bowls_and_feeders)
    db.session.add(grooming)
    db.session.add(clothing_and_accessories)

    db.session.commit()


def undo_categories():
    db.session.execute('TRUNCATE categories RESTART IDENTITY CASCADE;')
    db.session.commit()
