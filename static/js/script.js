// Wait until the page loads
document.addEventListener("DOMContentLoaded", function () {

    // ==========================
    // Report Form Confirmation
    // ==========================
    const form = document.querySelector("form");

    if (form) {

        form.addEventListener("submit", function (event) {

            const confirmSubmit = confirm(
                "Are you sure you want to submit this issue?"
            );

            if (!confirmSubmit) {
                event.preventDefault();
            }

        });

    }

    // ==========================
    // Auto-hide Success Message
    // ==========================
    const alertBox = document.querySelector(".alert");

    if (alertBox) {

        setTimeout(function () {

            alertBox.style.transition = "opacity 0.5s";
            alertBox.style.opacity = "0";

            setTimeout(function () {
                alertBox.style.display = "none";
            }, 500);

        }, 3000);

    }

});