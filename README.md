# NexGen Developers Website

A modern, responsive website for NexGen Developers built with Flask and deployed on Vercel.

## 🌟 Features

- **Responsive Design**: Fully responsive layout that works on all devices
- **Modern UI**: Clean and professional design with smooth animations
- **Contact Form**: Interactive contact form with email notifications
- **Service Showcase**: Detailed presentation of development services
- **Project Portfolio**: Showcase of completed projects with case studies
- **SEO Optimized**: Built-in SEO features and schema markup
- **Backend Integration**: Flask-powered backend with SMTP email support
- **Vercel Deployment**: Serverless deployment with automatic CI/CD

## 🛠️ Technologies Used

- **Frontend**:
  - HTML5
  - CSS3
  - JavaScript
  - Bootstrap 5
  - Font Awesome Icons
  - Google Fonts
  - Schema.org markup

- **Backend**:
  - Python 3.x
  - Flask
  - Flask-Mail
  - SMTP (Gmail)

## 📋 Prerequisites

- Python 3.x
- Modern web browser
- Gmail account for SMTP
- Vercel account for deployment

## 🚀 Getting Started

### Local Development

1. Clone the repository:
   ```bash
   git clone https://github.com/your-username/nexgendevelopers.git
   cd nexgendevelopers
   ```

2. Create and activate virtual environment:
   ```bash
   python -m venv venv
   source venv/bin/activate  # On Windows: venv\Scripts\activate
   ```

3. Install dependencies:
   ```bash
   pip install -r requirements.txt
   ```

4. Create `.env` file:
   ```
   MAIL_USERNAME=your-sender-email@gmail.com
   MAIL_PASSWORD=your-app-password
   RECEIVER_EMAIL=your-receiver-email@gmail.com
   SECRET_KEY=your-secret-key
   ```

5. Run the application:
   ```bash
   python app.py
   ```

### Deployment

1. Push your code to GitHub:
   ```bash
   git add .
   git commit -m "Initial commit"
   git push origin main
   ```

2. Deploy on Vercel:
   - Connect your GitHub repository
   - Add environment variables
   - Deploy

## 📁 Project Structure

```
nexgendevelopers/
├── app.py              # Flask application
├── requirements.txt    # Python dependencies
├── vercel.json        # Vercel configuration
├── .env               # Environment variables (not in git)
├── .gitignore         # Git ignore file
├── templates/         # HTML templates
│   └── index.html
└── static/           # Static files
    ├── css/
    ├── js/
    ├── img/
    └── Favicon/
```

## ⚙️ Configuration

### Email Setup

1. Enable 2-Step Verification in your Gmail account
2. Generate an App Password
3. Update `.env` file with your credentials

### Vercel Deployment

1. Add environment variables in Vercel dashboard:
   - MAIL_USERNAME
   - MAIL_PASSWORD
   - RECEIVER_EMAIL
   - SECRET_KEY


## 📝 License

This project is licensed under the MIT License - see the [LICENSE](LICENSE) file for details.

## 📞 Contact

- Email: nexgendevelopers11@gmail.com
- Phone: 6006161726
- Location: Srinagar, J&K

## 🙏 Acknowledgments

- Flask and Flask-Mail for backend functionality
- Bootstrap for responsive design
- Font Awesome for icons
- Google Fonts for typography
- Vercel for hosting and deployment

---

© 2025 NexGen Developers. All Rights Reserved. 
