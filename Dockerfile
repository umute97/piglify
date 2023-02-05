FROM node:lts-alpine AS build-stage

# Set up files
WORKDIR /app
COPY package.json .

# Install dependencies
RUN npm install

# Copy app
COPY . .

FROM nginx AS production-stage

COPY --from=build-stage /app/dist /usr/share/nginx/html

EXPOSE 80

CMD ["nginx", "-g", "daemon off;"]