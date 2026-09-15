document.addEventListener("DOMContentLoaded", function () {
    const contactForm = document.querySelector(".contact-form");
    if (!contactForm) return;

    contactForm.addEventListener("submit", function (e) {
        const name = document.getElementById("name").value.trim();
        const mobile = document.getElementById("mobile").value.trim();

        if (!name || !mobile) {
            e.preventDefault();
            alert("Please fill in your Name and Mobile Number.");
        }
    });
});