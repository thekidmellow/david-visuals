# Deployment

This document provides step-by-step instructions for deploying the David Visuals application to Heroku, as well as instructions for local development.

## Table of Contents

- [Prerequisites](#prerequisites)
- [Heroku Deployment](#heroku-deployment)
  - [Creating the Heroku App](#creating-the-heroku-app)
  - [Setting Up the Database](#setting-up-the-database)
  - [Configuring Environment Variables](#configuring-environment-variables)
  - [Connecting to GitHub](#connecting-to-github)
  - [Deploying the Application](#deploying-the-application)
- [Cloudinary Setup](#cloudinary-setup)
- [Stripe Setup](#stripe-setup)
  - [Getting API Keys](#getting-api-keys)
  - [Test Card Details](#test-card-details)
- [Local Development](#local-development)
  - [Forking the Repository](#forking-the-repository)
  - [Cloning the Repository](#cloning-the-repository)
  - [Setting Up Local Environment](#setting-up-local-environment)

---

## Prerequisites

Before deploying, ensure you have accounts with the following services:

- [Heroku](https://www.heroku.com/) - Cloud platform for hosting
- [Cloudinary](https://cloudinary.com/) - Image storage and management
- [Stripe](https://stripe.com/) - Payment processing
- [GitHub](https://github.com/) - Code repository

---

## Heroku Deployment

### Creating the Heroku App

1. Log in to your [Heroku Dashboard](https://dashboard.heroku.com/)

2. Click **New** in the top right corner and select **Create new app**

3. Enter a unique **App name** (e.g., `david-visuals`)

4. Select your **Region** (Europe or United States)

5. Click **Create app**

### Setting Up the Database

This project uses a **Code Institute PostgreSQL Database**.

To obtain my own Postgres Database from Code Institute, I followed these steps:

1. Signed-in to the CI LMS using my email address

2. Navigated to the **Databases** section

3. Requested a new PostgreSQL database

4. Received an email with my database credentials and connection URL

5. The database URL was in the format:
   ```
   postgresql://username:password@host:port/database_name
   ```

6. Added the `DATABASE_URL` to my Heroku Config Vars

> **⚠️ Caution**
>
> - PostgreSQL databases by Code Institute are only available to CI Students.
> - You must acquire your own PostgreSQL database through some other method if you plan to clone/fork this repository.
> - Code Institute students are allowed a maximum of 8 databases.
> - Databases are subject to deletion after 18 months.

### Configuring Environment Variables

1. In your Heroku app dashboard, click on the **Settings** tab

2. Click **Reveal Config Vars**

3. Add the following environment variables:

| Key | Value |
|-----|-------|
| `SECRET_KEY` | Your Django secret key (generate a random string) |
| `DEBUG` | `False` |
| `ALLOWED_HOSTS` | `your-app-name.herokuapp.com` |
| `DATABASE_URL` | Your Code Institute PostgreSQL URL |
| `CLOUDINARY_CLOUD_NAME` | Your Cloudinary cloud name |
| `CLOUDINARY_API_KEY` | Your Cloudinary API key |
| `CLOUDINARY_API_SECRET` | Your Cloudinary API secret |
| `STRIPE_PUBLIC_KEY` | Your Stripe publishable key |
| `STRIPE_SECRET_KEY` | Your Stripe secret key |

**Generating a Secret Key:**

You can generate a secure secret key using Python:

```python
python -c "from django.core.management.utils import get_random_secret_key; print(get_random_secret_key())"
```

Or use an online generator like [Djecrety](https://djecrety.ir/)

### Connecting to GitHub

1. In your Heroku app dashboard, click on the **Deploy** tab

2. In the **Deployment method** section, click **GitHub**

3. Click **Connect to GitHub** and authorize Heroku if prompted

4. Search for your repository name (e.g., `david-visuals`)

5. Click **Connect** next to the correct repository

### Deploying the Application

**Option 1: Automatic Deploys**

1. In the **Automatic deploys** section, select the branch to deploy (usually `main`)

2. Click **Enable Automatic Deploys**

3. Every push to the selected branch will trigger a new deployment

**Option 2: Manual Deploy**

1. In the **Manual deploy** section, select the branch to deploy

2. Click **Deploy Branch**

3. Wait for the build to complete

**Post-Deployment Steps:**

1. Once deployed, click **More** in the top right and select **Run console**

2. Run the following commands:

```bash
python manage.py migrate
```

```bash
python manage.py createsuperuser
```

3. Follow the prompts to create your admin account

4. Click **Open app** to view your live site

---

## Cloudinary Setup

Cloudinary is used for storing and serving images in production.

1. Sign up or log in to [Cloudinary](https://cloudinary.com/)

2. From your **Dashboard**, locate the following credentials:
   - Cloud Name
   - API Key
   - API Secret

3. Add these values to your Heroku Config Vars:
   - `CLOUDINARY_CLOUD_NAME`
   - `CLOUDINARY_API_KEY`
   - `CLOUDINARY_API_SECRET`

4. In your Django `settings.py`, ensure you have:

```python
CLOUDINARY_STORAGE = {
    'CLOUD_NAME': os.environ.get('CLOUDINARY_CLOUD_NAME'),
    'API_KEY': os.environ.get('CLOUDINARY_API_KEY'),
    'API_SECRET': os.environ.get('CLOUDINARY_API_SECRET'),
}

DEFAULT_FILE_STORAGE = 'cloudinary_storage.storage.MediaCloudinaryStorage'
```

---

## Stripe Setup

### Getting API Keys

1. Sign up or log in to [Stripe](https://stripe.com/)

2. Navigate to **Developers** > **API keys**

3. Copy your **Publishable key** (starts with `pk_`)

4. Copy your **Secret key** (starts with `sk_`)

5. Add these to your Heroku Config Vars:
   - `STRIPE_PUBLIC_KEY` = Publishable key
   - `STRIPE_SECRET_KEY` = Secret key

**Note:** For testing, use the test mode keys. Switch to live keys when ready for production.

### Test Card Details

Use the following test card for Stripe payments in test/sandbox mode:

| Field | Value |
|-------|-------|
| Card Number | `4242 4242 4242 4242` |
| Expiry Date | Any future date (e.g., `12/34`) |
| CVC | Any 3 digits (e.g., `123`) |
| ZIP | Any 5 digits (e.g., `12345`) |

---

## Local Development

### Forking the Repository

Forking creates a copy of the repository in your own GitHub account.

1. Log in to [GitHub](https://github.com/)

2. Navigate to the repository: [https://github.com/thekidmellow/david-visuals](https://github.com/thekidmellow/david-visuals)

3. Click the **Fork** button in the top right corner

4. Select your GitHub account as the destination

5. The forked repository will now appear in your account

### Cloning the Repository

Cloning downloads a copy of the repository to your local machine.

1. Navigate to the repository on GitHub

2. Click the **Code** button

3. Copy the HTTPS URL:
   ```
   https://github.com/thekidmellow/david-visuals.git
   ```

4. Open your terminal and navigate to your desired directory

5. Run the clone command:
   ```bash
   git clone https://github.com/thekidmellow/david-visuals.git
   ```

6. Navigate into the project directory:
   ```bash
   cd david-visuals
   ```

### Setting Up Local Environment

1. **Create a virtual environment:**

   ```bash
   python -m venv venv
   ```

2. **Activate the virtual environment:**

   On macOS/Linux:
   ```bash
   source venv/bin/activate
   ```

   On Windows:
   ```bash
   venv\Scripts\activate
   ```

3. **Install dependencies:**

   ```bash
   pip install -r requirements.txt
   ```

4. **Create a `.env` file in the project root:**

   ```env
   SECRET_KEY=your-local-secret-key
   DEBUG=True
   DATABASE_URL=sqlite:///db.sqlite3
   ALLOWED_HOSTS=127.0.0.1,localhost

   CLOUDINARY_CLOUD_NAME=your_cloud_name
   CLOUDINARY_API_KEY=your_api_key
   CLOUDINARY_API_SECRET=your_api_secret

   STRIPE_PUBLIC_KEY=pk_test_your_key
   STRIPE_SECRET_KEY=sk_test_your_key
   ```

   **Note:** For local development, you can use SQLite instead of PostgreSQL by setting:
   ```
   DATABASE_URL=sqlite:///db.sqlite3
   ```

5. **Run database migrations:**

   ```bash
   python manage.py migrate
   ```

6. **Create a superuser:**

   ```bash
   python manage.py createsuperuser
   ```

7. **Load sample data (optional):**

   ```bash
   python manage.py loaddata packages
   ```

8. **Collect static files:**

   ```bash
   python manage.py collectstatic
   ```

9. **Run the development server:**

   ```bash
   python manage.py runserver
   ```

10. **Access the application:**

    - Homepage: [http://127.0.0.1:8000/](http://127.0.0.1:8000/)
    - Admin Panel: [http://127.0.0.1:8000/admin/](http://127.0.0.1:8000/admin/)

---

## Troubleshooting

### Common Issues

**Static files not loading:**
- Ensure `DEBUG=False` in production
- Run `python manage.py collectstatic`
- Verify WhiteNoise is configured in `MIDDLEWARE`

**Database connection errors:**
- Check `DATABASE_URL` is correctly set in Config Vars
- Verify your Code Institute database credentials are correct
- Ensure the database has not expired (18 month limit)

**Stripe payments not working:**
- Verify all Stripe keys are correctly set in Config Vars
- Ensure you're using test keys for sandbox mode
- Check that `STRIPE_PUBLIC_KEY` and `STRIPE_SECRET_KEY` are correct

**Cloudinary images not displaying:**
- Verify Cloudinary credentials are correct
- Check image URLs use HTTPS
- Ensure `DEFAULT_FILE_STORAGE` is set correctly

**Application error on Heroku:**
- Check Heroku logs: `heroku logs --tail`
- Verify all Config Vars are set
- Ensure `Procfile` exists with correct content:
  ```
  web: gunicorn david_visuals_project.wsgi
  ```

---

[Back to README](README.md)
