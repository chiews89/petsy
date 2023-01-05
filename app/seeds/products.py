from app.models import db, Product
from datetime import datetime


def seed_products():
  ############################## Category - Dog Food ##############################
  blue_buffalo = Product(
    seller_id=1,
    name="Blue Buffalo Life Protection Formula",
    image_url="https://img.chewy.com/is/image/catalog/46860_MAIN._AC_SL1500_V1636151211_.jpg",
    description="Blue Buffalo Life Protection Formula was created for the holistic health and well-being of adult dogs. All formulas start with real meat, whole grains, garden veggies and fruit, plus added LifeSource Bits, a precise blend of nutrients that have been enhanced with a Super 7 package of antioxidant-rich ingredients. This Adult Chicken & Brown Rice Recipe features delicious, protein-rich deboned chicken and other natural ingredients for a healthy meal your dog will love.",
    price=55.98,
    category_id=1,
    created_at=datetime.now(),
    updated_at=datetime.now()
  )

  pedigree = Product(
    seller_id=1,
    name="Pedigree Adult Complete Nutrition",
    image_url="https://m.media-amazon.com/images/I/81vc7aaPoeL._AC_SX522_.jpg",
    description="Help your four-legged friend live life to the fullest with Pedigree Adult Complete Nutrition Roasted Chicken, Rice & Vegetable Flavor Dry Dog Food. Formulated to give dogs all the energy and nourishment they need to thrive, this food is packed with essential nutrition and a delicious roasted chicken flavor. Including B vitamins, zinc and omega-6 fatty acid to keep him looking great, it also contains leading levels of the antioxidant vitamin E to help keep his immune systems strong. Plus, this balanced dog food features a special fiber blend, which helps promote healthy digestion—and helps keep yard patrol under control.",
    price=7.50,
    category_id=1,
    created_at=datetime.now(),
    updated_at=datetime.now()
  )

  purina = Product(
    seller_id=1,
    name="Purina ONE SmartBlend",
    image_url="https://img.chewy.com/is/image/catalog/91837_MAIN._AC_SL1500_V1634333508_.jpg",
    description="Purina ONE's SmartBlend Chicken & Rice Formula features real chicken as the first ingredient, blended with other high-quality protein sources to help support strong muscles and a healthy heart. Chicken is tastefully rich in protein and blends well with grains and other ingredients to create a complete protein profile. A dual defense antioxidant blend of vitamins E and A joins forces with zinc and selenium to promote a healthy immune system and a radiant coat. By choosing smart ingredients that work together, SmartBlend provides a 100% complete diet and helps support your dog's whole body health.",
    price=14.98,
    category_id=1,
    created_at=datetime.now(),
    updated_at=datetime.now()
  )

  kibbles = Product(
    seller_id=1,
    name="Kibbles 'n Bits Original",
    image_url="https://img.chewy.com/is/image/catalog/134039_MAIN._AC_SS800_V1557864186_.jpg",
    description="Give your pup the nutrition and flavor he loves with the Kibbles 'n Bits Original Savory Beef & Chicken Flavors Dry Dog Food. This formula packs plenty of meaty taste into a blend of crunchy kibble and soft meaty bits made with the flavors of beef and chicken. It's loaded with high-quality protein to help support strong muscles, plus vitamins, minerals and antioxidants so it's a complete and balanced diet for adults. Plus, it's proudly made in the USA so it's a satisfying meal you can feel good about serving your dog every day!",
    price=23.98,
    category_id=1,
    created_at=datetime.now(),
    updated_at=datetime.now()
  )

  hills = Product(
    seller_id=1,
    name="Hill's Science Diet",
    image_url="https://assets.petco.com/petco/image/upload/f_auto,q_auto/1327593-center-1",
    description="Nourish your furry friend from the inside out with Hill's Science Diet Adult Sensitive Stomach & Skin Chicken Recipe. This dry dog food is specifically designed for adult dogs. It features real chicken first and contains prebiotic fiber to support a balanced microbiome for healthy digestion. This recipe also delivers a generous source of vitamin E and omega-6 fatty acids to promote healthy skin and a lustrous coat. You'll love knowing that it's backed by decades of cutting-edge research, and your dog will love the way every bite tastes!",
    price=68.99,
    category_id=1,
    created_at=datetime.now(),
    updated_at=datetime.now()
  )

  ############################## Category - Dog Toys ##############################
  moose = Product(
    seller_id=1,
    name="KONG Cozie Marvin the Moose Plush Dog Toy",
    image_url="https://cdn.shopify.com/s/files/1/2382/0223/products/40938-1499796385_e16bfbd0-ff98-40f5-b828-2bd43b22581b_1000x1000.jpg?v=1571614173",
    description="The KONG Cozies are cute, soft and cuddly plush toys made with an extra layer of material, so they're extra tough. Cozies are perfect for a game of fetch or as a comfort toy for your furry friend. Grab one of the 10 amazingly cute Cozie characters for your dog and we know your dog will love you for it.",
    price=10.99,
    category_id=2,
    created_at=datetime.now(),
    updated_at=datetime.now()
  )

  ball = Product(
    seller_id=1,
    name="KONG Squeezz Ball Dog Toy",
    image_url="https://img.chewy.com/is/image/catalog/53376_MAIN._V1524496315_.jpg",
    description="The KONG Squeezz Ball has a recessed squeaker that gives the safest and funnest squeak of any toy out there. Great for games of fetch, the erratic bounce and squeak guarantee tons of fun for you and your dog.",
    price=5.99,
    category_id=2,
    created_at=datetime.now(),
    updated_at=datetime.now()
  )

  zebra = Product(
    seller_id=1,
    name="Frisco Zebra Rope Squeaky Dog Toy",
    image_url="https://img.chewy.com/is/image/catalog/242163_MAIN._V1603378285_.jpg",
    description="Send your pup on a safari of fun! This zebra rope toy is made for everyday, interactive play—from fetch to catch and all other kinds of interactive games. With a knotted ball in the middle, four rope legs sticking out of the ball and a squeaky zebra head on top, this toy is made to keep your pup engaged in playtime and up for all the exercise they need.",
    price=7.98,
    category_id=2,
    created_at=datetime.now(),
    updated_at=datetime.now()
  )

  pig = Product(
    seller_id=1,
    name="Multipet Latex Polka Dot Globlet Pig Squeaky Dog Toy",
    image_url="https://img.chewy.com/is/image/catalog/68052_MAIN._V1628098589_.jpg",
    description="No wonder pups love to rough up the Multipet Latex Polka Dot Globlet Pig Dog Toy… if it sounds like a pig, and looks like a pig, it's gotta be filled with bacon. Right? While there are no bits of bacon inside, the Globlet Pig Dog Toy is filled with hours of chew-time fun for pets of all ages.",
    price=5.12,
    category_id=2,
    created_at=datetime.now(),
    updated_at=datetime.now()
  )

  leprechaun = Product(
    seller_id=1,
    name="Frisco St. Patrick's Leprechaun Muscle Plush Squeaky Dog Toy",
    image_url="https://img.chewy.com/is/image/catalog/303126_MAIN._AC_SL1500_V1641230241_.jpg",
    description="With a little bit of Irish luck, your pooch may become just as big and strong as their new best friend! This muscular leprechaun is the perfect playmate for handling any level of epic adventures that you and your dog have in store. His orange beard and five sewn-in squeakers will make him irresistible, that is, if his muscles won't first. But that's not all, as his TPR chest is just waiting for your pooch to sink their teeth into it. Playtime is about to get big and swole with this new leprechaun friend on board.",
    price=9.79,
    category_id=2,
    created_at=datetime.now(),
    updated_at=datetime.now()
  )

  ############################## Category - Cat Food ##############################
  fancy_feast = Product(
    seller_id=2,
    name="Fancy Feast Gravy Lovers",
    image_url="https://img.chewy.com/is/image/catalog/75978_MAIN._AC_SL1500_V1584020009_.jpg",
    description="Make dinner a black tie optional affair with the Fancy Feast Gravy Lovers Poultry & Beef Feast Variety Pack. With a delicious combo of your cat's favorite flavors—chicken, turkey and beef—this gourmet food features small, delicate bites that are slow-cooked and served in a thick gourmet gravy. The added vitamins and minerals offer complete and balanced nutrition, making every mealtime a nutritious and delicious occasion. And since variety is the spice of life, the selection of flavors will keep him interested, with an even mix of Turkey Feast, Chicken Feast and Beef Feast to keep his tummy happy.",
    price=19.20,
    category_id=3,
    created_at=datetime.now(),
    updated_at=datetime.now()
  )

  iams = Product(
    seller_id=2,
    name="Iams ProActive Health",
    image_url="https://img.chewy.com/is/image/catalog/348940_MAIN._AC_SL1500_V1639537897_.jpg",
    description="Great health starts with a great diet, so IAMS PROACTIVE HEALTH Adult Indoor Weight Control & Hairball Control Care Dry Cat Food with Chicken and Turkey Cat Kibble to bring out the best in your pet! This dry cat food is made with tasty chicken and turkey, packed into an irresistibly crunchy kibble. A special formula with healthy weight management in mind, this recipe is made with L-carnitine which helps burn fat and maintain a healthy metabolism. Plus, a fiber blend with beet pulp helps support healthy digestion and reduce hairballs, while omega acids promote a beautiful, healthy coat. Your cat will love this purr-fect blend of flavor and nutrients!",
    price=24.98,
    category_id=3,
    created_at=datetime.now(),
    updated_at=datetime.now()
  )

  friskies = Product(
    seller_id=2,
    name="Friskies Chicken Lovers",
    image_url="https://img.chewy.com/is/image/catalog/76424_MAIN._AC_SL1500_V1590595025_.jpg",
    description="Show your kitty how much your care with Purina Friskies Gravy Wet Cat Food Variety Pack, Chicken Lovers Prime Filets & Shreds. This variety pack of high-protein wet food for adult cats is purr-pared to provide 100% complete and balanced nutrition to your furry buddy. It features tender shreds of real chicken and savory gravy in four different recipes all with an enticing aroma. This variety pack of wet cat food is crafted with an array of textures that cats love and flavors that are paw-sitively irresistible.",
    price=20.78,
    category_id=3,
    created_at=datetime.now(),
    updated_at=datetime.now()
  )

  nine_lives = Product(
    seller_id=2,
    name="9 Lives Daily Essentials",
    image_url="https://img.chewy.com/is/catalog/99877_MAIN._AC_SL1500_V1474979127_.jpg",
    description="9 Lives Daily Essentials Dry Cat Food features the flavors cats love, including chicken, beef, and salmon. Formulated to supply complete and balanced nutrition for all life stages, 9 Lives Daily Essentials combines omega 3 fatty acids for healthy skin and coat, high-quality protein for strong muscle growth, and taurine to help maintain heart and vision health. It's the great taste cats want, and the nutrition they need to live long, healthy lives.",
    price=3.68,
    category_id=3,
    created_at=datetime.now(),
    updated_at=datetime.now()
  )

  sheba = Product(
    seller_id=2,
    name="Sheba Perfect Portions Multipack",
    image_url="https://img.chewy.com/is/image/catalog/126366_MAIN._AC_SL1500_V1626815809_.jpg",
    description="Please even the pickiest palates with the meaty flavor of Sheba Perfect Portions Roasted Chicken and Tender Turkey Entrées. This tasty variety pack includes 6 Roasted Chicken and 6 Tender Turkey Cuts in Gravy Twin Pack entrees to satisfy your kitty's appetite for exciting culinary variety. Both entrees feature tender meaty morsels in tasty gravy and are fortified with all the essential vitamins and minerals your kitty needs to feel her best. They're made entirely without grain, wheat, corn, soy or artificial flavors or preservatives and come in convenient snap-and-peel twin packs that let you feed the purr-fect amount without leftovers every time. Your cat will love the thrill of fresh new flavors and you'll love the mess-free convenience!",
    price=11.29,
    category_id=3,
    created_at=datetime.now(),
    updated_at=datetime.now()
  )

  ############################## Category - Cat Toys ##############################
  teaser = Product(
    seller_id=2,
    name="Frisco Bird Teaser with Feathers",
    image_url="https://img.chewy.com/is/image/catalog/161199_MAIN._AC_SL1500_V1568240232_.jpg",
    description="This is no angry bird, but the perfect play buddy for your kitty. Wave it around and let the colorful feathers, dangly string, crinkly sound and catnip entice bored felines to jump into play. Leap, actually! By stimulating their natural hunting instincts, it's the perfect way to provide cats with the daily exercise they need. Playing together also helps strengthen the bond between you and your cat, on the daily.",
    price=3.98,
    category_id=4,
    created_at=datetime.now(),
    updated_at=datetime.now()
  )

  springs = Product(
    seller_id=2,
    name="Frisco Colorful Springs",
    image_url="https://img.chewy.com/is/image/catalog/161807_MAIN._V1565795954_.jpg",
    description="Spring into playtime with a classic kitty playtime favorite! Some cats are all about the simple things, like a colorful, bouncy spring to chase and bat around the house. These springs have an erratic bounce to turn up the playtime excitement, and come in vibrant colors to keep cats engaged in play. They're perfect to give your kitty the daily mental stimulation and exercise he needs, without a whole lot of fuss. Just break them out and let the games spring on!",
    price=4.98,
    category_id=4,
    created_at=datetime.now(),
    updated_at=datetime.now()
  )

  mice = Product(
    seller_id=2,
    name="Frisco Basic Plush Mice Cat Toy with Catnip",
    image_url="https://img.chewy.com/is/image/catalog/245899_MAIN._V1607371641_.jpg",
    description="This mousy crew packs triple the fun for cats everywhere—a fuzzy texture to grab and bite, string tails to chase, and an infusion of Canadian catnip to go wild over! Toss these around to get cats chasing and batting after them, or carrying them around as their playtime “prey”. By stimulating their natural hunting instincts, it's the perfect way to provide cats with the daily exercise they need. Playing together also helps strengthen the bond between you and your cat, on the daily.",
    price=6.98,
    category_id=4,
    created_at=datetime.now(),
    updated_at=datetime.now()
  )

  butterfly = Product(
    seller_id=2,
    name="Frisco Butterfly Cat Tracks",
    image_url="https://img.chewy.com/is/image/catalog/161805_MAIN._AC_SL400_V1565736428_.jpg",
    description="If there was an amusement park for kitties, this toy would be the main attraction. That's because these tracks have everything cats love—a ball to bat and chase around the tracks, the excitement of the rolling sound, and even a fluttery butterfly on top! There are three levels for even more play, each with its own rolling ball, so even more than one kitty can get in on the fun. Go ahead, let them go wild. The nonskid pads keep the track from sliding around when playtime goes into overtime.",
    price=10.98,
    category_id=4,
    created_at=datetime.now(),
    updated_at=datetime.now()
  )

  scratcher = Product(
    seller_id=2,
    name="Frisco Magic Moon & Stars Wave Scratcher Cat Toy with Catnip",
    image_url="https://img.chewy.com/is/image/catalog/265622_MAIN._AC_SL1500_V1620918820_.jpg",
    description="Scratching is already pretty magical for kitty! The wavy shape is purr-fect for cats to get a good grip and stretch while they scratch. Layers of pressed wavy cardboard shred easily under your cat's claws—instead of your furniture—without catching. Now kitty can scratch to the moon (and stars) and back. Don't let the enchantment vanish—collect all the magic-themed toys from Frisco, only at Chewy.",
    price=10.98,
    category_id=4,
    created_at=datetime.now(),
    updated_at=datetime.now()
  )

  ############################## Category - Cat Litter ##############################
  feline_pine = Product(
    seller_id=2,
    name="Feline Pine Original Non-Clumping Wood Cat Litter",
    image_url="https://img.chewy.com/is/catalog/47406._AC_SL400_V1460478783_.jpg",
    description="Banish odors and keep your home pine fresh with Feline Pine Non-Clumping Cat Litter. The highly-absorbent pine fibers work like thousands of tiny sponges to absorb liquid and lock away ammonia odors in a snap. This natural, non-clumping litter is clay-free, which means it leaves no irritating dust in the air when you pour. Plus, the improved formula absorbs liquid twice as fast as the original Feline Pine. This improved formula still uses the odor-fighting powers of 100% natural pine and says no to harsh chemicals, additives and synthetic perfumes—utilizing the power of nature to eliminate the toughest odors and leave your home smelling fresh.",
    price=17.04,
    category_id=5,
    created_at=datetime.now(),
    updated_at=datetime.now()
  )

  tidy_cats = Product(
    seller_id=2,
    name="Tidy Cats Glade Tough Scented Clumping Clay Cat Litter",
    image_url="https://img.chewy.com/is/image/catalog/66923_MAIN._AC_SL1500_V1617073918_.jpg",
    description="Double down on litter box odor control with Purina Tidy Cats With Glade Clear Springs clumping litter. Backed by the power of Glade, this clay cat litter takes a stand against strong scents, leaving a fresh fragrance behind. The clumping multi cat litter locks down ammonia, urine and fecal odors, keeping your kitties' litter boxes smelling nice for 10 days when used as directed. Plus, the clay clumping cat litter forms strong, tight clumps that make cleaning up a simple task. Great for your whole feline family, this scented clumping cat has a moisture-locking technology to keep them dry, comfy and willing to use their boxes. Check kitty litter box cleaning off your to-do list with this powerful odor control cat litter, and get back to spending more fun time with your favorite felines.",
    price=11.49,
    category_id=5,
    created_at=datetime.now(),
    updated_at=datetime.now()
  )

  scoopable = Product(
    seller_id=2,
    name="Frisco Multi-Cat Unscented Clumping Clay Cat Litter",
    image_url="https://img.chewy.com/is/image/catalog/129035_MAIN._SY630_V1524164847_.jpg",
    description="Frisco Multi-Cat Clumping Cat Litter is made of all-natural clay that forms hard clumps for easy scooping. The granules create a powerful bond to lock in moisture and prevent any liquid from getting to the bottom of the litter box. This litter is especially formulated to neutralize odors quickly and is low-tracking, so there's less mess and no scattered litter trails. It's hypo-allergenic to common allergens such as dust, plant proteins and fragrances. Frisco Multi-Cat is a heavy-duty litter that's ideal for sifting and mechanical boxes and is highly effective in multiple cat households.",
    price=15.99,
    category_id=5,
    created_at=datetime.now(),
    updated_at=datetime.now()
  )

  naturally_fresh = Product(
    seller_id=2,
    name="Naturally Fresh Multi-Cat Unscented Clumping Walnut Cat Litter",
    image_url="https://assets.petco.com/petco/image/upload/f_auto,q_auto/2167525-center-1",
    description="Protect your home from the smell of your kitty's litter box with Naturally Fresh Walnut-Based Multi-Cat Quick-Clumping Cat Litter. Made from 100% natural walnut shells, it eliminates both urine and fecal odors with a malodor counteractant. This absorbent formula neutralizes odors better than clay, pine, corn and wheat and is biodegradable for an eco-friendly option. Free of silica dust for paw-tners or pet parents with respiratory problems, this litter doesn't stick to your furry friend's paws to reduce tracking. Ideal for multi-cat households, Naturally Fresh Walnut-Based Multi-Cat Quick-Clumping Cat Litter also contains no chemicals, toxins, clay, corn and grains for the safety of your companion.",
    price=22.99,
    category_id=5,
    created_at=datetime.now(),
    updated_at=datetime.now()
  )

  scoopfree = Product(
    seller_id=2,
    name="ScoopFree Premium Unscented Non-Clumping Crystal Cat Litter",
    image_url="https://img.chewy.com/is/image/catalog/70734_MAIN._V1616423529_.jpg",
    description="Simplify litter box maintenance and keep your home smelling fresh with ScoopFree Premium Unscented Non-Clumping Crystal Cat Litter. These convenient trays are specifically designed to work with the PetSafe ScoopFree Self-Cleaning Cat Litter Box, and because they're completely disposable, you never have to see, touch or smell messy waste. Each tray is pre-filled with 4.5 pounds of ScoopFree's original blue crystals cat litter that features a light, fresh scent to help control odor better than traditional clay or clumping litter. Simply replace the disposable tray every few weeks, and your ScoopFree cat litter box is just like new.",
    price=58.95,
    category_id=5,
    created_at=datetime.now(),
    updated_at=datetime.now()
  )

  ############################## Category - Bowls & Feeders ##############################
  elevated_dog_bowls = Product(
    seller_id=1,
    name="Frisco Marble Print Stainless Steel Double Elevated Dog Bowl",
    image_url="https://img.chewy.com/is/image/catalog/216017_MAIN._AC_SL1500_V1591020393_.jpg",
    description="Dinnertime just leveled up in a massive way. With separate bowls for food and water, and elevated legs for comfort, your dog won't ever want to stop chowing down. Small and medium dogs won't have to bend down too far to reach their bowls, seeing that it'll now be at the perfect height to reach. The marble print will entice your pup and fits in with your stylish home décor. Style meets substance with this awesome set.",
    price=22.99,
    category_id=6,
    created_at=datetime.now(),
    updated_at=datetime.now()
  )

  slow_feeder = Product(
    seller_id=1,
    name="Frisco Bone Shaped Ridges Slow Feed Bowl",
    image_url="https://img.chewy.com/is/image/catalog/216041_MAIN._V1591020668_.jpg",
    description="If your dog's a speed eater, help them slow down with Frisco Slow Feed Bowls. This bowl features ridges to encourage your dog to take their sweet time eating, which helps support their digestive system and overall health. They're even top rack dishwasher safe so you can clean it easily in between meals.",
    price=6.90,
    category_id=6,
    created_at=datetime.now(),
    updated_at=datetime.now()
  )

  stainless_bowl = Product(
    seller_id=1,
    name="Frisco Stainless Steel Bowl",
    image_url="https://img.chewy.com/is/image/catalog/175220_Main._AC_SL1500_V1572449624_.jpg",
    description="Serve up dinner in style with the Frisco Stainless Steel Pet Bowl. The smart design helps keep kibble in its place—in the bowl—and features a wide rubber base that keeps it from tipping, even if your pal is extra hungry. Stainless steel is stain-proof, rust-resistant and easy to clean by hand or in the dishwasher. It's the perfect bowl for all your pet's meals and water too.",
    price=3.85,
    category_id=6,
    created_at=datetime.now(),
    updated_at=datetime.now()
  )

  ceramic_bowl = Product(
    seller_id=2,
    name="Frisco Double-Sided Ceramic Elevated Cat Bowl",
    image_url="https://img.chewy.com/is/image/catalog/232081_MAIN._AC_SL400_V1605055318_.jpg",
    description="Your cat will flip for the Frisco Double-Sided Ceramic Elevated Cat Bowl. This modern tiled ceramic bowl features an elevated design to help with easier swallowing and smoother digestion. The bowls on either side are designed to each have a different angle so it's suited for different pet size use. Simply flip the bowl to use either side! This, cat parents, is the future of feline fine dining.",
    price=9.64,
    category_id=6,
    created_at=datetime.now(),
    updated_at=datetime.now()
  )

  cat_bowl = Product(
    seller_id=2,
    name="Frisco Cat Face Non-skid Ceramic Cat Dish",
    image_url="https://img.chewy.com/is/image/catalog/256101_MAIN._AC_SL400_V1615321299_.jpg",
    description="Add a pop of color to your kitty's meals with this saucer-style cat dish! It's purr-fect for bright kitty personalities, with solid blue all around and an adorable kitty face inside that's (almost) as cute as your cat. With this adorable dish, you're not only serving up dinner, you're serving up the cute, too! Plus, it features non-skid feet on the bottom to help keep mealtime messiness under control.",
    price=5.53,
    category_id=6,
    created_at=datetime.now(),
    updated_at=datetime.now()
  )

  ############################## Category - Grooming ##############################
  paw_butter = Product(
    seller_id=3,
    name="Pet Head Oatmeal Paw Butter",
    image_url="https://img.chewy.com/is/image/catalog/108958_MAIN._SY630_V1543610031_.jpg",
    description="Give your furball some well-deserved TLC with the Pet Head Oatmeal Paw Butter. Specially formulated to soothe dry and cracked paws, there's no need to tread lightly after a dose of paw butter. Using shea butter, oatmeal, mango, vitamins E and F, coconut oil, olive oil, and aloe vera, it packs a powerful—yet gentle—blend of soothing therapy. Just gently massage into your best bud's paws and let him go back to playing! Safe for cats, dogs and any furball with paws, it's ideal for homes with multiple furry friends. Plus, it smells great, and it's made in the USA with completely safe and pet-friendly ingredients.",
    price=7.87,
    category_id=7,
    created_at=datetime.now(),
    updated_at=datetime.now()
  )

  oatmeal_shampoo = Product(
    seller_id=3,
    name="Burt's Bees Oatmeal Shampoo",
    image_url="https://img.chewy.com/is/image/catalog/94028_MAIN._AC_SL1500_V1543533456_.jpg",
    description="Burt's Bees Oatmeal with Colloidal Oat Flour Dog Shampoo is made with natural ingredients like colloidal oat flour and honey for a product you can trust! Colloidal oat flour helps to deeply condition your BFF's dry skin, while honey promotes a shiny coat. This gentle shampoo is completely pH balanced for dogs and just like other Burt's Bees products, it's made in the USA without artificial fragrances, chemicals, parabens, phthalates, petrolatum or sodium lauryl sulfate (SLS). And, so your pup can stay clean and protected from pests, it won't wash off topical flea and tick treatments when used as directed! So, give your paw-tner's coat a deep clean with this gentle, veterinarian recommended solution that's packaged in an 80% post-consumer recycled bottle!",
    price=5.94,
    category_id=7,
    created_at=datetime.now(),
    updated_at=datetime.now()
  )

  dog_brush = Product(
    seller_id=3,
    name="Hartz Groomer's Best Combo Dog Brush",
    image_url="https://img.chewy.com/is/image/catalog/132675_MAIN._AC_SL1500_V1637362610_.jpg",
    description="Make your grooming work double time with the Hartz Groomer's Best Combo Dog Brush. This dual-action brush has two specialized sides―one with stainless steel pins to remove lose hair and tangles, and another with nylon bristles to redistribute the natural oils in your dog's coat to restore shine and silkiness. It's great for pups with long, curly or wiry coats and is extra-gentle thanks to the safety tips on every pin. Plus, it has an ergonomically designed handle so you can enjoy brushing time as much as your pal.",
    price=5.45,
    category_id=7,
    created_at=datetime.now(),
    updated_at=datetime.now()
  )

  brush_gloves = Product(
    seller_id=3,
    name="Mr. Peanut's Hand Gloves Dog & Cat Grooming & Deshedding Aid",
    image_url="https://i5.walmartimages.com/asr/092bce33-e72a-46b8-bf1a-62e61bf909eb.ae5cf59bb30d514f9cbb72271cb81b29.jpeg",
    description="Help remove loose fur from your pet's coat with Mr. Peanuts' Hand Gloves. Excessive shedding means more cleaning for you, so catching those loose hairs before they fall is crucial! These gloves are made with a flexible mesh and soft, rubber tips all over the palms to help lift dirt and undo tangles and mats. While some grooming tools may intimidate your companion, with this grooming glove all you have to do is put it on, secure it with the adjustable fuzzy fastener strap and pet your best bud like you usually do! As you pet, the glove traps the fur in the glove for easy cleanup and removal. It's perfect for all coat types including short hair, long hair and even wet or dry hair. When you're all done, simply wash the glove and let it dry under the sun!",
    price=9.99,
    category_id=7,
    created_at=datetime.now(),
    updated_at=datetime.now()
  )

  deodorizing_shampoo = Product(
    seller_id=3,
    name="Arm & Hammer Kiwi Blossom Super Deodorizing Dog Shampoo",
    image_url="https://img.chewy.com/is/image/catalog/227879_MAIN._AC_SL1500_V1584977167_.jpg",
    description="Help keep your pup smelling fur-esh and clean with Arm & Hammer's Super Deodorizing Dog Shampoo! Made with a refreshing kiwi blossom scent, this shampoo is formulated with natural ingredients to stop the stink. It is ultra-gentle, and pH balanced making it extra paw-fect for puppies and for canine companions with sensitive skin! Simply scrub your best bud from the back of his ears to his tail, rinse, dry him with a towel and brush his coat once it's fully dry. And when you're cleaning his precious face, be sure to use a washcloth for a more careful clean.",
    price=4.48,
    category_id=7,
    created_at=datetime.now(),
    updated_at=datetime.now()
  )

  ############################## Category - Clothing & Accessories ##############################
  hawaiian_shirt = Product(
    seller_id=3,
    name="Frisco Pineapple Hawaiian Camp Dog & Cat Shirt",
    image_url="https://img.chewy.com/is/image/catalog/153596_PT3._AC_SL1500_V1644883746_.jpg",
    description="Remember to measure your pet for the paw-fect fit. Bring a tropical flair to your pet's look with the Frisco Pineapple Hawaiian Camp Dog & Cat Shirt. Perfect for any summer outing, this fruit and hibiscus print shirt is a go-to for any BBQ, luau or day at the beach. The step-in design and fuzzy fasteners on the belly make it easy and quick to put on and take off your pet. It features wide hook-and-loop fasteners for built-in adjustability. With machine washable fabric and a built-in leash hole so you can always be ready to go for a walk, this shirt is totally chill for summer.",
    price=13.99,
    category_id=8,
    created_at=datetime.now(),
    updated_at=datetime.now()
  )

  raincoat = Product(
    seller_id=3,
    name="Frisco Rubber Ducky Dog Raincoat",
    image_url="https://img.chewy.com/is/image/catalog/224910_MAIN._SY630_V1599819382_.jpg",
    description="Remember to measure your pet for the paw-fect fit. Duck, duck, gear up—keep the weather from raining on your parade with the Frisco Dog Rubber Ducky Raincoat. This doggy raincoat is water-resistant to help keep your pup dry come drizzle or downpour, and it's fit with secure belly straps to ensure a snug fit—and a drier pooch. The built-in leash hole lets you attach a leash to a collar worn underneath the raincoat, so you can always be ready to dash, and the cute ducky print is stylishly Insta-worthy. Plus, it's available in different sizes to fit pups of most proportions.",
    price=17.99,
    category_id=8,
    created_at=datetime.now(),
    updated_at=datetime.now()
  )

  bow_tie = Product(
    seller_id=3,
    name="Frisco Polka Dot Dog & Cat Bow Tie",
    image_url="https://i.pinimg.com/564x/15/ea/4b/15ea4bf85bfcce5e52305ee7aca60210.jpg",
    description="Get your pup or kitty ready to make a fashion statement with the Frisco Polka Dot Dog & Cat Bow Tie. It goes on with a hook-and-loop fastener around your pal's neck for that polished look. Choose from a teal, red, or navy polka dot pattern to find the perfect pop of posh for your pet. The white collar makes it look so realistic, too. It also comes in two sizes with a wide fastener so you can adjust it for the right fit.",
    price=2.35,
    category_id=8,
    created_at=datetime.now(),
    updated_at=datetime.now()
  )

  fleece_vest = Product(
    seller_id=3,
    name="Frisco Plaid Dog & Cat Fleece Vest",
    image_url="https://img.chewy.com/is/image/catalog/224279_MAIN._AC_SL1500_V1599003697_.jpg",
    description="A stylish fleece vest makes a great addition to anyone's cold-weather wardrobe, even your pet! These cozy, polyester fleece vests are made with stretchy, high-pile plush fleece material that work great as a standalone vest or layering piece to help your dog stay comfy through cold weather. They're also made with a pullover design, so there's no need to fumble with hook-and-loop fasteners or snaps. Plus, they come in two classic plaid patterns which is a staple of winter style!",
    price=7.50,
    category_id=8,
    created_at=datetime.now(),
    updated_at=datetime.now()
  )

  party_hat = Product(
    seller_id=3,
    name="Frisco Confetti Dog & Cat Birthday Hat",
    image_url="https://img.chewy.com/is/image/catalog/191275_Main._AC_SL400_V1582053292_.jpg",
    description="Invite all your pet's friends over for a birthday party—because we have the perfect party hat for the birthday pup or kitty! Confetti print, colorful trimming and a fluffy ball on top. Yup, bring on the selfies and cuteness overload. Plus, it comes with adjustable chin straps so it stays on, even if the party gets wild.",
    price=8.60,
    category_id=8,
    created_at=datetime.now(),
    updated_at=datetime.now()
  )

  db.session.add(blue_buffalo)
  db.session.add(pedigree)
  db.session.add(purina)
  db.session.add(kibbles)
  db.session.add(hills)
  db.session.add(moose)
  db.session.add(ball)
  db.session.add(zebra)
  db.session.add(pig)
  db.session.add(leprechaun)
  db.session.add(fancy_feast)
  db.session.add(iams)
  db.session.add(friskies)
  db.session.add(nine_lives)
  db.session.add(sheba)
  db.session.add(teaser)
  db.session.add(springs)
  db.session.add(mice)
  db.session.add(butterfly)
  db.session.add(scratcher)
  db.session.add(feline_pine)
  db.session.add(tidy_cats)
  db.session.add(scoopable)
  db.session.add(naturally_fresh)
  db.session.add(scoopfree)
  db.session.add(elevated_dog_bowls)
  db.session.add(slow_feeder)
  db.session.add(stainless_bowl)
  db.session.add(ceramic_bowl)
  db.session.add(cat_bowl)
  db.session.add(paw_butter)
  db.session.add(oatmeal_shampoo)
  db.session.add(dog_brush)
  db.session.add(brush_gloves)
  db.session.add(deodorizing_shampoo)
  db.session.add(hawaiian_shirt)
  db.session.add(raincoat)
  db.session.add(bow_tie)
  db.session.add(fleece_vest)
  db.session.add(party_hat)

  db.session.commit()


def undo_products():
  db.session.execute('TRUNCATE products RESTART IDENTITY CASCADE;')
  db.session.commit()
