import React, { useEffect } from "react";
import { useDispatch, useSelector } from "react-redux";
import { Link } from "react-router-dom";

import { getAllProducts } from "../../store/products";
import { getCategories } from "../../store/category";
import "./HomePage.css";

const HomePage = () => {
  const dispatch = useDispatch();

  const categoriesObj = useSelector((state) => state.categories);
  const categories = Object.values(categoriesObj);

  useEffect(() => {
    dispatch(getAllProducts());
    dispatch(getCategories());
  }, [dispatch]);

  return (
    <main>
      <div className="home-banner">
        <h1>Explore items for all of your pet's needs</h1>
      </div>
      <div className='categories-container'>
        {categories?.map((category) => (
          <div key={category?.id} className="category-container">
            <h2>
              <Link to={`/categories/${category?.id}`}>
                {category?.name}
              </Link>
            </h2>
            <div className="home-category-products">
              {category?.products?.map((product) => (
                <Link
                  key={`single_product_link_${product?.id}`}
                  to={`/products/${product?.id}`}
                >
                  <div key={product?.id} className="product-card">
                    <div>
                      <img
                        className="home-product-image"
                        alt={product?.name}
                        src={
                          product?.image_url
                            ? product?.image_url
                            : "https://media.istockphoto.com/vectors/no-image-available-sign-vector-id922962354?k=20&m=922962354&s=612x612&w=0&h=f-9tPXlFXtz9vg_-WonCXKCdBuPUevOBkp3DQ-i0xqo="
                        }
                      />
                      <h3 className="home-product-name">{product?.name}</h3>
                      <h4 className="home-product-price">${parseFloat(product?.price).toFixed(2)}</h4>
                    </div>
                  </div>
                </Link>
              ))}
            </div>
          </div>
        ))}
      </div>
    </main>
  );
};

export default HomePage;
