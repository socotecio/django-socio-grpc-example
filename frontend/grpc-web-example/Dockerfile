FROM node:lts-alpine

WORKDIR /opt/code

COPY package.json package-lock.json ./
RUN npm install 

EXPOSE 5173
ENTRYPOINT ["npm", "run"]