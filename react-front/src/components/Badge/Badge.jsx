import React from 'react';
import styles from './Badge.module.scss';

export const Badge = ({ children }) => {
  return <span className={styles.badge}>
    {children}
  </span>;
};
