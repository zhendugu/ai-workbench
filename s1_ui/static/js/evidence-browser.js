/**
 * Evidence Browser Module
 * Navigates evidence packs and displays files
 */

const EvidenceBrowser = {
    async load() {
        S1App.showLoading();
        
        try {
            const data = await S1App.apiCall('/evidence');
            this.renderEvidencePackList(data.evidence_packs);
        } catch (error) {
            S1App.showError('Failed to load evidence packs: ' + error.message);
        }
    },
    
    renderEvidencePackList(packs) {
        if (!packs || packs.length === 0) {
            S1App.showContent('<p>No evidence packs found.</p>');
            return;
        }
        
        const html = `
            <h2>Evidence Packs</h2>
            <div class="evidence-pack-list">
                ${packs.map(pack => `
                    <div class="evidence-pack-card ${pack.type}" onclick="EvidenceBrowser.showPack('${pack.id}')">
                        <h4>${pack.id}</h4>
                        <p>Type: ${pack.type}</p>
                        <p>Phase: ${pack.phase || 'N/A'}</p>
                        <p>Files: ${pack.file_count}</p>
                    </div>
                `).join('')}
            </div>
        `;
        
        S1App.showContent(html);
    },
    
    async showPack(packId) {
        S1App.showLoading();
        
        try {
            const data = await S1App.apiCall(`/evidence/${packId}`);
            this.renderPackDetails(data);
        } catch (error) {
            S1App.showError('Failed to load evidence pack: ' + error.message);
        }
    },
    
    renderPackDetails(pack) {
        const fileTree = pack.files.slice(0, 50).map(file => `
            <div class="file-tree-item" onclick="EvidenceBrowser.showFile('${pack.id}', '${file}')">
                ${file}
            </div>
        `).join('');
        
        const moreFiles = pack.files.length > 50 ? `<p>... and ${pack.files.length - 50} more files</p>` : '';
        
        const html = `
            <div>
                <button onclick="EvidenceBrowser.load()" style="margin-bottom: 20px;">← Back to Evidence Packs</button>
                <h2>${pack.id}</h2>
                <p>Type: ${pack.type}</p>
                <p>Phase: ${pack.phase || 'N/A'}</p>
                <p>Directory: ${pack.directory_path}</p>
                
                <h3 style="margin-top: 30px;">Files (${pack.files.length})</h3>
                <div class="file-tree">
                    ${fileTree}
                    ${moreFiles}
                </div>
            </div>
        `;
        
        S1App.showContent(html);
    },
    
    async showFile(packId, filePath) {
        S1App.showLoading();
        
        try {
            const encodedPath = encodeURIComponent(filePath);
            const data = await S1App.apiCall(`/evidence/${packId}/file/${encodedPath}`);
            this.renderFileContent(packId, filePath, data);
        } catch (error) {
            S1App.showError('Failed to load file: ' + error.message);
        }
    },
    
    renderFileContent(packId, filePath, fileData) {
        const contentHtml = fileData.type === 'markdown' ? 
            `<div class="markdown-content">${fileData.content}</div>` :
            `<pre>${JSON.stringify(fileData.content, null, 2)}</pre>`;
        
        const html = `
            <div>
                <button onclick="EvidenceBrowser.showPack('${packId}')" style="margin-bottom: 20px;">← Back to Pack</button>
                <h2>${filePath}</h2>
                <p>Type: ${fileData.type}</p>
                ${contentHtml}
            </div>
        `;
        
        S1App.showContent(html);
    }
};

