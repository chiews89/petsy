import React, { useState } from 'react';
import { useHistory, Link } from 'react-router-dom';
import { useDispatch, useSelector } from 'react-redux';
import { findResults } from '../store/results';

const SearchBar = () => {
    const products = useSelector(state => state.productsReducer)
    const [searchTerm, setSearchTerm] = useState('');
    const history = useHistory();
    const dispatch = useDispatch();

    let allProducts = Object.values(products)

    const handleSubmit = (e) => {
        e.preventDefault()

        localStorage.setItem("search", searchTerm)

        dispatch(findResults(searchTerm))

        setSearchTerm("")

        history.push('/results');
    }

    let count = 0

    return (
        <>
            <form onSubmit={handleSubmit} className='search-form'>
                <input type='text'
                    placeholder='Search Products'
                    name='search'
                    value={searchTerm}
                    onChange={e => setSearchTerm(e.target.value)}
                    required
                />
                <button>
                    <i className="fas fa-search"></i>
                </button>
            </form>
            <div hidden={!searchTerm} className='search-bar-results-div'>
                <ul>
                    {allProducts.map((product) => {
                        if (product?.name.toLowerCase().includes(searchTerm.toLowerCase())) {
                            count++
                            return (
                                <li key={product.id}>
                                    <Link to={`/products/${product.id}`}
                                        onClick={() => setSearchTerm('')}
                                    >
                                        {product.name}
                                    </Link>
                                </li>)
                        } else {
                            return null;
                        }
                    })}
                    {!count ? <li> No results found </li> : null}
                </ul>
            </div>
        </>
    )
}

export default SearchBar;
