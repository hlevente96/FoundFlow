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

    document.getElementById('customAmountBtn').addEventListener('click', function(e) {
      e.preventDefault();

      // Hide the initial button
      const button = document.getElementById('customAmountBtn');
      button.style.display = 'none';

      // Show the input field
      const input = document.getElementById('customAmount');
      input.style.display = 'inline-block';

      // Show the second "Előfizetek" button below the input field
      const newButton = document.getElementById('newSubscriptionBtn');
      newButton.style.display = 'block';
    });
    document.getElementById('customAmountBtnOT').addEventListener('click', function(e) {
      e.preventDefault();

      // Hide the initial button
      const button = document.getElementById('customAmountBtnOT');
      button.style.display = 'none';

      // Show the input field
      const input = document.getElementById('customAmountOT');
      input.style.display = 'inline-block';

      // Show the second "Előfizetek" button below the input field
      const newButton = document.getElementById('newSubscriptionBtnOT');
      newButton.style.display = 'block';
    });