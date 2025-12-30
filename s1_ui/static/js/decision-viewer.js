/**
 * Decision Viewer Module
 * Displays decision documents
 */

const DecisionViewer = {
    async load() {
        S1App.showLoading();
        
        try {
            const data = await S1App.apiCall('/decisions');
            this.renderDecisionList(data.decisions);
        } catch (error) {
            S1App.showError('Failed to load decisions: ' + error.message);
        }
    },
    
    renderDecisionList(decisions) {
        if (!decisions || decisions.length === 0) {
            S1App.showContent('<p>No decisions found.</p>');
            return;
        }
        
        const html = `
            <h2>Decisions</h2>
            <div class="decision-list">
                ${decisions.map(decision => `
                    <div class="decision-item ${decision.human_signed ? 'signed' : 'unsigned'}" 
                         onclick="DecisionViewer.showDecision('${decision.id}')">
                        <h4>${decision.id}</h4>
                        <p>Phase: ${decision.phase || 'N/A'}</p>
                        <p>Signed: ${decision.human_signed ? '✓ Yes' : '✗ No'}</p>
                    </div>
                `).join('')}
            </div>
        `;
        
        S1App.showContent(html);
    },
    
    async showDecision(decisionId) {
        S1App.showLoading();
        
        try {
            const data = await S1App.apiCall(`/decisions/${decisionId}`);
            this.renderDecisionDetails(data);
        } catch (error) {
            S1App.showError('Failed to load decision: ' + error.message);
        }
    },
    
    renderDecisionDetails(decision) {
        const questionsHtml = decision.questions.length > 0 ? 
            `<ul>${decision.questions.map(q => `<li>${q}</li>`).join('')}</ul>` : 
            '<p>No questions extracted.</p>';
        
        const answersHtml = decision.answers.length > 0 ? 
            `<ul>${decision.answers.map(a => `<li>${a}</li>`).join('')}</ul>` : 
            '<p>No answers extracted.</p>';
        
        const html = `
            <div>
                <button onclick="DecisionViewer.load()" style="margin-bottom: 20px;">← Back to Decisions</button>
                <h2>${decision.id}</h2>
                <p>Phase: ${decision.phase || 'N/A'}</p>
                <p>Signed: ${decision.human_signed ? '✓ Yes' : '✗ No'}</p>
                
                <h3 style="margin-top: 30px;">Questions</h3>
                ${questionsHtml}
                
                <h3 style="margin-top: 30px;">Answers</h3>
                ${answersHtml}
                
                <h3 style="margin-top: 30px;">Full Content</h3>
                <div class="markdown-content">${decision.content}</div>
            </div>
        `;
        
        S1App.showContent(html);
    }
};

