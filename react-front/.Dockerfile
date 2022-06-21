FROM node:14-alpine
WORKDIR ./react-front
COPY . .
RUN npm install
RUN npm run build

