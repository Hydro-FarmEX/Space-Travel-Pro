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
async function connectWallet() {
    if (typeof window.ethereum !== 'undefined') {
        try {
            const accounts = await window.ethereum.request({ method: 'eth_requestAccounts' });
            return accounts[0];
        } catch (error) {
            console.error('Error connecting wallet:', error);
            return null;
        }
    }
    return null;
}

async function loadAchievements() {
    try {
        const response = await fetch('/api/user/achievements');
        const data = await response.json();
        
        document.querySelector('.points').textContent = `${data.points} pts`;
        
        const badgesGrid = document.querySelector('.badges-grid');
        badgesGrid.innerHTML = data.achievements.map(achievement => `
            <div class="achievement-badge">
                <span class="achievement-icon">${achievement.icon}</span>
                <h5>${achievement.name}</h5>
                <p>${achievement.description}</p>
            </div>
        `).join('');
    } catch (error) {
        console.error('Error loading achievements:', error);
    }
}

async function loadLeaderboard() {
    try {
        const response = await fetch('/api/leaderboard');
        const data = await response.json();
        
        const leaderboardList = document.querySelector('.leaderboard-list');
        leaderboardList.innerHTML = data.map((user, index) => `
            <div class="leaderboard-item">
                <span class="rank">#${index + 1}</span>
                <span class="user-info">
                    <strong>User ${user.user_id}</strong>
                    <small>${user.points} pts</small>
                </span>
                <span class="badges">
                    ${user.achievements.map(a => a.icon).join(' ')}
                </span>
            </div>
        `).join('');
    } catch (error) {
        console.error('Error loading leaderboard:', error);
    }
}

document.addEventListener('DOMContentLoaded', () => {
    loadAchievements();
    loadLeaderboard();
});
