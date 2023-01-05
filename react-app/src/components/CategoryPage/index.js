import React, { useEffect } from "react";
import { useDispatch, useSelector } from "react-redux";
import { useParams, Link } from "react-router-dom";
import { getCategory } from "../../store/category";
import AddProductModal from "../ProductsPage/AddProduct";
import "./CategoryPage.css";

const CategoryPage = () => {
  const { id } = useParams();
  const category = useSelector((state) => state.categories[id]);
  const user = useSelector((state) => state.session.user);
  const dispatch = useDispatch()

  useEffect(() => {
    dispatch(getCategory(parseInt(id)));
  }, [dispatch, id]);

  return (
    <main className="products-main">
      <h1>{category?.name}</h1>
      {user ? <AddProductModal /> : null}
      <div className='products-content'>
        {category?.products.map(product => (
          <Link to={`/products/${product?.id}`}>
            <div key={product?.id} className='all-products-container'>
              <div className="product_images">
                <img
                  height={250}
                  alt={product?.name}
                  src={
                    product?.image_url
                      ? product?.image_url
                      : "https://media.istockphoto.com/vectors/no-image-available-sign-vector-id922962354?k=20&m=922962354&s=612x612&w=0&h=f-9tPXlFXtz9vg_-WonCXKCdBuPUevOBkp3DQ-i0xqo="
                  } />
              </div>
              <div className="product_name">{product?.name}</div>
              <div className="product_price">${parseFloat(product?.price).toFixed(2)}</div>
            </div>
          </Link>
        ))}
      </div>
    </main>
  )
};

export default CategoryPage;
