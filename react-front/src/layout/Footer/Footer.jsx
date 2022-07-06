import styles from './Footer.module.css';
import cn from 'classnames';
import React from 'react';

export const Footer = ({ children, ...props }) => {
  return (
    <div className="bg-indigo-800 w-screen">
      <footer className="max-w-7xl m-auto bg-indigo-800 text-white">
        footer
        {children}
      </footer>
    </div>
  );
};
