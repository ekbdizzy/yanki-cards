import styles from './Header.module.css';
import React from 'react';
import cn from 'classnames';

export const Header = ({ children, ...props }) => {
  return (
    <header className={cn(styles.header, {})}
            {...props}>
      {children}
    </header>);
};
