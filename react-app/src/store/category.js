const LOAD_CATEGORIES = "categories/LOAD_CATEGORIES";
const LOAD_CATEGORY = "categories/LOAD_CATEGORY";

const loadCategories = (categories) => {
  return {
    type: LOAD_CATEGORIES,
    categories,
  };
};

const loadCategory = (category) => {
  return {
    type: LOAD_CATEGORY,
    category,
  };
};

export const getCategories = () => async (dispatch) => {
  const res = await fetch("/api/categories");

  if (res.ok) {
    const categories = await res.json();
    dispatch(loadCategories(categories));
  }

  return res;
};

export const getCategory = (id) => async (dispatch) => {
  const res = await fetch(`/api/categories/${id}`);
  if (res.ok) {
    const category = await res.json();
    dispatch(loadCategory(category));
    return res;
  }
};

const categoriesReducer = (state = {}, action) => {
  let newState;
  switch (action.type) {
    case LOAD_CATEGORIES:
      newState = { ...state };
      action.categories.categories.forEach((category) => {
        newState[category.id] = category;
      });
      return newState;
    case LOAD_CATEGORY:
      newState = { ...state };
      newState[action.category.id] = action.category;
      return newState;
    default:
      return state;
  }
};

export default categoriesReducer;
