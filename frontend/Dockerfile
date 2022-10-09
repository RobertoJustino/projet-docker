# pull official base image
FROM node:alpine

# set working directory
WORKDIR /frontend

# add `/app/node_modules/.bin` to $PATH
ENV PATH /frontend/node_modules/.bin:$PATH

# install app dependencies
COPY package.json ./
COPY package-lock.json ./
RUN npm install -d flag

# add app
COPY . ./

EXPOSE 8080

# start app
CMD ["npm", "run", "serve"]

