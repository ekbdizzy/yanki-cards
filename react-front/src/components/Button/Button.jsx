import React from 'react';
import styles from './Button.module.scss';
import cn from 'classnames';
import {
  RefreshIcon,
  PlusIcon,
  GlobeAltIcon,
  DocumentAddIcon,
} from '@heroicons/react/outline';

import {
  PencilAltIcon,
} from '@heroicons/react/solid';

export const Button = ({
  color = 'amber',
  size = 'medium',
  icon = null,
  isDisabled = false,
  children,
}) => {
  return (
    <button className={styles.button} disabled={isDisabled}>
      <span className={cn(styles.title, {
        [styles.amber]: color === 'amber',
        [styles.fuchsia]: color === 'fuchsia',
        [styles.small]: size === 'small',
        [styles.medium]: size === 'medium',
        [styles.large]: size === 'large',
      })}>{children}</span>
      {icon === 'refresh' && <RefreshIcon className={styles.icon}/>}
      {icon === 'new' && <PencilAltIcon className={styles.icon}/>}
      {icon === 'add' && <DocumentAddIcon className={styles.icon}/>}
      {icon === 'translate' && <GlobeAltIcon className={styles.icon}/>}
    </button>
  );
};

