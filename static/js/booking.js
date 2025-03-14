document.addEventListener('DOMContentLoaded', function() {
    const bookButtons = document.querySelectorAll('.book-trip');
    
    bookButtons.forEach(button => {
        button.addEventListener('click', async function() {
            const tripId = this.dataset.tripId;
            try {
                const response = await fetch('/api/book_trip', {
                    method: 'POST',
                    headers: {
                        'Content-Type': 'application/json'
                    },
                    body: JSON.stringify({ trip_id: tripId })
                });
                
                const data = await response.json();
                
                if (response.ok) {
                    alert('Booking successful!');
                    window.location.href = '/dashboard';
                } else {
                    alert('Booking failed: ' + data.error);
                }
            } catch (error) {
                alert('Error making booking: ' + error.message);
            }
        });
    });
});
