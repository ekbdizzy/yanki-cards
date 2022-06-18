import {InputProps} from "./Input.props";
import styles from './Input.module.css';


export const Input = ({value, ...props}: InputProps): JSX.Element => {
    return <input className={styles.input}
                  placeholder={value}
                  type='text'
        {...props}/>;
};
