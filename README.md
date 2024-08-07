# Watsus - Help Users Find What's Sustainable 🌿

## Project Overview 📈
Watsus aims to create a two-sided marketplace where users can rent or sell event-specific clothing (e.g., wedding dresses, pageant gowns) and buy or rent second-hand clothes. The platform helps users afford high-quality clothing for special occasions and reduce clothing waste by facilitating the resale and rental of underused items.

### Product Manager
- Jean Noubeyo Noubeyo

### Team Members
- William Sokol
- Chidinma
- Claire

### Technical Advisor
- Toby Morning
  - Follow On: [GitHub](http://github.com/urbantech/)
  - Connect On: [LinkedIn](http://linkedin.com/in/urbantech/)

---

## Vision 🌟
Create a sustainable and affordable marketplace for high-quality event-specific clothing. Reduce clothing waste and support small businesses by enabling users to rent, sell, or trade items they no longer need.

---

## Goals 🎯
- **Shop Creation**: Utilize user-generated images and form fields to create a searchable shop for ethnic clothing (e.g., African clothes).
- **Database Development**: Implement a database for clothing images with classification capabilities to extract fabric types, colors, and patterns.
- **Image Recognition**: Use convolutional methods to extract information and represent cuts as vectors, building segmentation models.
- **Exchange Platform**: Enable users to trade items to afford new ones.
- **Small Business Discovery**: Help users find small businesses that make similar items.
- **Ease of Disposal**: Enable users to get rid of excess unwanted items easily.

---

## User Stories 📝
- **Finding Affordable Items**: As a user, I want to find affordable items for events by paying a fee or trading items I no longer need.
- **Ethnic Clothing Search**: As a user, I want to easily search for ethnic clothing using user-generated images and form fields.
- **Image Classification**: As a user, I want to upload images of my clothing items and have them classified by fabric, color, and pattern.
- **Small Business Discovery**: As a user, I want to discover small businesses that offer similar items.
- **Item Disposal and Trade**: As a user, I want to get rid of my unwanted items and potentially trade them for items I need.

---

## Tools and Requirements 🛠️
### Database 📚
- Store images of clothing items.
- Classify items to extract fabric and cuts (e.g., light blue, color, and pattern).
- Use convolutional methods to illustrate cuts and represent them as vectors.
- Build segmentation models for precise classification.

### Storage 📦
- Develop an exchange platform for item trade.

### Image Recognition 📸
- Utilize the camera app to find items based on existing data.
- Limit searches to relevant items.
- Help users discover small businesses that make similar items.

### Search 🔍
- Scrap items from the reuse/resale market.
- Create a searchable database of 1 billion pieces of clothing.

---

## User Experience 🎨
### Figma Prototype 🎨
[Figma Design Link](#)

---

## Personas 👥
### Primary Users
- Individuals needing clothing for special events.
- People looking to sell or rent out their gently used clothing items.

### Secondary Users
- Small businesses offering unique clothing items.
- Users looking to trade items they no longer need.

---

## Technical To-Do List 🛠️
### Image Classification 📸
- Find similar items.
- Auto-categorize items.
- Create vector embeddings for clothing images.
- Label certain areas by category name.

### Photo Entries 📸
- Implement a photo upload system.
- Create a photo PSQL database.

### Public Website Development 🌐
- **Lead Developer**: William Sokol

### Prototype Development 📊
- **Chidinma**:
  - Create a dashboard prototype.
  - Show the flow of how pictures will be saved with descriptions and prices.
  - Demonstrate how items will be searched for.
  - Develop an MVP pitch deck.

### Dataset and Embeddings 📂
- **Claire**:
  - Find a dataset with images.
  - Create image embeddings.
  - Develop a search function for images from the embeddings.

---

## Storage 📦
TBD: Define storage solutions for the platform.

---

## Bonus Features 🎁
- Explore integration of vector edges for enhanced image recognition.

---

## Goal for Today 🎯
Begin the creation of the shop with user-generated images and searchable form fields for ethnic clothing (e.g., African clothes).

---

## Installation / Setup Instructions 🛠️

### Prerequisites
- Node.js
- PostgreSQL

### Steps

1. **Clone the repository**:
   ```sh
   git clone https://github.com/yourusername/watsus.git
   cd watsus
