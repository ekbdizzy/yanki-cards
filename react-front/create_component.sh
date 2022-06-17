#!/bin/bash

mkdir "./components/$1";
touch ./components/$1/{$1.module.css,$1.props.ts,$1.tsx}
echo "$1.module.css, $1.props.css, $1.tsx done"
