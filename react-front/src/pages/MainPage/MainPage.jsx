import styles from './App.module.scss';
import { withLayout } from '../../layout';
import React, { Fragment } from 'react';
import { Popover, Transition } from '@headlessui/react';

const MainPage = () => {
  return (
    <div className="p-10 border-2 border-purple-600">
      <h1>Main Page</h1>
      <button className={styles.parent}>Login</button>
      <Popover>
        <Popover.Button>Some button</Popover.Button>
        <Transition
                    as={Fragment}
                    enter="transition ease-out duration-200"
                    enterFrom="opacity-0 translate-y-1"
                    enterTo="opacity-100 translate-y-0"
                    leave="transition ease-in duration-150"
                    leaveFrom="opacity-100 translate-y-0"
                    leaveTo="opacity-0 translate-y-1"
                  >
        <Popover.Panel className='p-20 border absolute bg-purple-100 sm:px-0 lg:ml-0 lg:left-1/2 lg:-translate-x-1/2'>
          <div>Some panel</div>
        </Popover.Panel>
        </Transition>
      </Popover>
    </div>

  );
};

export default withLayout(MainPage);
