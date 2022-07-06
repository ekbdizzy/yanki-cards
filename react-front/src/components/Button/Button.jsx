import React from 'react';
import styles from './Button.module.scss';
import cn from 'classnames';
import {
  RefreshIcon,
} from '@heroicons/react/outline';

import { PencilAltIcon } from '@heroicons/react/solid';

export const Button = ({ color = 'amber', size = 'medium', icon = null, children }) => {
  return (
    <button className={styles.button}>
      <span className={cn(styles.title, {
        [styles.amber]: color === 'amber',
        [styles.fuchsia]: color === 'fuchsia',
      })}>{children}</span>
      {icon === 'refresh' && <RefreshIcon className={styles.icon}/>}
      {icon === 'new' && <PencilAltIcon className={styles.icon}/>}
    </button>
  );
};

