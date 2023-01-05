import React, { useState, useEffect } from 'react';
import { BrowserRouter, Route, Switch } from 'react-router-dom';
import { useDispatch } from 'react-redux';
import LoginForm from './components/auth/LoginForm';
import SignUpForm from './components/auth/SignUpForm';
import NavBar from './components/NavBar';
import HomePage from './components/HomePage';
import ProtectedRoute from './components/auth/ProtectedRoute';
import User from './components/User/User';
import Results from './components/Results';
import AllProducts from './components/ProductsPage/AllProducts';
import SingleProduct from './components/ProductsPage/ProductDetail';
import CategoryPage from './components/CategoryPage';
import MissingPage from './components/MissingPage';
import Footer from './components/Footer';
import { authenticate } from './store/session';
import { findResults } from './store/results'
import { refreshCart } from './store/cart'
import { getAllProducts } from './store/products';

function App() {
  const [loaded, setLoaded] = useState(false);
  const dispatch = useDispatch();

  let term = ""
  if (localStorage.search) term = localStorage.search
  let sameCart = {}
  let jsonCart;
  if (localStorage.cart) {
    sameCart = localStorage.cart
    jsonCart = JSON.parse(`${sameCart}`)
  }

  useEffect(() => {
    (async () => {
      await dispatch(authenticate())
      await dispatch(getAllProducts())
      await dispatch(findResults(term))
      await dispatch(refreshCart(jsonCart))

      setLoaded(true);
    })();
  }, [dispatch, term, jsonCart]);

  if (!loaded) {
    return null;
  }

  return (
    <BrowserRouter>
      <NavBar />
      <Switch>
        <Route path="/" exact={true}>
          <HomePage />
        </Route>
        <Route path="/login" exact={true}>
          <LoginForm />
        </Route>
        <Route path="/sign-up" exact={true}>
          <SignUpForm />
        </Route>
        <Route path="/categories/:id" exact={true}>
          <CategoryPage />
        </Route>
        <Route path="/products" exact={true}>
          <AllProducts />
        </Route>
        <Route path="/products/:id" exact={true}>
          <SingleProduct />
        </Route>
        <ProtectedRoute path='/profile' exact={true} >
          <User />
        </ProtectedRoute>
        <Route path="/results" exact={true}>
          <Results />
        </Route>
        <Route>
          <MissingPage />
        </Route>
      </Switch>
      <Footer />
    </BrowserRouter>
  );
}

export default App;
