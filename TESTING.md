# Testing

Testing for this project was conducted primarily through **manual testing and validation tools**, in line with the scope of the project and learning outcomes. Automated test suites and continuous integration pipelines were not implemented.

This document outlines the testing procedures and results for the David Visuals e-commerce platform.

---

## Table of Contents

- [Code Validation](#code-validation)
  - [HTML Validation](#html-validation)
  - [CSS Validation](#css-validation)
  - [JavaScript Validation](#javascript-validation)
  - [Python Validation](#python-validation)
- [Lighthouse Testing](#lighthouse-testing)
- [Browser Compatibility](#browser-compatibility)
  - [Chrome](#chrome)
  - [Firefox](#firefox)
  - [Safari](#safari)
- [Responsiveness Testing](#responsiveness-testing)
  - [Mobile View](#mobile-view)
  - [Tablet View](#tablet-view)
- [Manual Testing](#manual-testing)
  - [Navigation Testing](#navigation-testing)
  - [Authentication Testing](#authentication-testing)
  - [Package Browsing Testing](#package-browsing-testing)
  - [Checkout and Payment Testing](#checkout-and-payment-testing)
  - [Profile Testing](#profile-testing)
  - [Admin Testing](#admin-testing)
  - [Footer Testing](#footer-testing)
- [User Story Testing](#user-story-testing)
- [Bugs](#bugs)
  - [Fixed Bugs](#fixed-bugs)
  - [Unfixed Bugs](#unfixed-bugs)

---

## Code Validation

### HTML Validation

All HTML pages were validated using the [W3C Markup Validation Service](https://validator.w3.org/). Pages were tested by direct input of the rendered HTML source code.

| Page | Result | Screenshot |
|------|--------|------------|
| Home | Pass - No errors or warnings | ![HTML Home](static/images/VALIDATIONS/W3CVALIDATOR_Home.png) |
| Package List | Pass - No errors or warnings | ![HTML Package List](static/images/VALIDATIONS/W3CVALIDATOR_Package_list.png) |
| Package Detail | Pass - No errors or warnings | ![HTML Package Detail](static/images/VALIDATIONS/W3CVALIDATOR_Package_detail.png) |
| Login | Pass - No errors or warnings | ![HTML Login](static/images/VALIDATIONS/W3CVALIDATOR_Login.png) |
| Sign Up | Pass - No errors or warnings | ![HTML Signup](static/images/VALIDATIONS/W3CVALIDATOR_Signup.html.png) |
| Logout | Pass - No errors or warnings | ![HTML Logout](static/images/VALIDATIONS/W3CVALIDATOR_Logoutpage.png) |
| Unsubscribe | Pass - No errors or warnings | ![HTML Unsubscribe](static/images/VALIDATIONS/W3CVALIDATOR_Unsubscribe.png) |
| Profile | Pass - No errors or warnings | ![HTML Profile](static/images/VALIDATIONS/W3CVALIDATOR_Profilepage.png) |
| Checkout | Pass - No errors or warnings | ![HTML Checkout](static/images/VALIDATIONS/W3CVALIDATOR_Checkoutpage.png) |
| 404 | Pass - No errors or warnings | ![HTML 404](static/images/VALIDATIONS/W3CVALIDATOR_404page.png) |



### CSS Validation

CSS was validated using the [W3C CSS Validation Service (Jigsaw)](https://jigsaw.w3.org/css-validator/).

| File | Result | Screenshot |
|------|--------|------------|
| style.css | Pass - No errors | ![CSS Validation](static/images/VALIDATIONS/jigsaw.w3.org_css-validator_validator.png) |

### JavaScript Validation

JavaScript was validated using [JSHint](https://jshint.com/).

| File | Result | Screenshot |
|------|--------|------------|
| script.js | Pass - No errors | ![JSHint](static/images/VALIDATIONS/jshint_validation.png) |

Configuration used:
- ES6 features enabled
- jQuery globals recognised

### Python Validation

Python code was validated using pycodestyle (formerly pep8) to ensure PEP8 compliance.

| File | Result | Screenshot |
|------|--------|------------|
| All Python files | Pass - No errors | ![PEP8](static/images/VALIDATIONS/PEP8_validation.png) |

---

## Lighthouse Testing

Lighthouse audits were performed using Chrome DevTools to assess Performance, Accessibility, Best Practices, and SEO.

| Page | Performance | Accessibility | Best Practices | SEO | Screenshot |
|------|-------------|---------------|----------------|-----|------------|
| Home | 99 | 93 | 100 | 100 | ![Lighthouse Home](static/images/LIGHTHOUSE_AUDIT/Lighthouse_Home.png) |
| Package List | 97 | 94 | 77 | 100 | ![Lighthouse Packages](static/images/LIGHTHOUSE_AUDIT/Lighthouse_Package_list.png) |
| Package Detail | 98 | 94 | 77 | 100 | ![Lighthouse Detail](static/images/LIGHTHOUSE_AUDIT/Lighthouse_Package_detail.png) |
| Login | 91 | 94 | 100 | 63 | ![Lighthouse Login](static/images/LIGHTHOUSE_AUDIT/Lighthouse_Login.png) |
| Sign Up | 100 | 94 | 100 | 63 | ![Lighthouse Signup](static/images/LIGHTHOUSE_AUDIT/Lighthouse_Signup.png) |
| Logout | 100 | 93 | 100 | 63 | ![Lighthouse Logout](static/images/LIGHTHOUSE_AUDIT/Lighthouse_Logout.png) |
| Profile | 99 | 93 | 100 | 63 | ![Lighthouse Profile](static/images/LIGHTHOUSE_AUDIT/Lighthouse_Profile.png) |
| Checkout | 99 | 93 | 100 | 63 | ![Lighthouse Checkout](static/images/LIGHTHOUSE_AUDIT/Lighthouse_Checkout.png) |
| Unsubscribe | 99 | 93 | 100 | 100 | ![Lighthouse Unsubscribe](static/images/LIGHTHOUSE_AUDIT/Lighthouse_Unsubscribe.png) |
| Payment Success | 100 | 93 | 100 | 63 | ![Lighthouse Success](static/images/LIGHTHOUSE_AUDIT/Lighthouse_Payment_successful.png) |
| Payment Cancelled | 100 | 93 | 100 | 63 | ![Lighthouse Cancelled](static/images/LIGHTHOUSE_AUDIT/Lighthouse_Payment_cancelled_page.png) |
| 404 | 100 | 93 | 100 | 63 | ![Lighthouse 404](static/images/LIGHTHOUSE_AUDIT/Lighthouse_404_page.png) |

All pages achieved high performance and accessibility scores, with minor Lighthouse Best Practices recommendations noted.

---

## Browser Compatibility

The website was tested on multiple browsers to ensure consistent functionality and appearance.

### Chrome

| Page | Result | Screenshot |
|------|--------|------------|
| Home | Pass | ![Chrome Home](static/images/Chrome/Chrome_Home_page.png) |
| Package List | Pass | ![Chrome Package List](static/images/Chrome/Chrome_Package_list_page.png) |
| Package Detail | Pass | ![Chrome Package Detail](static/images/Chrome/Chrome_Package_detail_page.png) |
| Login | Pass | ![Chrome Login](static/images/Chrome/Chrome_Login_page.png) |
| Sign Up | Pass | ![Chrome Signup](static/images/Chrome/Chrome_Signup_page.png) |
| Logout | Pass | ![Chrome Logout](static/images/Chrome/Chrome_Logout_page.png) |
| Unsubscribe | Pass | ![Chrome Unsubscribe](static/images/Chrome/Chrome_Unsubscribe_page.png) |
| Profile | Pass | ![Chrome Profile](static/images/Chrome/Chrome_Profile_page.png) |
| Checkout | Pass | ![Chrome Checkout](static/images/Chrome/Chrome_Checkout_page.png) |
| Payment Success | Pass | ![Chrome Success](static/images/Chrome/Chrome_Payment_Successful_page.png) |
| Payment Cancelled | Pass | ![Chrome Cancelled](static/images/Chrome/Chrome_Payment_cancelled_page.png) |
| 404 | Pass | ![Chrome 404](static/images/Chrome/Chrome_404_page.png) |

### Firefox

| Page | Result | Screenshot |
|------|--------|------------|
| Home | Pass | ![Firefox Home](static/images/Firefox/Firefox_Home_page.png) |
| Package List | Pass | ![Firefox Package List](static/images/Firefox/Firefox_Package_list_page.png) |
| Package Detail | Pass | ![Firefox Package Detail](static/images/Firefox/Firefox_Package_detail_page.png) |
| Login | Pass | ![Firefox Login](static/images/Firefox/Firefox_login_page.png) |
| Sign Up | Pass | ![Firefox Signup](static/images/Firefox/Firefox_Signup_page.png) |
| Logout | Pass | ![Firefox Logout](static/images/Firefox/Firefox_Logout_page.png) |
| Unsubscribe | Pass | ![Firefox Unsubscribe](static/images/Firefox/Firefox_Unsubscribe_page.png) |
| Profile | Pass | ![Firefox Profile](static/images/Firefox/Firefox_Profile_page.png) |
| Checkout | Pass | ![Firefox Checkout](static/images/Firefox/Firefox_Checkout_page.png) |
| Payment Success | Pass | ![Firefox Success](static/images/Firefox/Firefox_Paymentsuccessful_page.png) |
| Payment Cancelled | Pass | ![Firefox Cancelled](static/images/Firefox/Firefox_Paymentcancelled_page.png) |
| 404 | Pass | ![Firefox 404](static/images/Firefox/Firefox_404_page.png) |

### Safari

| Page | Result | Screenshot |
|------|--------|------------|
| Home | Pass | ![Safari Home](static/images/Safari/Safari_Home_page.png) |
| Package List | Pass | ![Safari Package List](static/images/Safari/Safari_Package_list_page.png) |
| Package Detail | Pass | ![Safari Package Detail](static/images/Safari/Safari_Package_detail_page.png) |
| Login | Pass | ![Safari Login](static/images/Safari/Safari_Login_page.png) |
| Sign Up | Pass | ![Safari Signup](static/images/Safari/Safari_Signup_page.png) |
| Logout | Pass | ![Safari Logout](static/images/Safari/Safari_Logout_page.png) |
| Unsubscribe | Pass | ![Safari Unsubscribe](static/images/Safari/Safari_Unsubscribe_page.png) |
| Profile | Pass | ![Safari Profile](static/images/Safari/Safari_Profile_page.png) |
| Checkout | Pass | ![Safari Checkout](static/images/Safari/Safari_Checkout_page.png) |
| Payment Success | Pass | ![Safari Success](static/images/Safari/Safari_Paymentsuccessful_page.png) |
| Payment Cancelled | Pass | ![Safari Cancelled](static/images/Safari/Safari_Paymentcancelled_page.png) |
| 404 | Pass | ![Safari 404](static/images/Safari/Safari_404_page.png) |

All browsers displayed the site correctly with no visual discrepancies or functional issues.

---

## Responsiveness Testing

The website was tested for responsiveness using Chrome DevTools device emulation.

### Mobile View

| Page | Result | Screenshot |
|------|--------|------------|
| Home | Pass | ![Mobile Home](static/images/Responsiveness/Mobile_Home.png) |
| Package List | Pass | ![Mobile Package List](static/images/Responsiveness/Mobile_Package_list.png) |
| Package Detail | Pass | ![Mobile Package Detail](static/images/Responsiveness/Mobile_Package_detail.png) |
| Login | Pass | ![Mobile Login](static/images/Responsiveness/Mobile_Login_page.png) |
| Sign Up | Pass | ![Mobile Signup](static/images/Responsiveness/Mobile_Signup_page.png) |
| Logout | Pass | ![Mobile Logout](static/images/Responsiveness/Mobile_Logout_page.png) |
| Unsubscribe | Pass | ![Mobile Unsubscribe](static/images/Responsiveness/Mobile_Unsubscribe_page.png) |
| Profile | Pass | ![Mobile Profile](static/images/Responsiveness/Mobile_Profile_page.png) |
| Checkout | Pass | ![Mobile Checkout](static/images/Responsiveness/Mobile_Checkout_page.png) |
| Payment Success | Pass | ![Mobile Success](static/images/Responsiveness/Mobile_Payment_successful_page.png) |
| Payment Cancelled | Pass | ![Mobile Cancelled](static/images/Responsiveness/Mobile_Payment_cancelled.png) |
| 404 | Pass | ![Mobile 404](static/images/Responsiveness/Mobile_404_page.png) |

### Tablet View

| Page | Result | Screenshot |
|------|--------|------------|
| Home | Pass | ![Tablet Home](static/images/Responsiveness/tablet_Home_page.png) |
| Package List | Pass | ![Tablet Package List](static/images/Responsiveness/tablet_Package_list_page.png) |
| Package Detail | Pass | ![Tablet Package Detail](static/images/Responsiveness/tablet_Package_detail_page.png) |
| Login | Pass | ![Tablet Login](static/images/Responsiveness/tablet_Login_page.png) |
| Sign Up | Pass | ![Tablet Signup](static/images/Responsiveness/tablet_Signup_page.png) |
| Logout | Pass | ![Tablet Logout](static/images/Responsiveness/tablet_Logout_page.png) |
| Unsubscribe | Pass | ![Tablet Unsubscribe](static/images/Responsiveness/tablet_Unsubscribe_page.png) |
| Profile | Pass | ![Tablet Profile](static/images/Responsiveness/tablet_Profile_page.png) |
| Checkout | Pass | ![Tablet Checkout](static/images/Responsiveness/tablet_Checkout_page.png) |
| Payment Success | Pass | ![Tablet Success](static/images/Responsiveness/tablet_Payment_successful_page.png) |
| Payment Cancelled | Pass | ![Tablet Cancelled](static/images/Responsiveness/tablet_Payment_cancelled_page.png) |
| 404 | Pass | ![Tablet 404](static/images/Responsiveness/tablet_404_page.png) |

All pages adapt correctly to different screen sizes with proper layout adjustments, readable text, and accessible navigation.

---

## Manual Testing

### Navigation Testing

| Feature | Action | Expected Result | Actual Result | Pass/Fail |
|---------|--------|-----------------|---------------|-----------|
| Logo | Click logo | Redirects to home page | Redirects to home page | Pass |
| Home link | Click Home | Redirects to home page | Redirects to home page | Pass |
| Packages link | Click Packages | Redirects to package list | Redirects to package list | Pass |
| Login link | Click Login (logged out) | Redirects to login page | Redirects to login page | Pass |
| Sign Up link | Click Sign Up (logged out) | Redirects to signup page | Redirects to signup page | Pass |
| Profile link | Click Profile (logged in) | Redirects to profile page | Redirects to profile page | Pass |
| Admin link | Click Admin (superuser) | Redirects to admin panel | Redirects to admin panel | Pass |
| Logout link | Click Logout (logged in) | Redirects to logout confirmation | Redirects to logout confirmation | Pass |
| Mobile menu | Click hamburger icon | Opens mobile navigation | Opens mobile navigation | Pass |
| Mobile menu links | Click any link | Navigates correctly and closes menu | Navigates correctly and closes menu | Pass |

### Authentication Testing

| Feature | Action | Expected Result | Actual Result | Pass/Fail |
|---------|--------|-----------------|---------------|-----------|
| Sign Up | Submit valid registration form | Account created, redirected to home | Account created, redirected to home | Pass |
| Sign Up | Submit with existing username | Error message displayed | Error message displayed | Pass |
| Sign Up | Submit with mismatched passwords | Error message displayed | Error message displayed | Pass |
| Sign Up | Submit with invalid email | Error message displayed | Error message displayed | Pass |
| Login | Submit valid credentials | Logged in, redirected to home | Logged in, redirected to home | Pass |
| Login | Submit invalid credentials | Error message displayed | Error message displayed | Pass |
| Login | Click Remember Me | Session persists after browser close | Session persists after browser close | Pass |
| Logout | Click Logout button | Logged out, redirected to home | Logged out, redirected to home | Pass |
| Logout | Click Return to Homepage | Redirects to home without logging out | Redirects to home without logging out | Pass |
| Protected pages | Access profile while logged out | Redirected to login | Redirected to login | Pass |
| Protected pages | Access checkout while logged out | Redirected to login | Redirected to login | Pass |

### Package Browsing Testing

| Feature | Action | Expected Result | Actual Result | Pass/Fail |
|---------|--------|-----------------|---------------|-----------|
| Package list | Load packages page | All packages displayed | All packages displayed | Pass |
| Category filter | Click Logo Design | Only logo packages shown | Only logo packages shown | Pass |
| Category filter | Click Social Media | Only social media packages shown | Only social media packages shown | Pass |
| Category filter | Click Flyer/Poster | Only flyer packages shown | Only flyer packages shown | Pass |
| Category filter | Click All Packages | All packages shown | All packages shown | Pass |
| Package card | View package card | Shows image, name, price, description | Shows image, name, price, description | Pass |
| View Details | Click View Details button | Redirects to package detail page | Redirects to package detail page | Pass |
| Package detail | Load detail page | Shows full package information | Shows full package information | Pass |
| Package detail | View delivery time | Delivery time displayed | Delivery time displayed | Pass |
| Package detail | View revisions | Number of revisions displayed | Number of revisions displayed | Pass |
| Package detail | View inclusions | What's included list displayed | What's included list displayed | Pass |
| Purchase button | Click Buy Now (logged in) | Redirects to checkout | Redirects to checkout | Pass |
| Purchase button | Click Login to Purchase (logged out) | Redirects to login | Redirects to login | Pass |
| Back to Packages | Click Back to Packages | Returns to package list | Returns to package list | Pass |

### Checkout and Payment Testing

| Feature | Action | Expected Result | Actual Result | Pass/Fail |
|---------|--------|-----------------|---------------|-----------|
| Checkout page | Load checkout | Order summary displayed | Order summary displayed | Pass |
| Order summary | View details | Package name, price, delivery time shown | Package name, price, delivery time shown | Pass |
| Total | View total | Correct total amount displayed | Correct total amount displayed | Pass |
| Stripe button | Click Pay with Stripe | Redirects to Stripe checkout | Redirects to Stripe checkout | Pass |
| Stripe payment | Complete with test card 4242... | Payment successful | Payment successful | Pass |
| Success page | After successful payment | Order confirmation displayed | Order confirmation displayed | Pass |
| Success page | View order number | Unique order number shown | Unique order number shown | Pass |
| Success page | View order details | Package and amount shown | Package and amount shown | Pass |
| Cancel payment | Cancel on Stripe | Redirects to cancel page | Redirects to cancel page | Pass |
| Cancel page | View cancel message | Cancellation confirmed, no charge | Cancellation confirmed, no charge | Pass |
| Browse Packages | Click on cancel page | Returns to package list | Returns to package list | Pass |
| Return Home | Click on success/cancel page | Returns to home page | Returns to home page | Pass |

### Profile Testing

| Feature | Action | Expected Result | Actual Result | Pass/Fail |
|---------|--------|-----------------|---------------|-----------|
| Profile page | Load profile | Account information displayed | Account information displayed | Pass |
| Account info | View username | Correct username shown | Correct username shown | Pass |
| Account info | View email | Correct email shown | Correct email shown | Pass |
| Account info | View member since | Registration date shown | Registration date shown | Pass |
| Update form | View form fields | Phone, address fields available | Phone, address fields available | Pass |
| Update profile | Enter phone number | Field accepts input | Field accepts input | Pass |
| Update profile | Enter address | All address fields accept input | All address fields accept input | Pass |
| Save changes | Click Update Profile | Profile updated, success message | Profile updated, success message | Pass |
| Data persistence | Reload page after update | Updated data still displayed | Updated data still displayed | Pass |

### Admin Testing

| Feature | Action | Expected Result | Actual Result | Pass/Fail |
|---------|--------|-----------------|---------------|-----------|
| Admin access | Login as superuser | Admin link visible in nav | Admin link visible in nav | Pass |
| Admin panel | Click Admin link | Django admin panel opens | Django admin panel opens | Pass |
| Packages | View packages in admin | All packages listed | All packages listed | Pass |
| Packages | Add new package | Package created successfully | Package created successfully | Pass |
| Packages | Edit package | Changes saved correctly | Changes saved correctly | Pass |
| Packages | Delete package | Package removed | Package removed | Pass |
| Orders | View orders | All orders listed | All orders listed | Pass |
| Orders | View order details | Full order information shown | Full order information shown | Pass |
| Users | View users | All users listed | All users listed | Pass |
| Subscribers | View newsletter subscribers | Subscriber list displayed | Subscriber list displayed | Pass |

### Footer Testing

| Feature | Action | Expected Result | Actual Result | Pass/Fail |
|---------|--------|-----------------|---------------|-----------|
| Footer | Scroll to bottom | Footer visible on all pages | Footer visible on all pages | Pass |
| Quick Links | Click Home | Navigates to home | Navigates to home | Pass |
| Quick Links | Click Packages | Navigates to packages | Navigates to packages | Pass |
| Quick Links | Click Profile (logged in) | Navigates to profile | Navigates to profile | Pass |
| Social link | Click Facebook | Opens Facebook in new tab | Opens Facebook in new tab | Pass |
| Newsletter | Enter valid email | Success message displayed | Success message displayed | Pass |
| Newsletter | Enter invalid email | Error message displayed | Error message displayed | Pass |
| Newsletter | Submit empty form | Validation prevents submission | Validation prevents submission | Pass |
| Newsletter | Subscribe existing email | Appropriate message displayed | Appropriate message displayed | Pass |

---

## User Story Testing

| User Story | How It Was Achieved | Screenshot |
|------------|---------------------|------------|
| As a visitor, I want to view available design packages so I can see what services are offered | The Packages page displays all available design packages with images, prices, and descriptions. Category filters allow easy browsing. | ![Packages](static/images/PAGES/Package_list.png) |
| As a visitor, I want to view package details so I can make an informed decision | Each package has a detailed page showing price, delivery time, revisions, and what's included. | ![Detail](static/images/PAGES/Package_details.png) |
| As a visitor, I want to create an account so I can purchase packages | The Sign Up page allows visitors to register with username, email, and password. | ![Signup](static/images/PAGES/Signup_page.png) |
| As a user, I want to login to my account so I can access my profile and make purchases | The Login page provides secure authentication with optional Remember Me functionality. | ![Login](static/images/PAGES/Login_page.png) |
| As a user, I want to purchase a design package securely | Stripe integration provides secure payment processing with test and live card support. | ![Checkout](static/images/PAGES/Checkout_page.png) |
| As a user, I want to receive confirmation of my purchase | The Payment Success page displays order confirmation with order number and details. | ![Success](static/images/PAGES/Payment_successful_page.png) |
| As a user, I want to update my profile information | The Profile page allows users to update phone number and address details. | ![Profile](static/images/PAGES/Profile_page.png) |
| As an admin, I want to manage packages | Django admin panel provides full CRUD functionality for packages. | ![Admin](static/images/PAGES/Admin_page.png) |

---

## Bugs

### Fixed Bugs

| Bug | Description | Solution |
|-----|-------------|----------|
| Static files not loading in production | When DEBUG=False, CSS and JavaScript files were not being served on Heroku | Configured WhiteNoise middleware correctly in settings.py and ensured STATIC_ROOT was set. Ran collectstatic and verified static files were being served properly. |
| Profile update redirect loop | After updating profile, users were caught in a redirect loop instead of seeing success message | Fixed the view logic to properly handle POST requests and redirect to the profile page with a success message after saving. |
| Cloudinary images not displaying | Package images stored in Cloudinary were not loading on the deployed site | Updated CLOUDINARY_STORAGE settings in settings.py and ensured the cloudinary credentials were properly configured in Heroku config vars. Verified image URLs were using HTTPS. |

### Unfixed Bugs

There are no known unfixed bugs in the application. All identified issues during development and testing have been resolved.

---

[Back to README](README.md)
