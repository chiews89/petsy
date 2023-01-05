import { useEffect } from "react";
import { useSelector, useDispatch } from "react-redux";
import { useParams, useHistory } from "react-router-dom";
import { populateCart } from "../../../store/cart";
import { getSingleProduct, deleteSingleProduct } from "../../../store/products";
import EditProductModal from "../EditProduct ";
import AllReviews from "../../Reviews/GetReviews";
import Reviews from "../../Reviews/CreateReview";
import "./ProductDetail.css";

const SingleProduct = () => {
  const dispatch = useDispatch();
  const history = useHistory();
  const { id } = useParams();
  const productId = +id;

  const product = useSelector((state) => state.productsReducer[id]);
  const userId = useSelector((state) => state.session.user?.id);
  const reviews = useSelector((state) => state.reviewsReducer);
  const reviewsArr = Object.values(reviews);
  const productReviews = reviewsArr.filter(
    (review) => review.product_id === productId
  );

  useEffect(() => {
    dispatch(getSingleProduct(id));
  }, [dispatch, id]);

  if (!product) {
    return null;
  }

  async function handleDelete(e) {
    e.preventDefault();
    await dispatch(deleteSingleProduct(id));
    history.push("/products");
  }

  async function handleAddToCart(e, product) {
    e.preventDefault()
    await dispatch(populateCart(product))
    // window.alert(`${product?.name} added to your cart!`)
  }


  const overallRating = (productReviews) => {
    return productReviews?.reduce(function (prevValue, review) {
      return prevValue + review.rating;
    }, 0);
  };

  let rating = Math.round(
    overallRating(productReviews) / productReviews.length
  );


  return (
    <div className="product_detail-container">
      <div className="product">
        <div className="product-image">
          <img
            width={350}
            height={450}
            alt={product?.name}
            src={
              product?.image_url
                ? product?.image_url
                : "https://media.istockphoto.com/vectors/no-image-available-sign-vector-id922962354?k=20&m=922962354&s=612x612&w=0&h=f-9tPXlFXtz9vg_-WonCXKCdBuPUevOBkp3DQ-i0xqo="
            }
          />
          <div className="reviews-display">
            {userId && userId !== product?.seller_id && (
              <div className="add-review-modal">
                <Reviews />
              </div>
            )}
            <h3>
              {productReviews?.length} Reviews{" "}
              {rating > 0 &&
                Array(rating)
                  .fill(
                    <span>
                      <i className="fas fa-star"></i>
                    </span>
                  )
                  .map((star, idx) => <span key={idx}>{star}</span>)}
            </h3>
            <AllReviews />
          </div>
        </div>
        <div className="product-info-container">
          <div>
            {productReviews?.length} review(s) |  {rating > 0 &&
              Array(rating)
                .fill(
                  <span>
                    <i className="fas fa-star"></i>
                  </span>
                )
                .map((star, idx) => <span key={idx}>{star}</span>)}
          </div>
          <h2 className="product-name">{product.name}</h2>
          <h4 className="product-category">{product.category_name}</h4>

          <div className="product-price">
            $ {parseFloat(product.price).toFixed(2)}
          </div>
          {userId !== product.seller_id && <h3>{"✓ "} In Stock </h3>}

          {/* <select className="size-selector">
            <option value="" selected="">
              Select an option
            </option>
            <option>Small</option>
            <option>Medium</option>
            <option>Large</option>
          </select> */}
          {userId && userId !== product.seller_id && (
            <button
              className="add-to-cart-btn"
              onClick={(e) => handleAddToCart(e, product)}
            >
              Add to Cart
            </button>

          )}
          <div className="product-btn-container">
            {userId && userId === product.seller_id && <EditProductModal />}
            {userId && userId === product.seller_id && (
              <button className="delete-product-button" onClick={handleDelete}>
                Delete Your Product
              </button>
            )}
          </div>
          <div className="bottom-right-container">
            <h2 className="product-description">Description</h2>
            <div>{product.description}</div>

            <h2 className="shipping-return">Shipping and return policies</h2>
            <p>
              If, for any reason, you are not completely satisfied with a purchase, we invite you to review our policy on refunds and returns.
            </p>
            <h2 className="faqs">FAQs</h2>
            <p>
              <b>Can I use this if I have a cat?</b>
              <p>
                Chase ball of string eat plants, meow, and throw up because I ate plants going to catch the red dot today going to catch the red dot today. I could pee on this if I had the energy. Chew iPad power cord steal the warm chair right after you get up for purr for no reason leave hair everywhere, decide to want nothing to do with my owner today.
              </p>
              <b>Can I use this if I have a dog?</b>
              <p>Doing me a frighten heck fluffer yapper what a nice floof, such treat very good spot doggo. Maximum borkdrive smol borking doge with a long snoot for pats shibe very good spot wow very biscit blep, blop yapper woofer waggy wags. Borking dog maximum borkdrive wow such tempt very hand that feed shibe, stop it cat. Woof you are doin me a concern, that tongue though. Much borkdrive.</p>
            </p>
            <h2 className="seller-name">Meet Your Seller</h2>
            <h3>{product.username}</h3>
          </div>
        </div>
      </div>
    </div>
  );
};

export default SingleProduct;
