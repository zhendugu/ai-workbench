// Interface F: Human Decision Points View - Read-Only Display
// FE_COGNITIVE_GUIDANCE_ADDENDUM compliance

// 自检规则：这个界面是否让人产生"系统在运行"的感觉？
// 答案：NO - 仅显示判断点事实，无动态更新

// 自检规则：是否让人感觉"点一下就能完成事情"？
// 答案：NO - 所有链接仅用于显示证据，无执行操作

// 自检规则：是否在任何地方暗示了推荐、执行或智能判断？
// 答案：NO - 仅显示判断点事实，无推荐、无执行、无智能判断

// T-3 验收标准：能够从判断结论回溯判断点、判断状态、证据来源，不出现推荐或默认选项

(function() {
    'use strict';

    // 加载判断点视图
    window.loadDecisionPointsView = function() {
        const decisionPointsList = document.getElementById('decision-points-list');
        if (!decisionPointsList) return;

        // 从 FE_FACT_HUMAN_DECISION_POINTS.md 和 FINAL_*_DECISION.md 读取数据
        // 这里使用示例数据，实际应从文件系统读取
        loadDecisionPointsData().then(decisionPoints => {
            renderDecisionPointsView(decisionPoints);
        }).catch(err => {
            console.error('Failed to load decision points:', err);
            decisionPointsList.innerHTML = '<p>无法加载判断点数据</p>';
        });
    };

    // 加载判断点数据
    async function loadDecisionPointsData() {
        // 实际实现中，这里应该从文件系统读取 FINAL_*_DECISION.md 文件
        // 示例：扫描 phase_*/FINAL_*_DECISION.md 文件
        return [
            {
                id: 'WO-Q4-1',
                title: 'Work Order Completion Decision',
                description: 'Work Order Q4-1 完成判断',
                status: '已判断',
                impact_scope: 'Phase Q, Epoch Mechanism',
                evidence_refs: [
                    { name: 'FINAL_Q4-1_DECISION.md', path: 'phase_q/Q4-1/FINAL_Q4-1_DECISION.md' },
                    { name: 'PASS_EVIDENCE_PACK_Q4-1', path: 'phase_q/Q4-1/PASS_EVIDENCE_PACK_Q4-1/' }
                ],
                decision_records: [
                    { timestamp: '2025-12-28', decision: 'PASS', human_signed: true }
                ]
            }
        ];
    }

    // 渲染判断点视图
    function renderDecisionPointsView(decisionPoints) {
        const decisionPointsList = document.getElementById('decision-points-list');
        if (!decisionPointsList) return;

        if (decisionPoints.length === 0) {
            decisionPointsList.innerHTML = '<p>暂无判断点</p>';
            return;
        }

        let html = '';

        decisionPoints.forEach(point => {
            html += '<div class="decision-point-item">';
            // 稳定标识符始终可见 (FE_COGNITIVE_GUIDANCE_ADDENDUM Section 6.3)
            html += `<h2>判断点 ID: ${escapeHtml(point.id)}</h2>`;
            html += `<h3>${escapeHtml(point.title)}</h3>`;

            // 判断点标题与描述
            html += '<div class="decision-point-item-section">';
            html += '<h3>判断点描述</h3>';
            html += `<p>${escapeHtml(point.description)}</p>`;
            html += '</div>';

            // 当前状态（文字：待判断/已判断）
            html += '<div class="decision-point-item-section">';
            html += '<h3>当前状态</h3>';
            html += `<p>${escapeHtml(point.status)}</p>`;
            html += '</div>';

            // 影响范围说明（纯文字）
            html += '<div class="decision-point-item-section">';
            html += '<h3>影响范围说明</h3>';
            html += `<p>${escapeHtml(point.impact_scope)}</p>`;
            html += '</div>';

            // 可参考证据列表（只读链接，类型化交叉链接 FE_COGNITIVE_GUIDANCE_ADDENDUM Section 6.4）
            html += '<div class="decision-point-item-section">';
            html += '<h3>可参考证据列表</h3>';
            if (point.evidence_refs && point.evidence_refs.length > 0) {
                html += '<ul>';
                point.evidence_refs.forEach(evidence => {
                    html += `<li><a href="#" class="evidence-link" data-evidence-path="${escapeHtml(evidence.path)}">[View Evidence] ${escapeHtml(evidence.name)}</a></li>`;
                });
                html += '</ul>';
            } else {
                html += '<p>无证据引用</p>';
            }
            html += '</div>';

            // 历史判断记录（只读列表）
            html += '<div class="decision-point-item-section">';
            html += '<h3>历史判断记录</h3>';
            html += '<p style="font-style: italic; margin-bottom: 1rem;">判断记录不可修改或删除。后续判断形成新记录。判断关系通过证据链体现。</p>';
            if (point.decision_records && point.decision_records.length > 0) {
                html += '<ul>';
                point.decision_records.forEach(record => {
                    html += '<li>';
                    html += `<p>时间: ${escapeHtml(record.timestamp)}</p>`;
                    html += `<p>判断: ${escapeHtml(record.decision)}</p>`;
                    html += `<p>人类签名: ${record.human_signed ? '是' : '否'}</p>`;
                    html += '</li>';
                });
                html += '</ul>';
            } else {
                html += '<p>无历史判断记录</p>';
            }
            html += '</div>';

            html += '</div>';
        });

        decisionPointsList.innerHTML = html;

        // 设置证据链接点击事件（显示证据回溯视图）
        const evidenceLinks = decisionPointsList.querySelectorAll('.evidence-link');
        evidenceLinks.forEach(link => {
            link.addEventListener('click', function(e) {
                e.preventDefault();
                const evidencePath = this.getAttribute('data-evidence-path');
                if (typeof showEvidenceView === 'function') {
                    showEvidenceView(evidencePath);
                }
            });
        });
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

