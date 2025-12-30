// Interface A: Company Anchor View - Read-Only Display
// FE_COGNITIVE_GUIDANCE_ADDENDUM compliance

// 自检规则：这个界面是否让人产生"系统在运行"的感觉？
// 答案：NO - 仅显示 Company 声明性信息，无动态更新

// 自检规则：是否让人感觉"点一下就能完成事情"？
// 答案：NO - 所有链接仅用于显示文档引用，无执行操作

// 自检规则：是否在任何地方暗示了推荐、执行或智能判断？
// 答案：NO - 仅显示 Company 事实，无推荐、无执行、无智能判断

// T-1 验收标准：30秒内能回答 Q-30-1 到 Q-30-4
// T-4 验收标准：不产生"系统在运行"的错觉
// T-5 验收标准：不产生推荐错觉

(function() {
    'use strict';

    // 加载 Company 视图
    window.loadCompanyView = function() {
        const companyInfo = document.getElementById('company-info');
        if (!companyInfo) return;

        // 从 COMPANY_DECLARATION.md 读取数据（实际实现中需要后端 API 或直接读取文件）
        // 这里使用硬编码数据，实际应从声明文件读取
        const companyData = {
            company_id: 'ai-workbench-v1',
            company_name: 'AI Workbench',
            creation_timestamp: '2025-12-28T00:00:00Z',
            current_phase: 'Phase R (CLOSED)',
            frozen_design_refs: [
                { name: 'AI Virtual Company Organizational GCD', path: 'docs/GCD.md' },
                { name: 'Epoch-based Time-Fractured Intelligence System', path: 'phase_q/PARADIGM_FREEZE_DECLARATION.md' },
                { name: 'Q4-2 Validity Boundaries', path: 'phase_q/LIMITS_OF_VALIDITY.md' },
                { name: 'Design Compliance Audit', path: 'DESIGN_COMPLIANCE_AUDIT.md' },
                { name: 'Engine v1 Freeze Declaration', path: 'docs/ENGINE_V1_FREEZE.md' },
                { name: 'Execution Contract', path: 'docs/EXECUTION_CONTRACT.md' },
                { name: 'Workflow Rules', path: 'docs/WORKFLOW_RULES.md' }
            ],
            description: `AI Workbench is a governance framework and execution system for AI-driven virtual company structures.

The system implements:
- Role-based organizational structure (GCD_v2)
- Cell composition and Task Force coordination
- Epoch-based time-fractured intelligence paradigm (Phase Q, FROZEN)
- Constitutional compliance and audit mechanisms
- Read-only operator interface (Phase S)

Current state:
- Phase R: CLOSED (Red Team validation complete)
- Active Stage: 6-A (Implementation not authorized)
- Active Blueprint: ai-virtual-company-org

The system is read-only at the frontend layer. All execution requires human authorization.`
        };

        renderCompanyView(companyData);
    };

    // 渲染 Company 视图
    function renderCompanyView(data) {
        const companyInfo = document.getElementById('company-info');
        if (!companyInfo) return;

        let html = '';

        // Company 标识与说明
        html += '<div class="company-info-section">';
        html += '<h2>Company 标识</h2>';
        html += `<p><strong>Company ID:</strong> ${escapeHtml(data.company_id)}</p>`;
        html += `<p><strong>Company Name:</strong> ${escapeHtml(data.company_name)}</p>`;
        html += `<p><strong>创建时间:</strong> ${escapeHtml(data.creation_timestamp)}</p>`;
        html += '</div>';

        // 当前阶段标签
        html += '<div class="company-info-section">';
        html += '<h2>当前阶段</h2>';
        html += `<p>${escapeHtml(data.current_phase)}</p>`;
        html += '</div>';

        // 人类可读说明
        html += '<div class="company-info-section">';
        html += '<h2>说明</h2>';
        html += `<div>${formatDescription(data.description)}</div>`;
        html += '</div>';

        // 冻结设计文档引用列表
        html += '<div class="company-info-section">';
        html += '<h2>冻结设计文档引用</h2>';
        html += '<ul>';
        data.frozen_design_refs.forEach(ref => {
            html += `<li><a href="#" data-doc-path="${escapeHtml(ref.path)}" class="doc-link">${escapeHtml(ref.name)}</a></li>`;
        });
        html += '</ul>';
        html += '</div>';

        // 明确表达的事实
        html += '<div class="company-info-section">';
        html += '<h2>明确表达的事实</h2>';
        html += '<ul>';
        html += '<li>Company 不拥有执行权</li>';
        html += '<li>Company 不是正在运行的实体</li>';
        html += '<li>Company 仅用于结构性指代</li>';
        html += '</ul>';
        html += '</div>';

        companyInfo.innerHTML = html;

        // 设置文档链接点击事件（仅显示，不执行）
        const docLinks = companyInfo.querySelectorAll('.doc-link');
        docLinks.forEach(link => {
            link.addEventListener('click', function(e) {
                e.preventDefault();
                const docPath = this.getAttribute('data-doc-path');
                // 仅显示文档路径，不执行任何操作
                alert(`文档路径: ${docPath}\n\n这是只读引用，不执行任何操作。`);
            });
        });
    }

    // 格式化描述文本
    function formatDescription(text) {
        return escapeHtml(text).split('\n').map(line => {
            if (line.trim() === '') return '<br>';
            if (line.trim().startsWith('-')) {
                return `<p style="margin-left: 1rem;">${escapeHtml(line)}</p>`;
            }
            return `<p>${escapeHtml(line)}</p>`;
        }).join('');
    }

    // HTML 转义
    function escapeHtml(text) {
        const div = document.createElement('div');
        div.textContent = text;
        return div.innerHTML;
    }
})();

