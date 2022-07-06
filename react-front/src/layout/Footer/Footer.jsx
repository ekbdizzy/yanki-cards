import React from 'react';
import { Link } from 'react-router-dom';
import Logo from '../../assets/logo.svg';

export const Footer = () => {
  return (
    <div className="bg-indigo-800 w-screen min-h-[100px]">
      <footer className="max-w-7xl m-auto bg-indigo-800 text-white">
                <div className="flex items-center my-5 justify-between">
          <Link to="/">
            <img className="h-10 w-auto sm:h-10"
                 alt="Yanki Cards"
                 src={Logo}
            />
          </Link>
          <div>
            <p className="text-white font-medium">Yanki Cards {new Date().getFullYear()}</p>
            <a className="hover:text-yellow-300 transition" href="https://github.com/ekbdizzy/yanki-cards"
               target="_blank" rel="noreferrer">Source code on Github</a>
          </div>
        </div>
      </footer>
    </div>
  );
};
