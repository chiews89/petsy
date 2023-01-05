import { useState, useEffect } from "react";
import { useSelector, useDispatch } from "react-redux";
import { Link } from "react-router-dom";
import { getAllProducts } from "../../../store/products";
import AddProductModal from "../AddProduct";
import './Products.css';

const AllProducts = () => {
  const [productList, setProductList] = useState([]);
  const dispatch = useDispatch();
  const products = useSelector(state => state.productsReducer);
  const user = useSelector((state) => state.session.user);

  useEffect(() => {
    dispatch(getAllProducts());
  }, [dispatch]);

  useEffect(() => {
    if (products) {
      setProductList(Object.values(products))
    }
  }, [products]);

  return (
    <main className="products-main">
      <h1>All Products</h1>
      {user ? <AddProductModal /> : null}
      <div className="products-content">
        {productList.length &&
          productList.map((product) => (
            <Link
              key={`single_product_link_${product?.id}`}
              to={`/products/${product?.id}`}
            >
              <div className="all-products-container">
                <div className="product_images">
                  <img
                    height={250}
                    alt={product?.name}
                    src={
                      product?.image_url
                        ? product?.image_url
                        : "https://media.istockphoto.com/vectors/no-image-available-sign-vector-id922962354?k=20&m=922962354&s=612x612&w=0&h=f-9tPXlFXtz9vg_-WonCXKCdBuPUevOBkp3DQ-i0xqo="
                    }
                  />
                </div>
                <div className="product_name">{product?.name}</div>
                <div className="product_price">$ {parseFloat(product?.price).toFixed(2)}</div>
              </div>
            </Link>
          ))}
      </div>
    </main>
  );
};

export default AllProducts;
