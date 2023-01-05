from app.models import db, User


# Adds a demo user, you can add other users here if you want
def seed_users():
    demo = User(
        username='Demo', email='demo@aa.io', password='password')
    anita = User(
        username='Anita', email='adarling@mail.cpm', password='password')
    mowgli = User(
        username='Mowgli', email='junglelover@mail.com', password='password')
    cruella = User(
        username='Cruella', email='cruella@devil.com', password='password')
    shaggy = User(
        username='LadyT', email='shaggy@mysteryinc.com', password='password')

    db.session.add(demo)
    db.session.add(anita)
    db.session.add(mowgli)
    db.session.add(cruella)
    db.session.add(shaggy)

    db.session.commit()


# Uses a raw SQL query to TRUNCATE the users table.
# SQLAlchemy doesn't have a built in function to do this
# TRUNCATE Removes all the data from the table, and RESET IDENTITY
# resets the auto incrementing primary key, CASCADE deletes any
# dependent entities
def undo_users():
    db.session.execute('TRUNCATE users RESTART IDENTITY CASCADE;')
    db.session.commit()
