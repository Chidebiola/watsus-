// src/__tests__/controllers/userController.test.ts

const request = require('supertest');
const app = require('../../app');

describe('UserController', () => {
  describe('GET /users', () => {
    it('should return all users', async () => {
      const res = await request(app).get('/users');
      expect(res.status).toBe(200);
      expect(res.body).toBeInstanceOf(Array);
    });
  });

  describe('POST /users', () => {
    it('should create a new user', async () => {
      const newUser = { username: 'newuser', email: 'newuser@example.com', password: 'password123' };
      const res = await request(app).post('/users').send(newUser);
      expect(res.status).toBe(201);
      expect(res.body.username).toEqual(newUser.username);
    });
  });
});
