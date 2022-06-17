import {DetailedHTMLProps, HTMLAttributes} from "react";


export interface MenuItem {
    name: string,
    route: string
}

export interface MenuProps extends DetailedHTMLProps<HTMLAttributes<HTMLUListElement>, HTMLUListElement> {
}
