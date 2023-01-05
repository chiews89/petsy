import { useState, useEffect } from "react";
import { useDispatch } from "react-redux";
import { populateCart, subtractFromCart, removeFromCart } from "../../store/cart";
import { updateCount } from "../../store/cart";

const CartItem = ({ item }) => {
  const dispatch = useDispatch()
  const [count, setCount] = useState(item?.count)

  useEffect(() => {
    setCount(item?.count)
  }, [item?.count])

  return (
    <li className='cart-item'>
      <div className="cart-name-and-price-container">
        <div className='cart-item-name'> {item?.name} </div>
        <div className='cart-item-price'>$ {parseFloat(item?.price * item.count).toFixed(2)}</div>
      </div>
      <div className="cart-item-functions">
        <button
          className="cart-function-buttons"
          onClick={() => dispatch(subtractFromCart(item))}
        > - </button>
        <form onSubmit={(e) => {
          e.preventDefault()
          dispatch(updateCount(item, Number(count)))
        }}>
          <input
            className="cart-number-input"
            type="number"
            value={count}
            onChange={(e) => setCount(e.target.value)}
            onBlur={() => dispatch(updateCount(item, Number(count)))}
            min={1}
          />
        </form>
        <button
          className="cart-function-buttons"
          onClick={() => dispatch(populateCart(item))}
        > + </button>
        <button
          className="cart-function-buttons-remove"
          onClick={() => dispatch(removeFromCart(item?.id))}
        > Remove </button>
      </div>
    </li>
  )

}

export default CartItem
