import styles from './Feedback.module.css';
import cn from 'classnames';
import React from 'react';

export const Feedback = ({ children, ...props }) => {
  return (
    <div className={cn(styles.feedback, {})}
         {...props}>
      {children}
      feedback
    </div>
  );
};
