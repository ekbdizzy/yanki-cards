import {DetailedHTMLProps, HTMLAttributes, ReactNode} from "react";

export interface BadgeProps extends DetailedHTMLProps<HTMLAttributes<HTMLSpanElement>, HTMLSpanElement> {
    children: ReactNode;
}
