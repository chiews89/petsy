import { useEffect } from "react";
import { useSelector, useDispatch } from "react-redux";
import { useParams } from "react-router-dom";
import { getAllReviews } from "../../../store/reviews";
import { deleteAReview } from "../../../store/reviews";
import { useHistory } from "react-router-dom";
import EditReviewModal from "../EditReview";
import "./Reviews.css";

const AllReviews = () => {
  const dispatch = useDispatch();
  const { id } = useParams();
  const userId = useSelector((state) => state.session.user?.id);
  const reviews = useSelector((state) => state.reviewsReducer);
  const product = useSelector((state) => state.productsReducer[id]);
  const history = useHistory();
  const reviewsArr = Object.values(reviews);

  useEffect(() => {
    dispatch(getAllReviews());
  }, [dispatch]);

  function handleReviewDelete(e, reviewId) {
    e.preventDefault();
    dispatch(deleteAReview(reviewId));
    history.push(`/products/${id}`);
  }

  return (
    <div className="reviews-content">
      {reviewsArr.map((review) => {
        if (review.product_id === product.id) {
          return (
            <div key={review?.id} className="review-container">
              <div className="user-name">{review.username}{" "}{review.created_at.slice(5, 17)}</div>
              <div className="star-rating">
                {Array(review.rating)
                  .fill(
                    <span>
                      <i className="fas fa-star fa-xs"></i>
                    </span>
                  )
                  .map((star, idx) => (
                    <span key={idx}>{star}</span>
                  ))}
              </div>
              <div className="date"></div>
              <div>{review?.review}</div>
              {userId === review.buyer_id && (
                <div>
                  <EditReviewModal reviewId={review?.id} />
                  <button
                    className="delete-review-button"
                    onClick={(e) => handleReviewDelete(e, review?.id)}
                  >
                    Delete Your Review
                  </button>
                </div>
              )}
            </div>
          );
        } else return null;
      })}

    </div>
  );
};

export default AllReviews;
