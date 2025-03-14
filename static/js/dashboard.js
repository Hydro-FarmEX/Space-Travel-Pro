document.addEventListener('DOMContentLoaded', function() {
    async function loadAITips() {
        const tipsElement = document.getElementById('aiTips');

        try {
            const response = await fetch('/api/ai_tips');
            const data = await response.json();

            if (response.ok) {
                let tips;
                try {
                    // Handle both string and parsed JSON responses
                    tips = typeof data.tips === 'string' ? JSON.parse(data.tips) : data.tips;
                } catch (e) {
                    tips = data;
                }

                if (Array.isArray(tips.tips)) {
                    let tipsHtml = '<ul class="list-unstyled">';
                    tips.tips.forEach(tip => {
                        tipsHtml += `<li class="mb-2">• ${tip}</li>`;
                    });
                    tipsHtml += '</ul>';
                    tipsElement.innerHTML = tipsHtml;
                } else {
                    throw new Error('Invalid tips format');
                }
            } else {
                throw new Error(data.error || 'Failed to load travel tips');
            }
        } catch (error) {
            console.error('Error loading tips:', error);
            tipsElement.innerHTML = `
                <div class="alert alert-info">
                    <h5>Travel Tips</h5>
                    <ul class="list-unstyled">
                        <li class="mb-2">• Consider starting with shorter trips to get acclimated to space travel</li>
                        <li class="mb-2">• Pack light and focus on essential items approved for space travel</li>
                        <li class="mb-2">• Take advantage of pre-flight training programs to prepare for your journey</li>
                    </ul>
                </div>`;
        }
    }

    loadAITips();
});