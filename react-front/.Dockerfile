FROM node:16-alpine
WORKDIR ./react-front
COPY ./frontend/package.json ./
COPY ./frontend/package-lock.json ./
RUN npm ci
COPY . .
RUN npm build
