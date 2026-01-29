# David Visuals


![HTML5](https://img.shields.io/badge/HTML5-Valid-orange)
![CSS3](https://img.shields.io/badge/CSS3-Valid-blue)
![JavaScript](https://img.shields.io/badge/JavaScript-ES6-yellow)
![GitHub](https://img.shields.io/badge/Django-6.0.1-green)
![Python](https://img.shields.io/badge/Python-3.13-blue)
![PostgreSQL](https://img.shields.io/badge/PostgreSQL-Database-blue)
![Stripe](https://img.shields.io/badge/Stripe-Payment-purple)

Professional graphic design services platform with fixed pricing and secure Stripe payment integration.

![Mobilephone View](static/images/PAGES/Website_presentation.png)

**Live Site:** [https://david-visuals-9e85de42044d.herokuapp.com](https://david-visuals-9e85de42044d.herokuapp.com)

---

## 📋 Table of Contents

- [Features](#features)
- [User Experience (UX) & Design Rationale](#user-experience-ux--design-rationale)
- [E-commerce Business Model](#e-commerce-business-model)
- [Database Schema](#database-schema)
- [Agile Methodology](#agile-methodology)
- [Wireframes](#wireframes)
- [Project Structure](#project-structure)
- [Technologies Used](#technologies-used)
- [Installation](#installation)
- [Deployment](#deployment)
- [Testing](#testing)
- [Credits](#credits)

---

## ✨ Features

- **Package Browsing**: Browse design packages with category filtering (Logo, Social Media, Flyer/Poster)
- **User Authentication**: Sign up, login, and manage user profiles using Django Allauth
- **Secure Payments**: Stripe Checkout integration for secure payment processing
- **Order Management**: View order history and track purchases with detailed order information
- **Newsletter**: Subscribe to updates and newsletters with email validation
- **Admin Panel**: Full CRUD functionality for managing packages, orders, and subscribers
- **SEO Optimized**: Meta tags, sitemap.xml, and robots.txt for search engine visibility
- **Responsive Design**: Mobile-first design that works on all devices
- **Custom 404 Page**: User-friendly error page with navigation options

---

## 🎨 User Experience (UX) & Design Rationale

The user experience of David Visuals was designed to prioritise clarity, trust, and ease of purchase for users seeking professional graphic design services.

The interface follows a clean, minimal layout to ensure that users can quickly understand available services, pricing, and delivery expectations without unnecessary distraction. Fixed pricing is clearly displayed across package pages to support transparent decision-making.

Navigation is consistent throughout the site, allowing users to move seamlessly between browsing packages, managing their profile, and completing purchases. Responsive design principles were applied to ensure usability across desktop, tablet, and mobile devices.

Accessibility considerations include clear visual hierarchy, readable typography, sufficient colour contrast, and intuitive form layouts to support a wide range of users.

### Colour Scheme

The colour scheme was carefully chosen to reflect a professional design services brand while maintaining excellent readability:

| Colour | Hex Code | Usage |
|--------|----------|-------|
| Dark Navy | `#2c3e50` | Header, footer, headings |
| Primary Blue | `#3498db` | Buttons, links, accents |
| Purple Gradient | `#667eea` to `#764ba2` | Hero section, profile cards |
| Light Grey | `#f4f4f4` | Background |
| White | `#ffffff` | Cards, content blocks |
| Dark Text | `#333` | Body text |
| Success Green | `#27ae60` | Success messages |
| Error Red | `#e74c3c` | Error messages |

### Typography

The website uses clean, modern system fonts for optimal readability and performance:

- **Primary Font**: `"Segoe UI", Tahoma, Geneva, Verdana, sans-serif`
- **Font Awesome** icons for visual elements (navigation, features, status indicators)

---

## 💼 E-commerce Business Model

David Visuals operates using a **B2C (Business-to-Consumer) fixed-price e-commerce model**.

Customers can browse pre-defined graphic design service packages with transparent, fixed pricing and complete purchases securely using Stripe Checkout. Revenue is generated through one-time payments for design services.

Marketing strategies include:
- A dedicated Facebook Business Page to reach potential customers
- A newsletter subscription feature to retain users and promote updates

This model prioritises clarity, trust, and ease of purchase for users seeking professional graphic design services.

---

### Site Pages

#### Home Page

The landing page showcases the brand with a hero section and clear call-to-action buttons.

![Home Page](static/images/PAGES/Home.png)

#### Package List

Browse all available design packages with category filtering options.

![Package List](static/images/PAGES/Package_list.png)

#### Package Details

Detailed view of each package showing price, delivery time, revisions, and what's included.

![Package Details](static/images/PAGES/Package_details.png)

#### Checkout

Secure checkout page with order summary and Stripe payment integration.

![Checkout](static/images/PAGES/Checkout_page.png)

#### Payment Success

Order confirmation page displayed after successful payment.

![Payment Success](static/images/PAGES/Payment_successful_page.png)

#### Payment Cancelled

Friendly cancellation page when users cancel their payment.

![Payment Cancelled](static/images/PAGES/Payment_cancelled.png)

#### Profile

User profile page showing account information and editable details.

![Profile](static/images/PAGES/Profile_page.png)

#### Login

Secure login page with Remember Me functionality.

![Login](static/images/PAGES/Login_page.png)

#### Sign Up

Registration page for new users.

![Sign Up](static/images/PAGES/Signup_page.png)

#### Unsubscribe

Page for users to unsubscribe from Newsletters.

![Unsubscribe](static/images/PAGES/Unsubscribe_page.png)

#### Admin Panel

Django admin interface for managing packages, orders, and users.

![Admin](static/images/PAGES/Admin_page.png)

#### 404 Page

Custom error page with navigation options.

![404 Page](static/images/PAGES/404page.png)

#### Facebook Business Page

Social media presence for the business.

![Facebook](static/images/PAGES/Facebook_page.png)

---

## 🗄️ Database Schema

The application uses PostgreSQL with the following entity relationship diagram:

![Database ERD](static/images/erd.png)

### Key Models:

- **User**: Django's built-in authentication user model
- **UserProfile**: Extended user information with phone and address details
- **Package**: Design packages with category, price, features, and images
- **Order**: Purchase records linking users to packages with Stripe payment details
- **Subscriber**: Newsletter email subscriptions

---

## 🎯 Agile Methodology

This project was developed using Agile methodology with GitHub Projects for task management:

![GitHub Project Board](static/images/PAGES/agile.png)

### User Stories Completed:

✅ **Epic 1: User Authentication**
- #4: Register an account
- #5: Log in to account
- #6: Log out of account

✅ **Epic 2: Package Management**
- #1: View all design packages
- #2: View package details
- #3: Browse packages by category

✅ **Epic 3: Order & Payment**
- #7: Purchase a package
- #8: View order confirmation
- #9: View order history

✅ **Epic 4: User Profile**
- #10: View profile
- #11: Update profile

✅ **Epic 5: Newsletter**
- #12: Subscribe to newsletter

✅ **Epic 6: Admin CRUD**
- #13-17: Admin package management

[View Project Board](https://github.com/users/thekidmellow/projects/6/views/1)

---

## 📐 Wireframes

Wireframes were created for both desktop and mobile views to plan the layout and user experience.

### Desktop Wireframes

| Page | Wireframe |
|------|-----------|
| Home | ![Desktop Home](static/images/Wireframe/Wireframes_desktop_Home.png) |
| Package List | ![Desktop Package List](static/images/Wireframe/Wireframes_desktop_Package_list.png) |
| Package Detail | ![Desktop Package Detail](static/images/Wireframe/Wireframes_desktop_Package_detail.png) |
| Checkout | ![Desktop Checkout](static/images/Wireframe/Wireframes_desktop_Checkout.png) |
| Profile | ![Desktop Profile](static/images/Wireframe/Wireframes_desktop_Profile.png) |
| Login | ![Desktop Login](static/images/Wireframe/Wireframes_desktop_Login.png) |
| Sign Up | ![Desktop Signup](static/images/Wireframe/Wireframes_desktop_Signup.png) |
| Unsubscribe | ![Desktop Unsubscribe](static/images/Wireframe/Wireframes_desktop_Unsubscribe.png) |

### Mobile Wireframes

| Page | Wireframe |
|------|-----------|
| Home | ![Mobile Home](static/images/Wireframe/Wireframes_Mobile_Home.png) |
| Package List | ![Mobile Package List](static/images/Wireframe/Wireframes_Mobile_Package_List.png) |
| Package Detail | ![Mobile Package Detail](static/images/Wireframe/Wireframes_Mobile_Package_Detail.png) |
| Checkout | ![Mobile Checkout](static/images/Wireframe/Wireframes_Mobile_Checkout.png) |
| Profile | ![Mobile Profile](static/images/Wireframe/Wireframes_Mobile_Profile.png) |
| Login | ![Mobile Login](static/images/Wireframe/Wireframes_Mobile_Login.png) |
| Sign Up | ![Mobile Signup](static/images/Wireframe/Wireframes_Mobile_Signup.png) |
| Unsubscribe | ![Mobile Unsubscribe](static/images/Wireframe/Wireframes_Mobile_Unsubscribe.png) |

---

## 📁 Project Structure

```
david-visuals/
│
├── david_visuals_project/      # Main project directory
│   ├── __init__.py
│   ├── asgi.py                 # ASGI configuration
│   ├── settings.py             # Django settings
│   ├── urls.py                 # Main URL configuration
│   └── wsgi.py                 # WSGI configuration
│
├── home/                       # Home app
│   ├── migrations/
│   ├── __init__.py
│   ├── admin.py
│   ├── apps.py
│   ├── models.py
│   ├── tests.py
│   ├── urls.py
│   └── views.py                # Homepage view
│
├── packages/                   # Packages app
│   ├── migrations/
│   ├── __init__.py
│   ├── admin.py                # Package admin configuration
│   ├── apps.py
│   ├── models.py               # Package model
│   ├── tests.py
│   ├── urls.py
│   └── views.py                # Package views
│
├── orders/                     # Orders app
│   ├── migrations/
│   ├── __init__.py
│   ├── admin.py                # Order admin configuration
│   ├── apps.py
│   ├── models.py               # Order model
│   ├── tests.py
│   ├── urls.py
│   └── views.py                # Checkout views
│
├── profiles/                   # User profiles app
│   ├── migrations/
│   ├── __init__.py
│   ├── admin.py                # Profile admin configuration
│   ├── apps.py
│   ├── forms.py                # Profile update form
│   ├── models.py               # UserProfile model
│   ├── signals.py              # Auto-create profile signal
│   ├── tests.py
│   ├── urls.py
│   └── views.py                # Profile views
│
├── newsletter/                 # Newsletter app
│   ├── migrations/
│   ├── templates/
│   │   └── newsletter/
│   │       └── unsubscribe.html
│   ├── __init__.py
│   ├── admin.py                # Subscriber admin configuration
│   ├── apps.py
│   ├── forms.py                # Subscriber form
│   ├── models.py               # Subscriber model
│   ├── tests.py
│   ├── urls.py
│   └── views.py                # Subscribe/unsubscribe views
│
├── templates/                  # Global templates
│   ├── account/                # Authentication templates
│   │   ├── login.html
│   │   ├── logout.html
│   │   └── signup.html
│   ├── home/
│   │   └── index.html          # Homepage
│   ├── includes/
│   │   ├── footer.html         # Footer partial
│   │   └── navbar.html         # Navigation partial
│   ├── orders/
│   │   ├── cancel.html         # Payment cancelled
│   │   ├── checkout.html       # Checkout page
│   │   └── success.html        # Payment success
│   ├── packages/
│   │   ├── package_detail.html # Package detail page
│   │   └── package_list.html   # Package list page
│   ├── profiles/
│   │   ├── order_history.html  # Order history
│   │   └── profile.html        # User profile page
│   ├── 404.html                # Custom 404 page
│   └── base.html               # Base template
│
├── static/                     # Static files
│   ├── css/
│   │   └── style.css           # Main stylesheet
│   ├── js/
│   │   └── script.js           # JavaScript functionality
│   └── images/                 # All images
│       ├── erd.png             # Database ERD diagram
│       ├── favicon-32x32.png   # Favicon
│       ├── Chrome/             # Chrome browser screenshots
│       ├── Firefox/            # Firefox browser screenshots
│       ├── Safari/             # Safari browser screenshots
│       ├── LIGHTHOUSE_AUDIT/   # Lighthouse audit screenshots
│       ├── PAGES/              # Site page screenshots
│       ├── Responsiveness/     # Mobile & tablet screenshots
│       ├── VALIDATIONS/        # Code validation screenshots
│       └── Wireframe/          # Wireframe images
│
├── .env                        # Environment variables (not in repo)
├── db.sqlite3                  # SQLite database (local dev)
├── erd.png                     # Database ERD diagram
├── manage.py                   # Django management script
├── Procfile                    # Heroku process file
├── README.md                   # Project documentation
├── DEPLOYMENT.md               # Deployment guide
├── TESTING.md                  # Testing documentation
├── requirements.txt            # Python dependencies
├── robots.txt                  # SEO robots.txt
└── sitemaps.py                 # SEO sitemap configuration
```

---

## 🛠️ Technologies Used

### Backend
- **Django 6.0.1** - Python web framework
- **Python 3.13** - Programming language
- **PostgreSQL** - Relational database
- **Django Allauth** - Authentication system
- **Stripe API** - Payment processing
- **Gunicorn** - WSGI HTTP server

### Frontend
- **HTML5** - Structure
- **CSS3** - Styling
- **JavaScript** - Interactivity
- **Bootstrap 5** - CSS framework (via CDN)

### Deployment & Storage
- **Heroku** - Cloud platform hosting
- **Cloudinary** - Image storage and management
- **WhiteNoise** - Static file serving
- **Git** - Version control
- **GitHub** - Code repository & project management

### Development Tools
- **VS Code** - Code editor
- **Python Decouple** - Environment variable management
- **dj-database-url** - Database configuration
- **Stripe CLI** - Webhook testing

---

## 🚀 Installation

### Prerequisites
- Python 3.13
- PostgreSQL
- Stripe Account
- Git

### Local Setup

1. **Clone the repository:**
```bash
git clone https://github.com/thekidmellow/david-visuals.git
cd david-visuals
```

2. **Create virtual environment:**
```bash
python3 -m venv venv
source venv/bin/activate  # On Windows: venv\Scripts\activate
```

3. **Install dependencies:**
```bash
pip install -r requirements.txt
```

4. **Create `.env` file with environment variables:**
```env
SECRET_KEY=your-secret-key-here
DEBUG=True
DATABASE_URL=postgresql://user:password@localhost/dbname
ALLOWED_HOSTS=127.0.0.1,localhost
STRIPE_PUBLIC_KEY=pk_test_your_key_here
STRIPE_SECRET_KEY=sk_test_your_key_here
CLOUDINARY_CLOUD_NAME=your_cloud_name
CLOUDINARY_API_KEY=your_api_key
CLOUDINARY_API_SECRET=your_api_secret
```

5. **Run migrations:**
```bash
python manage.py migrate
```

6. **Create superuser:**
```bash
python manage.py createsuperuser
```

7. **Load sample data (optional):**
```bash
python manage.py loaddata packages
```

8. **Run development server:**
```bash
python manage.py runserver
```

9. **Access the application:**
- Homepage: http://127.0.0.1:8000/
- Admin Panel: http://127.0.0.1:8000/admin/

---

## 📦 Deployment

The application is deployed on Heroku. For detailed deployment instructions, see [DEPLOYMENT.md](DEPLOYMENT.md).

### Quick Deploy Steps:

1. Create Heroku app
2. Add PostgreSQL database
3. Set environment variables
4. Deploy via Git
5. Run migrations
6. Create superuser

**Live Site:** [https://david-visuals-9e85de42044d.herokuapp.com](https://david-visuals-9e85de42044d.herokuapp.com)

---

## 🧪 Testing

Comprehensive testing documentation is available in [TESTING.md](TESTING.md).

### Testing Coverage:
- ✅ HTML, CSS, JavaScript, Python Validation
- ✅ Lighthouse Performance Audits
- ✅ Browser Compatibility Testing (Chrome, Firefox, Safari)
- ✅ Responsiveness Testing (Mobile & Tablet)
- ✅ User Authentication
- ✅ Package Browsing & Filtering
- ✅ Checkout & Payment Flow
- ✅ Profile Management
- ✅ Newsletter Subscription
- ✅ Admin CRUD Operations

### Test Stripe Card:
- **Card Number:** 4242 4242 4242 4242
- **Expiry:** Any future date
- **CVC:** Any 3 digits
- **ZIP:** Any 5 digits

---

### Admin Access

For assessment purposes, use the following superuser credentials to access the Django admin panel:

| Field | Value |
|-------|-------|
| **URL** | [https://david-visuals-9e85de42044d.herokuapp.com/admin/](https://david-visuals-9e85de42044d.herokuapp.com/admin/) |
| **Username** | `herokutest1` |
| **Email** | `heroku@test.com` |
| **Password** | `testpassh1` |

---

## 📄 License

This project is for educational purposes as part of Code Institute's Full Stack Software Development program.

---

## 👤 Author

**David Ujo**

- GitHub: [@thekidmellow](https://github.com/thekidmellow)
- Facebook: [David Visuals Business Page](https://www.facebook.com/profile.php?id=61586669439949)
- Email: thekidmellow@gmail.com

---

## 🙏 Credits

### Code & Resources
- Django Documentation
- Stripe Documentation
- Bootstrap Documentation
- Code Institute Learning Materials
- Stack Overflow Community

### Media
- Wireframe images: Custom designs created by David Ujo using Adobe Photoshop
- Package images: Custom designs created by David Ujo using Adobe Photoshop
- Icons: Font Awesome (via CDN)

### Acknowledgments
- Code Institute tutors and mentors
- Fellow students in the Slack community
- Family and friends for testing and feedback

---

**© 2026 David Visuals. All rights reserved.**
