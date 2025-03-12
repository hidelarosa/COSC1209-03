// Import the 'http' module to create a web server
const http = require('http');

// Set the hostname and port for the server
const hostname = '127.0.0.1';
const port = 3000;

// Create the server and respond with 'Hello, World!' on request
const server = http.createServer((req, res) => {
  res.statusCode = 200; // HTTP status code 200 means OK
  res.setHeader('Content-Type', 'text/plain'); // Set the response content type
  res.end('Hello, World!!\n'); // Send the response body
});

// Start the server on the specified hostname and port
server.listen(port, hostname, () => {
  console.log(`Server running at http://${hostname}:${port}/`);
});
