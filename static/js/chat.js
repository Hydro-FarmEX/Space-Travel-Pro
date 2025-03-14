document.addEventListener('DOMContentLoaded', function() {
    const chatToggle = document.getElementById('chatToggle');
    const chatWidget = document.getElementById('chatWidget');
    const chatInput = document.getElementById('chatInput');
    const chatMessages = document.getElementById('chatMessages');

    // Initialize Feather icons
    feather.replace();

    chatToggle.addEventListener('click', function() {
        chatWidget.classList.toggle('active');
        if (chatWidget.classList.contains('active')) {
            chatInput.focus();
        }
    });

    window.sendMessage = async function() {
        const message = chatInput.value.trim();
        if (!message) return;

        // Add user message to chat
        addMessage(message, 'user');
        chatInput.value = '';

        try {
            const response = await fetch('/api/chat', {
                method: 'POST',
                headers: {
                    'Content-Type': 'application/json'
                },
                body: JSON.stringify({ message })
            });

            const data = await response.json();
            
            if (response.ok) {
                addMessage(data.response, 'bot');
            } else {
                addMessage('Sorry, I encountered an error. Please try again.', 'bot');
            }
        } catch (error) {
            console.error('Chat error:', error);
            addMessage('Sorry, I encountered an error. Please try again.', 'bot');
        }
    };

    function addMessage(text, type) {
        const messageDiv = document.createElement('div');
        messageDiv.className = `message ${type}-message`;
        messageDiv.textContent = text;
        chatMessages.appendChild(messageDiv);
        chatMessages.scrollTop = chatMessages.scrollHeight;
    }
});
