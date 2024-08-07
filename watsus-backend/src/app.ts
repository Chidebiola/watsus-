// src/app.ts
const express = require('express');
const app = express();

app.use(express.json());

app.get('/users', (req, res) => {
  res.status(200).json([]);
});

app.post('/users', (req, res) => {
  const { username, email, password } = req.body;
  res.status(201).json({ username, email });
});

module.exports = app;
