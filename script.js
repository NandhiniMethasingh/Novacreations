<script>
function validateForm() {
    const email = document.getElementById("email").value;
    const password = document.getElementById("password").value;
    const emailPattern = /^[^\s@]+@[^\s@]+\.[^\s@]+$/; // Simple email regex
    const passwordPattern = /^(?=.*[A-Za-z])(?=.*\d)[A-Za-z\d]{8,}$/; // At least 8 chars, 1 letter, 1 number

    let valid = true;
    let errorMessage = "";

    if (!emailPattern.test(email)) {
        valid = false;
        errorMessage += "Invalid email format.\n";
    }

    if (!passwordPattern.test(password)) {
        valid = false;
        errorMessage += "Password must be at least 8 characters long, include at least one letter and one number.\n";
    }

    if (!valid) {
        alert(errorMessage);
    }

    return valid;
}
</script>

   