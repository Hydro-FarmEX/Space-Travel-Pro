document.addEventListener('DOMContentLoaded', function() {
    async function loadAITips() {
        try {
            const response = await fetch('/api/ai_tips');
            const data = await response.json();
            
            if (response.ok) {
                const tipsElement = document.getElementById('aiTips');
                const tips = JSON.parse(data.tips);
                
                let tipsHtml = '<ul class="list-unstyled">';
                tips.tips.forEach(tip => {
                    tipsHtml += `<li class="mb-2">• ${tip}</li>`;
                });
                tipsHtml += '</ul>';
                
                tipsElement.innerHTML = tipsHtml;
            } else {
                document.getElementById('aiTips').innerHTML = 
                    '<p class="text-danger">Failed to load travel tips</p>';
            }
        } catch (error) {
            document.getElementById('aiTips').innerHTML = 
                '<p class="text-danger">Error loading travel tips</p>';
        }
    }

    loadAITips();
});
