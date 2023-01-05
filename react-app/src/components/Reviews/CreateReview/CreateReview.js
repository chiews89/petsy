import React, { useEffect, useState } from "react";
import { useDispatch } from "react-redux";
import { useSelector } from "react-redux";
import { useHistory, useParams } from "react-router-dom";
import { addAReview } from "../../../store/reviews";

const CreateReview = ({ onClose }) => {
  const dispatch = useDispatch();
  const { id } = useParams();
  const user = useSelector((state) => state.session.user?.id);
  const product = useSelector((state) => state.productsReducer[id]);
  const history = useHistory();

  const [review, setReview] = useState("");
  const [rating, setRating] = useState(1);
  const [errorValidator, setErrorValidator] = useState([]);

  useEffect(() => {
    const errors = [];

    if (rating < 1 || rating > 5) errors.push("Rating must be between 1 or 5");

    setErrorValidator(errors);
  }, [review, rating]);

  const handleSubmit = async (e) => {
    e.preventDefault();
    const payload = {
      buyer_id: user.id,
      product_id: product.id,
      review,
      rating,
    };

    const newReview = await dispatch(addAReview(payload));
    if (newReview) {
      history.push(`/products/${product.id}`);
      onClose(false);
    }
  };

  return (
    <div>
      <ul className="errors-list">
        {errorValidator.map((error) => (
          <li className="error-list" key={error}>
            {error}
          </li>
        ))}
      </ul>
      <form className="new-review-form" onSubmit={handleSubmit}>
        <div className="review">
          <label> Review </label>
          <textarea
            type="text"
            placeholder="Review"
            value={review}
            onChange={(e) => setReview(e.target.value)}
            className="add_review_input-bar"
            required
          />
        </div>
        <div className="rating">
          <label> Rating </label>
          <input
            type="number"
            min="1"
            max="5"
            step="1"
            value={rating}
            onChange={(e) => setRating(e.target.value)}
            className="add_rating_input-bar"
            required
          />
        </div>
        <div className="add-review">
          <button
            className="add-product-button"
            type="submit"
            disabled={errorValidator.length > 0 || !review || !rating}
          >
            Submit
          </button>
          <button className="cancel-add-button" type="true" onClick={onClose}>
            Cancel
          </button>
        </div>
      </form>
    </div>
  );
};

export default CreateReview;
