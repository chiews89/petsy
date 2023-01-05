import React, { useState } from "react";
import { Modal } from "../../../context/Modal";
import EditProduct from "./EditProduct";
import './EditProduct.css'

const EditProductModal = () => {
  const [showModal, setShowModal] = useState(false);

  return (
    <>
      <button className="edit-product-modal" onClick={() => setShowModal(true)}>
        Edit Your Product
      </button>
      {showModal && (
        <Modal onClose={() => setShowModal(false)}>
          <EditProduct onClose={() => setShowModal(false)}/>
        </Modal>
      )}
    </>
  );
};

export default EditProductModal;
