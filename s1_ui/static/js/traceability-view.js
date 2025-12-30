/**
 * Traceability View Module
 * Displays traceability indexes
 */

const TraceabilityView = {
    async load() {
        S1App.showLoading();
        
        try {
            const data = await S1App.apiCall('/traceability');
            this.renderTraceabilityList(data.traceability_indexes);
        } catch (error) {
            S1App.showError('Failed to load traceability indexes: ' + error.message);
        }
    },
    
    renderTraceabilityList(indexes) {
        if (!indexes || indexes.length === 0) {
            S1App.showContent('<p>No traceability indexes found.</p>');
            return;
        }
        
        const html = `
            <h2>Traceability Indexes</h2>
            <div class="traceability-list">
                ${indexes.map(index => `
                    <div class="traceability-item" onclick="TraceabilityView.showIndex('${index.id}')">
                        <h4>${index.id}</h4>
                        <p>Phase: ${index.phase || 'N/A'}</p>
                        <p>Claims: ${index.claim_count}</p>
                    </div>
                `).join('')}
            </div>
        `;
        
        S1App.showContent(html);
    },
    
    async showIndex(indexId) {
        S1App.showLoading();
        
        try {
            const data = await S1App.apiCall(`/traceability/${indexId}`);
            this.renderIndexDetails(data);
        } catch (error) {
            S1App.showError('Failed to load traceability index: ' + error.message);
        }
    },
    
    renderIndexDetails(index) {
        const html = `
            <div>
                <button onclick="TraceabilityView.load()" style="margin-bottom: 20px;">← Back to Traceability</button>
                <h2>${index.id}</h2>
                <p>Phase: ${index.phase || 'N/A'}</p>
                <p>Claims: ${index.claim_count}</p>
                
                <h3 style="margin-top: 30px;">Content</h3>
                <div class="markdown-content">${index.content}</div>
            </div>
        `;
        
        S1App.showContent(html);
    }
};

