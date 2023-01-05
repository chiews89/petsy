import React, { useState, useEffect } from 'react';
import { NavLink } from 'react-router-dom';
import LogoutButton from '../auth/LogoutButton';

const ProfileButton = () => {
    const [showMenu, setShowMenu] = useState(false);

    const openMenu = () => {
        if (showMenu) return;
        setShowMenu(true);
    };

    useEffect(() => {
        if (!showMenu) return;

        const closeMenu = () => {
            setShowMenu(false);
        };

        document.addEventListener('click', closeMenu);

        return () => document.removeEventListener('click', closeMenu);
    }, [showMenu]);

    return (
        <>
            <button className='user-icon-button' onClick={openMenu}>
                <div className='user-icon'>
                    <i className="fas fa-user"></i>
                </div>
            </button>
            {showMenu && (
                <div className='profile-dropdown'>
                    <ul>
                        <li className='order-history-li'>
                            <NavLink to='/profile' exact={true} className='order-history'>Order History</NavLink>
                        </li>
                        <li className='logout-li'>
                            <LogoutButton />
                        </li>
                    </ul>
                </div>
            )}
        </>
    )
};

export default ProfileButton;
