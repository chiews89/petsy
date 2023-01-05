from app.models import db, Review
from datetime import datetime

def seed_reviews():
    review1 = Review(
        buyer_id=4,
        product_id=1,
        review="Many pats blop bork doggy big pupper shoob fat boy, shoober shoob shooberino. Puppy yapper adorable doggo woofer tongue aqua doggo, snoot ruff borkdrive bork. Bark chase pupper nap, he made many woofs corgie. Long water shoob subwoofer super cute, super nap. Doing woofers, woofer pupper yapper doggie I have ever seen, barking doggo aqua dog.",
        rating=5,
        created_at=datetime.now(),
        updated_at=datetime.now()
    )

    review2 = Review(
        buyer_id=3,
        product_id=1,
        review="Shoober shoob bork clouds long walks, very jealous pupper blop such treat. Stop it walk woof neighborhood pupper such treat, woofer doge. Fat pupper doggorino much ruin diet floofs angery woofer, boofers very taste wow woof wow bark woof. Borkdrive shoob tongue pupperino. Wow such tempt much woof doggo with a bark bark squirrel chase, pupperino bark bark. Small fluffer ball, lazy doggo.",
        rating=5,
        created_at=datetime.now(),
        updated_at=datetime.now()
    )

    review3 = Review(
        buyer_id=2,
        product_id=1,
        review="Much ruin diet floofs sub woofer super woof, tongue floofs borkdrive good boys and girls, bork waggy wags. Small doggo with a long snoot for pats long doggo pupper pup, long water shoob very good spot boy dog, very jealous pupper waggy wags big old pupper.",
        rating=5,
        created_at=datetime.now(),
        updated_at=datetime.now()
    )

    review4 = Review(
        buyer_id=5,
        product_id=1,
        review="Very taste wow, noodle horse. Thicc borking doggo long water shoob good boys and girls pug many pats, very jealous pupper pats big ol very hand that feed shibe. Fluffer porgo pupperino very taste wow good boy, doge borkf bork. Very jealous pupper wow very biscuit I am bekom fat bacon good boys and girls porgo, floofs adorable doggo ruff very good spot.",
        rating=5,
        created_at=datetime.now(),
        updated_at=datetime.now()
    )

    review5 = Review(
        buyer_id=4,
        product_id=1,
        review="Most angery pup jealous pupper puggo ruff, good boys he made many woofs, woof blep bork. Maximum borkdrive shooberino blep; bark house woof adorable doggo doge what a nice floof snoot most pupper, you pupper snoot. Pupper fluffer many pats big or small, good boy pup good boy. The neighborhood pupper snoot clouds noodle horse, extremely cute most angry pupper I have ever seen. Slobber tongue shoob fluffer, woof. Borkdrive blop doggy dog, you are doing me a frighten borkdrive.",
        rating=5,
        created_at=datetime.now(),
        updated_at=datetime.now()
    )

    db.session.add(review1)
    db.session.add(review2)
    db.session.add(review3)
    db.session.add(review4)
    db.session.add(review5)

    db.session.commit()

def undo_reviews():
    db.session.execute('TRUNCATE products RESTART IDENTITY CASCADE;')
    db.session.commit()
