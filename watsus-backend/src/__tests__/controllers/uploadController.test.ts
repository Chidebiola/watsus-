import request from 'supertest';
import app from '../../app';
import path from 'path';

describe('UploadController', () => {
  describe('POST /api/upload', () => {
    it('should upload an image and return its embedding', async () => {
      const res = await request(app)
        .post('/api/upload')
        .attach('image', path.resolve(__dirname, '../test-image.jpg'));
      expect(res.status).toBe(200);
      expect(res.body).toHaveProperty('message', 'Image uploaded successfully');
      expect(res.body).toHaveProperty('filename');
      expect(res.body).toHaveProperty('embedding');
    });
  });
});
