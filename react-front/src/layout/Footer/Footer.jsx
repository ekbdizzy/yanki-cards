import styles from './Footer.module.css';
import cn from 'classnames';
import React from 'react';

export const Footer = ({ children, ...props }) => {
  return (
    <footer className={cn(styles.footer, {})}
            {...props}>
      Some info in footer
      {children}
      footer
    </footer>
  );
};
