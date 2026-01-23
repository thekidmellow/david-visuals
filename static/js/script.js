document.addEventListener('DOMContentLoaded', function() {
    
    const messages = document.querySelectorAll('.alert');
    if (messages.length > 0) {
        messages.forEach(message => {
            setTimeout(() => {
                message.style.opacity = '0';
                setTimeout(() => {
                    message.remove();
                }, 300);
            }, 5000);
        });
    }

    const deleteButtons = document.querySelectorAll('.btn-danger');
    deleteButtons.forEach(button => {
        if (button.textContent.includes('Delete')) {
            button.addEventListener('click', function(e) {
                if (!confirm('Are you sure you want to delete this item?')) {
                    e.preventDefault();
                }
            });
        }
    });

    const forms = document.querySelectorAll('form');
    forms.forEach(form => {
        form.addEventListener('submit', function(e) {
            const requiredFields = form.querySelectorAll('[required]');
            let isValid = true;
            
            requiredFields.forEach(field => {
                if (!field.value.trim()) {
                    isValid = false;
                    field.style.borderColor = '#e74c3c';
                } else {
                    field.style.borderColor = '#ddd';
                }
            });
            
            if (!isValid) {
                e.preventDefault();
                alert('Please fill in all required fields.');
            }
        });
    });

    const emailFields = document.querySelectorAll('input[type="email"]');
    emailFields.forEach(field => {
        field.addEventListener('blur', function() {
            const emailPattern = /^[^\s@]+@[^\s@]+\.[^\s@]+$/;
            if (field.value && !emailPattern.test(field.value)) {
                field.style.borderColor = '#e74c3c';
                let errorMsg = field.parentElement.querySelector('.error-message');
                if (!errorMsg) {
                    errorMsg = document.createElement('span');
                    errorMsg.className = 'error-message';
                    errorMsg.textContent = 'Please enter a valid email address';
                    field.parentElement.appendChild(errorMsg);
                }
            } else {
                field.style.borderColor = '#ddd';
                const errorMsg = field.parentElement.querySelector('.error-message');
                if (errorMsg) {
                    errorMsg.remove();
                }
            }
        });
    });

    const navToggle = document.getElementById('navToggle');
    const navLinks = document.getElementById('navLinks');

    if (navToggle && navLinks) {
        navToggle.addEventListener('click', function() {
            navToggle.classList.toggle('active');
            navLinks.classList.toggle('active');
        });

        document.addEventListener('click', function(event) {
            if (!navToggle.contains(event.target) && !navLinks.contains(event.target)) {
                navToggle.classList.remove('active');
                navLinks.classList.remove('active');
            }
        });
    }

    const backToTop = document.createElement('button');
    backToTop.innerHTML = '↑';
    backToTop.className = 'back-to-top';
    backToTop.setAttribute('aria-label', 'Back to top');
    backToTop.style.display = 'none';
    document.body.appendChild(backToTop);

    window.addEventListener('scroll', function() {
        if (window.pageYOffset > 300) {
            backToTop.style.display = 'block';
        } else {
            backToTop.style.display = 'none';
        }
    });

    backToTop.addEventListener('click', function() {
        window.scrollTo({
            top: 0,
            behavior: 'smooth'
        });
    });

    const priceElements = document.querySelectorAll('.package-price, .package-detail-price');
    priceElements.forEach(element => {
        const price = element.textContent;
        if (price && !price.includes('€')) {
            element.textContent = '€' + price;
        }
    });
});