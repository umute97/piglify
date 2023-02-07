FROM node:lts-alpine AS build-stage

COPY package.json .
RUN npm install

COPY . .

RUN npm run build-only

FROM nginx:1.23-alpine AS deploy-stage

RUN rm -rf /usr/share/nginx/html/*

COPY --from=build-stage /dist /usr/share/nginx/html

EXPOSE 80
ENTRYPOINT ["nginx", "-g", "daemon off;"]