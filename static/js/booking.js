
document.addEventListener('DOMContentLoaded', function() {
    // Initialize Leaflet map
    const map = L.map('map').setView([25.2048, 55.2708], 13);
    L.tileLayer('https://{s}.tile.openstreetmap.org/{z}/{x}/{y}.png', {
        attribution: '© OpenStreetMap contributors'
    }).addTo(map);

    // Add launch site marker
    const launchMarker = L.marker([25.2048, 55.2708]).addTo(map);
    launchMarker.bindPopup("<b>Launch Site</b><br>Museum of the Future, Dubai").openPopup();

    // Initialize countdown
    function updateCountdown() {
        const now = new Date();
        const nextLaunch = new Date(now.getFullYear(), now.getMonth(), now.getDate() + 1);
        const diff = nextLaunch - now;
        
        const hours = Math.floor(diff / (1000 * 60 * 60));
        const minutes = Math.floor((diff % (1000 * 60 * 60)) / (1000 * 60));
        const seconds = Math.floor((diff % (1000 * 60)) / 1000);
        
        document.getElementById('countdown').textContent = 
            `${hours}h ${minutes}m ${seconds}s`;
    }
    
    setInterval(updateCountdown, 1000);
    updateCountdown();

    // Booking functionality
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

    // Accommodation booking functionality
    const accButtons = document.querySelectorAll('.book-accommodation');
    accButtons.forEach(button => {
        button.addEventListener('click', async function() {
            const accId = this.dataset.accId;
            try {
                const response = await fetch('/api/book_accommodation', {
                    method: 'POST',
                    headers: {
                        'Content-Type': 'application/json'
                    },
                    body: JSON.stringify({ accommodation_id: accId })
                });
                
                const data = await response.json();
                
                if (response.ok) {
                    alert('Accommodation booked successfully!');
                    window.location.href = '/dashboard';
                } else {
                    alert('Booking failed: ' + data.error);
                }
            } catch (error) {
                alert('Error making booking: ' + error.message);
            }
        });
    });

    // Initialize Feather icons
    feather.replace();

    // Add hover animations to trip cards
    const tripCards = document.querySelectorAll('.trip-card');
    tripCards.forEach(card => {
        card.addEventListener('mouseenter', () => {
            card.style.transform = 'translateY(-5px)';
            card.style.transition = 'transform 0.3s ease';
        });
        
        card.addEventListener('mouseleave', () => {
            card.style.transform = 'translateY(0)';
        });
    });
});
