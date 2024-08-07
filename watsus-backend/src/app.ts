import express from 'express';

const app = express();

app.use(express.json());  // Middleware for parsing JSON bodies

// Define routes here
app.get('/', (req, res) => {
  res.send('Welcome to the Watsus API!');
});

// More route definitions can go here

export default app;  // Export the configured Express app
