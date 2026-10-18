FROM node:20-alpine

WORKDIR /app

COPY package.json ./
RUN npm install

COPY . .

# Development server (hot reload). Listen on all interfaces so the host can reach it.
ENV HOST=0.0.0.0
EXPOSE 3000
CMD ["npm", "start"]
