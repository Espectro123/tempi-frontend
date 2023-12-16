# Use the official Node image
FROM node:20-alpine

# Set working directory
WORKDIR /app


# Install Vue CLI
RUN npm install -g @vue/cli

# Copy package.json and install dependencies
COPY package.json /app
RUN npm install

# Copy rest of the application code
COPY . /app

# Build the app
RUN npm run build

# Start the app
CMD ["npm", "run", "serve"]
