    // Select payment option
    document.addEventListener("DOMContentLoaded", function () {
        const paymentTypePile = document.getElementById('paymentTypePile');
        const recurringOptions = document.getElementById('recurringOptions');
        const oneTimeOptions = document.getElementById('oneTimeOptions');

        if (paymentTypePile) {
            // Display recurringOptions by default
            if (paymentTypePile.value === 'recurring') {
                recurringOptions.style.display = 'block';
                oneTimeOptions.style.display = 'none';
            } else if (paymentTypePile.value === 'one-time') {
                recurringOptions.style.display = 'none';
                oneTimeOptions.style.display = 'block';
            }

            // Update on change
            paymentTypePile.addEventListener('change', function () {
                if (this.value === 'recurring') {
                    recurringOptions.style.display = 'block';
                    oneTimeOptions.style.display = 'none';
                } else if (this.value === 'one-time') {
                    recurringOptions.style.display = 'none';
                    oneTimeOptions.style.display = 'block';
                }
            });
        }
    });
