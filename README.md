# Petsy

Inspired by Etsy, Petsy is an e-commerce platform for pet enthusiasts where users can buy and sell pet products as well as leave ratings/reviews of their items.

# Index

- [Live Site](https://petsy-store.herokuapp.com/)
- [Feature List](https://github.com/miajoubert/petsy/wiki/Feature-List)
- [Database Schema](https://github.com/miajoubert/petsy/wiki/Database-Schema)
- [Frontend Routes](https://github.com/miajoubert/petsy/wiki/Frontend-Routes)
- [API Documentation](https://github.com/miajoubert/petsy/wiki/API-Routes)
- [User Stories](https://github.com/miajoubert/petsy/wiki/User-Stories)
- [Redux State](https://github.com/miajoubert/petsy/wiki/Redux-State)

# Technologies Used

<img src="https://cdn.jsdelivr.net/gh/devicons/devicon/icons/python/python-original.svg" height=40/><img src="https://cdn.jsdelivr.net/gh/devicons/devicon/icons/flask/flask-original.svg" height=40/><img src="https://cdn.jsdelivr.net/gh/devicons/devicon/icons/sqlalchemy/sqlalchemy-original.svg" height=40/><img  src="https://cdn.jsdelivr.net/gh/devicons/devicon/icons/javascript/javascript-original.svg"  height=40/><img src="https://cdn.jsdelivr.net/gh/devicons/devicon/icons/react/react-original.svg" height=40/><img src="https://cdn.jsdelivr.net/gh/devicons/devicon/icons/redux/redux-original.svg" height=40/><img src="https://cdn.jsdelivr.net/gh/devicons/devicon/icons/nodejs/nodejs-plain-wordmark.svg" height=40/><img  src="https://cdn.jsdelivr.net/gh/devicons/devicon/icons/css3/css3-original.svg"  height=40/><img  src="https://cdn.jsdelivr.net/gh/devicons/devicon/icons/html5/html5-original.svg"  height=40/><img  src="https://cdn.jsdelivr.net/gh/devicons/devicon/icons/git/git-original.svg"  height=40/><img src="https://cdn.jsdelivr.net/gh/devicons/devicon/icons/docker/docker-original.svg" height=40/><img  src="https://cdn.jsdelivr.net/gh/devicons/devicon/icons/vscode/vscode-original.svg"  height=40/>

# Getting started

1. Clone this repository

   ```git@github.com/miajoubert/petsy.git```

2. CD into the /app directory and install dependencies

    ```pipenv install```

3. CD into the /react-app directory and install dependencies

    ```npm install```

4.  Create a .env file based on the .env.example given

5.  Create a user in psql based on your .env DATABASE_URL app_name

    ```psql -c "CREATE USER <username> PASSWORD '<password>' CREATEDB"```

6.  Create a database in psql based on your.env DATABASE_URL app_db_name

7. Start your shell, migrate your database, seed your database, and run the flask app

   ```pipenv shell```

   ```flask db upgrade```

    ```flask seed all```

    ```flask run```

8. Open another terminal and change directory into /react-app and run the React app

	```npm start```


# Features

## Splash Page 
![Splash Page](https://user-images.githubusercontent.com/92398763/158102304-8f352a22-ad0c-439c-adb9-76e5443c0bc1.png)


## Login Page
![Login Page](https://user-images.githubusercontent.com/92398763/158102327-367a82cc-3970-4b1d-9a95-72e5861d6534.png)


## All Products Page
![All Products](https://user-images.githubusercontent.com/92398763/158102344-6089a025-b8af-485d-a335-5d18d43efcfe.png)


## Product Detail Page
![Product Detail Page](https://user-images.githubusercontent.com/92398763/158102357-e3531954-058f-4b94-b98a-d28d37d8b659.png)
![Product Detail Page2](https://user-images.githubusercontent.com/92398763/158102611-e5468205-6834-44b9-bfeb-69813fbc3f9a.png)


## Shopping Cart
![Shopping Cart](https://user-images.githubusercontent.com/92398763/158102398-57e590a3-dac1-4fd8-a7a3-f6efe05e6243.png)


## Order History
![Order History](https://user-images.githubusercontent.com/92398763/158102410-bbbff3f9-5a3f-47f9-8951-043dea0b9ac7.png)


## 404 Page Not Found 
![image](https://user-images.githubusercontent.com/87781597/158023261-a9b58781-45b6-47eb-a058-73bd005135f7.png)
# petsy
