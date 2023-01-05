import React from 'react';
import { useSelector } from 'react-redux';
import { Link } from 'react-router-dom';
import './Results.css';

const Results = () => {
    let rslts = useSelector(state => state.results)
    let results = Object.values(rslts)

    if (!results.length) {
        return (
            <div className='no-results'>No results found!</div>
        )
    } else if (results.length) {
        return (
            <main className="products-main">
                <div className="products-content">
                    {results?.map((result) => (
                        <Link
                            key={`single_product_link_${result?.id}`}
                            to={`/products/${result?.id}`}
                        >
                            <div className="all-products-container">
                                <div className="product_images">
                                    <img
                                        height={250}
                                        alt={result?.name}
                                        src={
                                            result?.image_url
                                                ? result?.image_url
                                                : "https://media.istockphoto.com/vectors/no-image-available-sign-vector-id922962354?k=20&m=922962354&s=612x612&w=0&h=f-9tPXlFXtz9vg_-WonCXKCdBuPUevOBkp3DQ-i0xqo="
                                        }
                                    />
                                </div>
                                <div className="product_name">{result?.name}</div>
                                <div className="product_price">${parseFloat(result?.price).toFixed(2)}</div>
                            </div>
                        </Link>
                    ))}
                </div>
            </main>
        )
    }
}

export default Results;
