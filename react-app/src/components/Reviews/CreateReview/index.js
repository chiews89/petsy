import React, { useState } from "react";
import { Modal } from "../../../context/Modal";
import CreateReview from "./CreateReview";
import "./CreateReview.css"

const AddReviewModal = () => {
  const [showModal, setShowModal] = useState(false);

  return (
    <>
      <button className="create-review-modal" onClick={() => setShowModal(true)}>
        Add Your Review
      </button>
      {showModal && (
        <Modal onClose={() => setShowModal(false)}>
          <CreateReview onClose={() => setShowModal(false)}/>
        </Modal>
      )}
    </>
  );
};

export default AddReviewModal;
