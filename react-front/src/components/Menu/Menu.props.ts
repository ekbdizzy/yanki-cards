import {DetailedHTMLProps, HTMLAttributes, ReactNode} from "react";


export interface MenuProps extends DetailedHTMLProps<HTMLAttributes<HTMLUListElement>, HTMLUListElement> {
    children: ReactNode;
}
