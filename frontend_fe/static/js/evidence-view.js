// Interface G: Evidence Backtracking View - Embedded, Read-Only Display

// 自检规则：这个界面是否让人产生"系统在运行"的感觉？
// 答案：NO - 仅显示证据事实，无动态更新

// 自检规则：是否让人感觉"点一下就能完成事情"？
// 答案：NO - 仅显示证据内容，无执行操作

// 自检规则：是否在任何地方暗示了推荐、执行或智能判断？
// 答案：NO - 仅显示证据事实，无推荐、无执行、无智能判断

(function() {
    'use strict';

    // 显示证据回溯视图
    window.showEvidenceView = function(evidencePath) {
        const evidenceModal = document.getElementById('evidence-modal');
        const evidenceContent = document.getElementById('evidence-content');
        if (!evidenceModal || !evidenceContent) return;

        // 加载证据数据（实际实现中需要从文件系统读取）
        loadEvidenceData(evidencePath).then(evidence => {
            renderEvidenceView(evidence);
            evidenceModal.style.display = 'block';
        }).catch(err => {
            console.error('Failed to load evidence:', err);
            evidenceContent.innerHTML = '<p>无法加载证据数据</p>';
            evidenceModal.style.display = 'block';
        });
    };

    // 加载证据数据
    async function loadEvidenceData(evidencePath) {
        // 实际实现中，这里应该从文件系统读取证据文件
        // 示例：读取 evidencePath 目录下的文件
        return {
            evidence_type: 'Evidence Pack',
            timestamp: '2025-12-28T00:00:00Z',
            creator: 'Human',
            summary: 'Evidence pack for Work Order Q4-1',
            files: [
                { name: 'execution_log_001.txt', path: `${evidencePath}/execution_log_001.txt` },
                { name: 'metrics.json', path: `${evidencePath}/metrics.json` }
            ]
        };
    }

    // 渲染证据视图
    function renderEvidenceView(evidence) {
        const evidenceContent = document.getElementById('evidence-content');
        if (!evidenceContent) return;

        let html = '';

        html += '<div class="evidence-content-section">';
        html += '<h3>证据类型</h3>';
        html += `<p>${escapeHtml(evidence.evidence_type)}</p>`;
        html += '</div>';

        html += '<div class="evidence-content-section">';
        html += '<h3>时间戳</h3>';
        html += `<p>${escapeHtml(evidence.timestamp)}</p>`;
        html += '</div>';

        html += '<div class="evidence-content-section">';
        html += '<h3>创建者标识</h3>';
        html += `<p>${escapeHtml(evidence.creator)}</p>`;
        html += '</div>';

        html += '<div class="evidence-content-section">';
        html += '<h3>内容摘要</h3>';
        html += `<p>${escapeHtml(evidence.summary)}</p>`;
        html += '</div>';

        if (evidence.files && evidence.files.length > 0) {
            html += '<div class="evidence-content-section">';
            html += '<h3>证据文件</h3>';
            html += '<ul>';
            evidence.files.forEach(file => {
                html += `<li>${escapeHtml(file.name)}</li>`;
            });
            html += '</ul>';
            html += '</div>';
        }

        // 明确表达的事实
        html += '<div class="evidence-content-section">';
        html += '<h3>明确表达的事实</h3>';
        html += '<p>审计不是操作对象，是回溯能力</p>';
        html += '</div>';

        evidenceContent.innerHTML = html;
    }

    // 关闭证据模态框
    function closeEvidenceModal() {
        const evidenceModal = document.getElementById('evidence-modal');
        if (evidenceModal) {
            evidenceModal.style.display = 'none';
        }
    }

    // 设置关闭按钮事件
    if (document.readyState === 'loading') {
        document.addEventListener('DOMContentLoaded', function() {
            const closeBtn = document.querySelector('.evidence-modal-close');
            if (closeBtn) {
                closeBtn.addEventListener('click', closeEvidenceModal);
            }
            // 点击模态框外部关闭
            const evidenceModal = document.getElementById('evidence-modal');
            if (evidenceModal) {
                evidenceModal.addEventListener('click', function(e) {
                    if (e.target === evidenceModal) {
                        closeEvidenceModal();
                    }
                });
            }
        });
    } else {
        const closeBtn = document.querySelector('.evidence-modal-close');
        if (closeBtn) {
            closeBtn.addEventListener('click', closeEvidenceModal);
        }
        const evidenceModal = document.getElementById('evidence-modal');
        if (evidenceModal) {
            evidenceModal.addEventListener('click', function(e) {
                if (e.target === evidenceModal) {
                    closeEvidenceModal();
                }
            });
        }
    }

    // HTML 转义
    function escapeHtml(text) {
        if (typeof text !== 'string') {
            text = String(text);
        }
        const div = document.createElement('div');
        div.textContent = text;
        return div.innerHTML;
    }
})();

