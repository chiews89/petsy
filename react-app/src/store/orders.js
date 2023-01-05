const ADD_ORDER = 'orders/ADD_ORDER';
const GET_ORDERS = 'orders/GET_ORDERS';

const addOrder = (order) => {
    return {
        type: ADD_ORDER,
        order
    }
}

const getOrders = (orders) => {
    return {
        type: GET_ORDERS,
        orders
    }
}

export const submitOrder = (order) => async (dispatch) => {
    const res = await fetch('/api/orders', {
        method: 'POST',
        headers: {
            'Content-Type': 'application/json'
        },
        body: JSON.stringify(order)
    });

    if (res.ok) {
        const newOrder = await res.json();
        dispatch(addOrder(newOrder));
        return newOrder;
    }
}

export const listOrders = () => async (dispatch) => {
    const res = await fetch('/api/orders');

    if (res.ok) {
        const orders = await res.json();
        dispatch(getOrders(orders));
        return orders;
    }
}

const ordersReducer = (state = {}, action) => {
    let newState;
    switch (action.type) {
        case ADD_ORDER:
            newState = { ...state }
            return newState;
        case GET_ORDERS:
            newState = { ...state };
            action.orders.orders.forEach((order) => {
                newState[order.id] = order;
            });
            return newState;
        default:
            return state;
    }
}

export default ordersReducer;
