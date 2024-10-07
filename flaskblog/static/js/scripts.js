// Toggle Password and Confirm Password Visibility
const togglePassword = document.getElementById('togglePassword');
const toggleConfirmPassword = document.getElementById('toggleConfirmPassword');
const passwordInput = document.getElementById('passwordInput');
const confirmPasswordInput = document.getElementById('confirmpasswordInput');
const toggleIcon = document.getElementById('toggleIcon');
const toggleConfirmIcon = document.getElementById('toggleConfirmIcon');

if (togglePassword) {
    togglePassword.addEventListener('click', function () {
        const type = passwordInput.getAttribute('type') === 'password' ? 'text' : 'password';
        passwordInput.setAttribute('type', type);
        toggleIcon.classList.toggle('bi-eye');
        toggleIcon.classList.toggle('bi-eye-slash');
    });
}

if (toggleConfirmPassword) {
    toggleConfirmPassword.addEventListener('click', function () {
        const type = confirmPasswordInput.getAttribute('type') === 'password' ? 'text' : 'password';
        confirmPasswordInput.setAttribute('type', type);
        toggleConfirmIcon.classList.toggle('bi-eye');
        toggleConfirmIcon.classList.toggle('bi-eye-slash');
    });
}

// Function to handle placeholder visibility for any input
function handlePlaceholder(inputElement) {
    inputElement.addEventListener('focus', function () {
        this.setAttribute('data-placeholder', this.getAttribute('placeholder'));
        this.setAttribute('placeholder', '');
    });

    inputElement.addEventListener('blur', function () {
        if (this.value === '') {
            this.setAttribute('placeholder', this.getAttribute('data-placeholder'));
        }
    });
}

// Apply placeholder handling to relevant fields
const nameInput = document.getElementById('nameInput');
const usernameInput = document.getElementById('usernameInput');
const emailInput = document.getElementById('emailInput');
const bioInput = document.getElementById('bioInput');

if (nameInput) handlePlaceholder(nameInput);
if (usernameInput) handlePlaceholder(usernameInput);
if (emailInput) handlePlaceholder(emailInput);
if (bioInput) handlePlaceholder(bioInput);
if (passwordInput) handlePlaceholder(passwordInput);
if (confirmPasswordInput) handlePlaceholder(confirmPasswordInput);

// Initialize and show toasts with smooth animation and auto-dismiss after 5 seconds
var toastElList = [].slice.call(document.querySelectorAll('.toast'));
var toastList = toastElList.map(function (toastEl) {
    var toast = new bootstrap.Toast(toastEl, { autohide: true, delay: 5000 });
    toast.show();  // Show the toast with fade-in effect
    return toast;
});
