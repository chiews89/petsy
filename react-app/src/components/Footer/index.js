import React from 'react';

import './Footer.css';

const Footer = () => {
    return (
        <div className='footer'>
            <div className='footer-content'>
                <div className='team-members'>
                    <p>Created By</p>
                    <ul>
                        <li>
                            <a href='https://github.com/chiews89' target='_blank' rel='noopener noreferrer' className='footer-links'>Chiew Saetern</a>
                        </li>
                        <li>
                            <a href='https://github.com/jameschen56' target='_blank' rel='noopener noreferrer' className='footer-links'>James Chen</a>
                        </li>
                        <li>
                            <a href='https://github.com/lrmaser' target='_blank' rel='noopener noreferrer' className='footer-links'>Laura Maser</a>
                        </li>
                        <li>
                            <a href='https://github.com/miajoubert' target='_blank' rel='noopener noreferrer' className='footer-links'>Mia Joubert</a>
                        </li>
                        {/* <li>
                            <a href='https://github.com/miajoubert/petsy' target='_blank' rel='noopener noreferrer' className='footer-links'>
                                <i className="fab fa-github"></i>
                            </a>
                        </li> */}
                    </ul>
                </div>
                <div className='technologies'>
                    <p>Technologies Used</p>
                    <ul>
                        <li>JavaScript</li>
                        <li>CSS</li>
                        <li>React</li>
                        <li>Redux</li>
                        <li>Flask</li>
                        <li>SQLAlchemy</li>
                        <li>Alembic</li>
                        <li>PostgreSQL</li>
                    </ul>
                </div>
            </div>
            <div className='footer-bottom'>
                <div>
                    <a href='https://github.com/miajoubert/petsy' target='_blank' rel='noopener noreferrer' className='footer-links'>
                        <i className="fab fa-github"></i>
                    </a>
                </div>
                <div className='footer-copyright'>© 2022 Petsy</div>
            </div>
        </div>
    );
};

export default Footer;
