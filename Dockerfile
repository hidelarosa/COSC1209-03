# Use a specific version of Node.js for better stability
FROM node:14.18.1

# Set the working directory in the container
WORKDIR /app

# Copy package.json and package-lock.json first to take advantage of Docker cache
COPY package*.json /app/

# Install production dependencies only
RUN npm install --production

# Copy the rest of your application files into the container
COPY . /app

# Expose the port your app will run on
EXPOSE 3000

# Define the command to run your app
CMD ["npm", "start"]
