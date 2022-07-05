import React, { Fragment } from 'react';
import { Menu, Transition } from '@headlessui/react';
import styles from './TopMenu.module.scss';
import { UserIcon } from '@heroicons/react/solid';
import { Link } from 'react-router-dom';

export const ProfileMenu = () => {
  return (
    <Menu className="relative" as="div">
      <Menu.Button className={styles.menu_button}>
        <div className="flex">
          <UserIcon className="relative h-6 pr-1"/>
          <span className="">Profile</span>
        </div>
      </Menu.Button>
      <Transition
        as={Fragment}
        enter="transition ease-out duration-200"
        enterFrom="opacity-0 translate-y-1"
        enterTo="opacity-100 translate-y-0"
        leave="transition ease-in duration-150"
        leaveFrom="opacity-100 translate-y-0"
        leaveTo="opacity-0 translate-y-1"
      >
        <Menu.Items className="absolute" as="ul">
          <div className="bg-white border-2 border-indigo-200 px-3 -mr-5">
            <Menu.Item as="li" className={styles.menu_item}>
              <Link to="/profile/" className={styles.link}>My words</Link>
            </Menu.Item>
            <Menu.Item as="li" className={styles.menu_item}>
              <Link to="/profile/" className={styles.link}>Settings</Link>
            </Menu.Item>
            <Menu.Item as="li" className={styles.menu_item}>
              <Link to="/profile/" className={styles.link}>Log out</Link>
            </Menu.Item>
          </div>
        </Menu.Items>
      </Transition>
    </Menu>
  );
};
