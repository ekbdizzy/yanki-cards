import {HelperProps} from "./Helper.props";
import styles from './Helper.module.css';
import addIcon from './icons/icon_add.svg';
import updateIcon from './icons/icon_update.svg';
import saveIcon from './icons/icon_save.svg';
import exportIcon from './icons/icon_export.svg';
import cn from "classnames";


export const Helper = ({children, size = 'small', icon = 'none', ...props}: HelperProps): JSX.Element => {
    return (
        <span className={styles.helper} {...props}>
            <span className={cn({
                [styles.small]: size == 'small',
                [styles.medium]: size == 'medium'
            })}>{children}</span>

            {icon == 'add' && <img className={cn(styles.icon, {
                [styles.small_icon]: size == 'small',
                [styles.medium_icon]: size == 'medium'
            })} alt='' src={addIcon}/>}

            {icon == 'update' && <img className={cn(styles.icon, {
                [styles.small_icon]: size == 'small',
                [styles.medium_icon]: size == 'medium'
            })} alt='' src={updateIcon}/>}

            {icon == 'export' && <img className={cn(styles.icon, {
                [styles.small_icon]: size == 'small',
                [styles.medium_icon]: size == 'medium'
            })} alt='' src={exportIcon}/>}

            {icon == 'save' && <img className={cn(styles.icon, {
                [styles.small_icon]: size == 'small',
                [styles.medium_icon]: size == 'medium'
            })} alt='' src={saveIcon}/>}
        </span>
    );
};
