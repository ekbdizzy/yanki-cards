import React from 'react';
import logo from './logo.svg';
import './App.css';
import {Menu} from './components';
import {Layout, withLayout} from "./layout";

function App() {
    return (
            <div className="App">
                <Menu>Hello!1</Menu>
            </div>
    );
}

export default withLayout(App);
