import { useSelector, useDispatch } from "react-redux";
import { useHistory } from 'react-router-dom';
import CartItem from "./CartItem";
import { submitOrder } from "../../store/orders";
import { resetCart } from "../../store/cart";
import './Cart.css'

const Cart = ({ showCart }) => {
    let cart = useSelector(state => state.cart);
    const products = useSelector(state => state.productsReducer)
    const dispatch = useDispatch();
    const history = useHistory();

    const cartItems = Object.values(cart)
        .map(item => {
            return {
                ...item,
                ...products[item.id]
            }
        });

    if (!cartItems.length) return null

    const handleSubmit = (e) => {
        e.preventDefault();

        let order_number = Date.now();

        Object.values(cart)
            .map(item => {
                const payload = {
                    order_number,
                    product_id: item.id,
                    quantity: item.count
                }
                return dispatch(submitOrder(payload))
            });

        dispatch(resetCart());
        localStorage.removeItem('cart');
        showCart(false)
        history.push('/profile');
    }

    let subtotal = parseInt(0);
    cartItems.map(item => parseFloat(subtotal += parseFloat(item.price * item.count)).toFixed(2))

    return (
        <div className='cart'>
            <ul className="cart-list">
                {cartItems.map(item => <CartItem key={item.id} item={item} />)}
            </ul>
            <hr />
            <div className='cart-totals-container'>
                <div className="cart-totals-div">
                    <div> Subtotal: $ {parseFloat(subtotal).toFixed(2)} </div>
                    <div> Tax: $ {parseFloat(subtotal * .055).toFixed(2)} </div>
                    <div className="cart-total"><b> Total: $ {parseFloat(subtotal * 1.055).toFixed(2)} </b></div>
                </div>
                <form onSubmit={handleSubmit}>
                    <button
                        className="submit-cart-button"
                        type="submit"
                    >
                        Submit Order
                    </button>
                </form>
            </div>
        </div>
    )
}

export default Cart;
