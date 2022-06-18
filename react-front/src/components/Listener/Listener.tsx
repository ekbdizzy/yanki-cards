import {ListenerProps} from "./Listener.props";
import styles from './Listener.module.css';
import Duck from './duck.png';

export const Listener = ({person, ...props}: ListenerProps): JSX.Element => {
    return <div className={styles.listener}
        {...props} >
        <img src={Duck} alt=''/>
    </div>;
};
