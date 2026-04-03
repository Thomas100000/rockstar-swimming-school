document.addEventListener("DOMContentLoaded", () => {
    // 1. Mobile Hamburger Menu
    const hamburger = document.querySelector('.hamburger');
    const navLinks = document.querySelector('.nav-links');
    if (hamburger && navLinks) {
        hamburger.addEventListener('click', () => {
            navLinks.classList.toggle('active');
            hamburger.classList.toggle('active');
        });
    }

    // 2. Initialize VanillaTilt explicitly if needed (auto-init happens via data-tilt attributes, but just to be sure)
    if (typeof VanillaTilt !== 'undefined') {
        const tiltElements = document.querySelectorAll("[data-tilt]");
        if(tiltElements.length > 0) {
            VanillaTilt.init(tiltElements);
        }
    }

    // 3. Form Validation Logic
    const enquiryForm = document.getElementById("enquiryForm");
    if (enquiryForm) {
        const nameInput = document.getElementById("id_name");
        const emailInput = document.getElementById("id_email");
        const mobileInput = document.getElementById("id_mobile_number");

        const nameError = document.getElementById("nameError");
        const emailError = document.getElementById("emailError");
        const mobileError = document.getElementById("mobileError");

        const validateName = () => {
            if (nameInput.value.trim().length < 2) {
                nameError.textContent = "Name must be at least 2 characters.";
                nameInput.classList.add("invalid");
                nameInput.classList.remove("valid");
                return false;
            } else {
                nameError.textContent = "";
                nameInput.classList.remove("invalid");
                nameInput.classList.add("valid");
                return true;
            }
        };

        const validateEmail = () => {
            const re = /^[^\s@]+@[^\s@]+\.[^\s@]+$/;
            if (!re.test(emailInput.value.trim())) {
                emailError.textContent = "Please enter a valid email address.";
                emailInput.classList.add("invalid");
                emailInput.classList.remove("valid");
                return false;
            } else {
                emailError.textContent = "";
                emailInput.classList.remove("invalid");
                emailInput.classList.add("valid");
                return true;
            }
        };

        const validateMobile = () => {
            const re = /^\+?1?\d{9,15}$/;
            if (!re.test(mobileInput.value.trim())) {
                mobileError.textContent = "Valid 10-15 digit mobile number required.";
                mobileInput.classList.add("invalid");
                mobileInput.classList.remove("valid");
                return false;
            } else {
                mobileError.textContent = "";
                mobileInput.classList.remove("invalid");
                mobileInput.classList.add("valid");
                return true;
            }
        };

        nameInput.addEventListener("input", validateName);
        emailInput.addEventListener("input", validateEmail);
        mobileInput.addEventListener("input", validateMobile);

        enquiryForm.addEventListener("submit", (e) => {
            const isNameValid = validateName();
            const isEmailValid = validateEmail();
            const isMobileValid = validateMobile();

            if (!isNameValid || !isEmailValid || !isMobileValid) {
                e.preventDefault();
            }
        });
    }

    // 4. Still Image Background is now handled via CSS for Kainakary theme.
});
