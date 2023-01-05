import { useState, useEffect } from "react";
import { useSelector, useDispatch } from "react-redux";
import { useHistory } from "react-router-dom";
import { addAProduct } from "../../../store/products";
import { getCategories } from '../../../store/category';

const AddProduct = ({ onClose }) => {
  const dispatch = useDispatch();
  const history = useHistory();
  const user = useSelector((state) => state.session.user);
  const categoriesObj = useSelector(state => state.categories);
  const categories = Object.values(categoriesObj);

  const [name, setName] = useState("");
  const [image_url, setImageUrl] = useState("");
  const [description, setDescription] = useState("");
  const [price, setPrice] = useState(1);
  const [category_id, setCategoryId] = useState("");
  const [errors, setErrors] = useState([]);

  useEffect(() => {
    dispatch(getCategories());
  }, [dispatch]);

  useEffect(() => {
    if (!user) {
      history.push("/");
    }
  }, [user, history]);

  useEffect(() => {
    const validationErrors = [];

    if (image_url.length > 0 && !image_url.match(/^https?:\/\/.+\/.+$/))
    validationErrors.push("Please provide a valid URL");

    setErrors(validationErrors);
  }, [image_url, price]);

  const newProductSubmit = async (e) => {
    e.preventDefault();

    const payload = {
      userId: user.id,
      name,
      image_url,
      description,
      price,
      category_id,
    };
    const newProduct = await dispatch(addAProduct(payload));
    if (newProduct) {
      history.push(`/products/${newProduct.id}`);
    }
  };

  return (
    <form className="new-product-container" onSubmit={newProductSubmit}>
      <h2>List Your Product</h2>
      <ul>
        {errors.map((error, ind) => (
          <li className="error-list" key={ind}>{error}</li>
        ))}
      </ul>
      <div>
        <label> Name </label>
        <input
          id="form-label-name"
          placeholder="Name"
          value={name}
          onChange={(e) => setName(e.target.value)}
          className="edit_product_input-bar"
          required
        />
      </div>
      <div>
        <label> Image </label>
        <input
          id="form-label-image"
          type="text"
          placeholder="Image"
          value={image_url}
          onChange={(e) => setImageUrl(e.target.value)}
          className="edit_product_input-bar"
          required
        />
      </div>
      <div>
        <label> Description </label>
        <textarea
          id="form-label-description"
          placeholder="Description"
          value={description}
          onChange={(e) => setDescription(e.target.value)}
          className="edit_product_description_input-bar"
          required
        />
      </div>
      <div>
        <label> Price </label>
        <input
          id="form-label-price"
          type="number"
          min="1"
          placeholder="Price"
          value={price}
          onChange={(e) => setPrice(e.target.value)}
          className="edit_product_input-bar"
          required
        />
      </div>
      <div className="category-input">
        <label> Category </label>
        <select
          id="form-label-category"
          value={category_id}
          onChange={(e) => setCategoryId(e.target.value)}
          className='edit_product_category_input_bar'
          required
        >
          <option value=''>Please choose an option</option>
          {categories?.map(category => <option key={category.id} value={category.id}>{category.name}</option>)}
        </select>
      </div>
      <div className="add-product">
        <button
          className="add-product-button"
          type="submit"
          disabled={errors.length > 0 || !name || !image_url || !description || !category_id}
        >
          Submit
        </button>
        <button className="cancel-add-button" type="true" onClick={onClose}>
          Cancel
        </button>
      </div>
    </form>
  );
};

export default AddProduct;
