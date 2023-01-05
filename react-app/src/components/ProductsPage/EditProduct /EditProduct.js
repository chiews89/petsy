import { useState, useEffect } from "react";
import { useSelector, useDispatch } from "react-redux";
import { useHistory, useParams } from "react-router-dom";
import { editOneProduct } from "../../../store/products";
import { getCategories } from '../../../store/category';

const EditProduct = ({ onClose }) => {
  const dispatch = useDispatch();
  const history = useHistory();

  const { id } = useParams();
  const product = useSelector((state) => state.productsReducer[id]);
  const categoriesObj = useSelector(state => state.categories);
  const categories = Object.values(categoriesObj);

  const [name, setName] = useState(product?.name || "");
  const [image_url, setImageUrl] = useState(product?.image_url || "");
  const [description, setDescription] = useState(product?.description || "");
  const [price, setPrice] = useState(product?.price || "");
  const [category_id, setCategoryId] = useState(product?.category_id || "");
  const [created_at] = useState(product?.created_at || "");
  const [errorValidator, setErrorValidator] = useState([]);

  useEffect(() => {
    const errors = [];
    if (!name) errors.push("Please provide a name");
    if (!image_url.length) errors.push("Please provide a valid URL");
    if (image_url.length > 0 && !image_url.match(/^https?:\/\/.+\/.+$/))
      errors.push("Please provide a valid URL");
    if (!description) errors.push("Please provide a description");
    if (!price) errors.push("Please provide a price");
    if (!category_id) errors.push('Please provide a category');
    setErrorValidator(errors)
    dispatch(getCategories());
  }, [name, image_url, description, price, category_id, dispatch]);

  useEffect(() => {
    if (product) {
      setName(product.name);
      setImageUrl(product.image_url);
      setDescription(product.description);
      setPrice(product.price);
      setCategoryId(product.category_id);
    }
  }, [product]);

  const handleEditSubmit = async (e) => {
    e.preventDefault();
    const payload = {
      ...product,
      name,
      image_url,
      description,
      price,
      category_id,
      created_at,
    };

    const updatedProduct = await dispatch(editOneProduct(payload));
    if (updatedProduct) {
      history.push(`/products/${product.id}`);
      onClose(false);
    }
  };

  return (
    <div className="edit-product-container">
      <form className="edit-product" onSubmit={handleEditSubmit}>
        <ul>
          {errorValidator.map((error) => (
            <li className="error-list" key={error}>{error}</li>
          ))}
        </ul>
        <div className="name-input">
          <label> Name </label>
          <input
            id="form-label-name"
            placeholder="Name"
            value={name}
            onChange={(e) => setName(e.target.value)}
            className="edit_product_input-bar"
          />
        </div>
        <div className="image-input">
          <label> Image </label>
          <input
            id="form-label-image"
            type="text"
            placeholder="Image"
            value={image_url}
            onChange={(e) => setImageUrl(e.target.value)}
            className="edit_product_input-bar"
          />
        </div>
        <div className="description-input">
          <label> Description </label>
          <textarea
            id="form-label-description"
            placeholder="Description"
            value={description}
            onChange={(e) => setDescription(e.target.value)}
            className="edit_product_description_input-bar"
          />
        </div>
        <div className="price-input">
          <label> Price </label>
          <input
            id="form-label-price"
            type="number"
            step="0.01"
            pattern="^(./d{1,2}?$)"
            placeholder="Price"
            value={price}
            onChange={(e) => setPrice(e.target.value)}
            className="edit_product_input-bar"
          />
        </div>
        <div className="category-input">
          <label> Category </label>
          <select
            id="form-label-category"
            value={category_id}
            onChange={(e) => setCategoryId(e.target.value)}
            className='edit_product_category_input_bar'
          >
            <option value=''>Please choose an option</option>
            {categories?.map(category => <option key={category.id} value={category.id}>{category.name}</option>)}
          </select>
        </div>
        <div className="created-at-input">
          <input type="hidden" value={created_at} />
        </div>
        <button className="edit-product-button" type="submit" disabled={errorValidator.length > 0}>
          Submit
        </button>
        <button className="cancel-edit-button" onClick={onClose}>
          Cancel
        </button>
      </form>
    </div>
  );
};

export default EditProduct;
