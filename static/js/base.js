    document.addEventListener("DOMContentLoaded", function () {
        const paymentToggle = document.getElementById('paymentTypeToggle');
        const recurringOptions = document.getElementById('recurringOptions');
        const oneTimeOptions = document.getElementById('oneTimeOptions');

        function updatePaymentDisplay() {
            if (paymentToggle.checked) {
                recurringOptions.style.display = 'block';
                oneTimeOptions.style.display = 'none';
            } else {
                recurringOptions.style.display = 'none';
                oneTimeOptions.style.display = 'block';
            }
        }

        // Initialize default state
        updatePaymentDisplay();

        // Add event listener for toggle switch
        paymentToggle.addEventListener('change', updatePaymentDisplay);
    });