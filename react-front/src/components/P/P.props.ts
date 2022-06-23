import {DetailedHTMLProps, HTMLAttributes, ReactNode} from "react";

export interface PProps extends DetailedHTMLProps<HTMLAttributes<HTMLParagraphElement>, HTMLParagraphElement> {
    children: ReactNode
    center?: boolean
    size?: 'normal' | 'big'
    color?: 'primary' | 'cyan' | 'purple'
}
