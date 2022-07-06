import styles from './Header.module.css';
import React from 'react';
import cn from 'classnames';

export const Header = ({ children }) => {
  return (
    <header className='w-full'>
      {children}
    </header>);
};
