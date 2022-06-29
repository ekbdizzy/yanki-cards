export interface Credentials {
    email: string;
    password: string;
}

export interface TokenResponse {
    access: string,
    refresh: string
}


export interface UserData {
    first_name: string
    last_name: string
    email: string
}
