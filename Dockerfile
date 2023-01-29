FROM node:19-alpine3.16

WORKDIR /webapp

ENV PATH /webapp/node_modules/.bin:$PATH

COPY package.json /webapp/package.json

RUN npm install

CMD ["npm", "run", "dev"]