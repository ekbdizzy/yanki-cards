import {FeedbackProps} from "./Feedback.props";
import styles from './Feedback.module.css';
import cn from "classnames";


export const Feedback = ({children, ...props}: FeedbackProps): JSX.Element => {
    return <div className={cn(styles.Feedback, {})}
                {...props}>
        {children}
        feedback
    </div>;
};
