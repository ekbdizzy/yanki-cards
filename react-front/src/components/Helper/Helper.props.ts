import {DetailedHTMLProps, HTMLAttributes, ReactNode} from "react";

export interface HelperProps extends DetailedHTMLProps<HTMLAttributes<HTMLAnchorElement>, HTMLAnchorElement> {
    children: ReactNode
    size: 'small' | 'medium'
    icon?: 'add' | 'update' | 'save' | 'export' | 'none'
}
