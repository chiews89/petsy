import React, { useState } from "react";
import { Modal } from "../../../context/Modal";
import AddProduct from "./AddProduct";
import './AddProduct.css';

const AddProductModal = () => {
  const [showModal, setShowModal] = useState(false);

  return (
    <>
      <button className="add-product-modal" onClick={() => setShowModal(true)}>
        Add Product
      </button>
      {showModal && (
        <Modal onClose={() => setShowModal(false)}>
          <AddProduct onClose={() => setShowModal(false)} />
        </Modal>
      )}
    </>
  );
};

export default AddProductModal
