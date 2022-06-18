import {DetailedHTMLProps, HTMLAttributes, ReactNode} from "react";


export interface HProps extends DetailedHTMLProps<HTMLAttributes<HTMLHeadingElement>, HTMLHeadingElement> {
    children: ReactNode
    tag: 'h1' | 'h2'
}
