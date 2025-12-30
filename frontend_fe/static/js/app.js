// Frontend FE Main Application - Read-Only Cognitive Interface
// FE_COGNITIVE_GUIDANCE_ADDENDUM compliance

// 自检规则：这个界面是否让人产生"系统在运行"的感觉？
// 答案：NO - 仅显示静态事实，无动态更新

// 自检规则：是否让人感觉"点一下就能完成事情"？
// 答案：NO - 所有链接仅用于导航，无执行操作

// 自检规则：是否在任何地方暗示了推荐、执行或智能判断？
// 答案：NO - 仅显示事实，无推荐、无执行、无智能判断

(function() {
    'use strict';

    // 当前视图状态
    let currentView = null;
    let currentLayer = null;
    let currentCompanyId = 'ai-workbench-v1'; // 从 COMPANY_DECLARATION.md 读取

    // 层映射 (FE_COGNITIVE_GUIDANCE_ADDENDUM Section 4)
    const layerMap = {
        'company': 'L1: Company Context (Identity Layer)',
        'responsibility': 'L2: Structure Layer',
        'topology': 'L2: Structure Layer',
        'decision-points': 'L4: Judgment Layer',
        'evidence': 'L5: Evidence Layer'
    };

    // 初始化应用
    function init() {
        setupNavigation();
        setupCognitivePaths();
        updateLocationHeader('company', 'Company', 'Company Context');
        loadInitialView();
    }

    // 设置导航
    function setupNavigation() {
        const navLinks = document.querySelectorAll('.nav-link, .secondary-nav-link');
        navLinks.forEach(link => {
            link.addEventListener('click', function(e) {
                e.preventDefault();
                const viewName = this.getAttribute('data-view');
                if (viewName) {
                    switchView(viewName);
                }
            });
        });
    }

    // 切换视图
    function switchView(viewName) {
        // 隐藏所有视图
        const allViews = document.querySelectorAll('.view-container');
        allViews.forEach(view => {
            view.style.display = 'none';
        });

        // 显示目标视图
        const targetView = document.getElementById(`view-${viewName}`);
        if (targetView) {
            targetView.style.display = 'block';
            currentView = viewName;
            currentLayer = layerMap[viewName] || 'Unknown Layer';
            
            // 更新位置头部 (FE_COGNITIVE_GUIDANCE_ADDENDUM Section 6.1)
            updateLocationHeader(viewName, getEntityType(viewName), getLayerName(viewName));
            
            loadViewData(viewName);
        }
    }

    // 获取实体类型
    function getEntityType(viewName) {
        const typeMap = {
            'company': 'Company',
            'responsibility': 'Cell',
            'topology': 'Workflow',
            'decision-points': 'Judgment Point',
            'evidence': 'Evidence'
        };
        return typeMap[viewName] || 'View';
    }

    // 获取层名称
    function getLayerName(viewName) {
        return layerMap[viewName] || 'Unknown Layer';
    }

    // 更新位置头部 (FE_COGNITIVE_GUIDANCE_ADDENDUM Section 6.1)
    function updateLocationHeader(viewName, entityType, layerName) {
        const breadcrumb = document.getElementById('location-breadcrumb');
        const layerDecl = document.getElementById('layer-declaration');
        
        if (breadcrumb) {
            breadcrumb.textContent = `${currentCompanyId} > ${layerName} > ${entityType}`;
        }
        
        if (layerDecl) {
            layerDecl.textContent = `YOU ARE VIEWING: ${layerName} (READ-ONLY)`;
        }
    }

    // 设置认知路径 (FE_COGNITIVE_GUIDANCE_ADDENDUM Section 5)
    function setupCognitivePaths() {
        const pathLinks = document.querySelectorAll('.path-link');
        pathLinks.forEach(link => {
            link.addEventListener('click', function(e) {
                e.preventDefault();
                const pathType = this.getAttribute('data-path');
                navigateCognitivePath(pathType);
            });
        });
    }

    // 导航认知路径 (FE_COGNITIVE_GUIDANCE_ADDENDUM Section 5)
    function navigateCognitivePath(pathType) {
        switch(pathType) {
            case 'understand-company':
                // PATH A: Understand the Company
                switchView('company');
                break;
            case 'inspect-responsibility':
                // PATH B: Inspect a Responsibility
                switchView('responsibility');
                break;
            case 'verify-decision':
                // PATH C: Verify a Decision
                switchView('decision-points');
                break;
        }
    }

    // 加载初始视图
    function loadInitialView() {
        const hash = window.location.hash.replace('#', '');
        if (hash) {
            switchView(hash);
        } else {
            switchView('company');
        }
    }

    // 加载视图数据
    function loadViewData(viewName) {
        switch(viewName) {
            case 'company':
                if (typeof loadCompanyView === 'function') {
                    loadCompanyView();
                }
                break;
            case 'responsibility':
                if (typeof loadCellView === 'function') {
                    loadCellView();
                }
                break;
            case 'topology':
                if (typeof loadTopologyView === 'function') {
                    loadTopologyView();
                }
                break;
            case 'decision-points':
                if (typeof loadDecisionPointsView === 'function') {
                    loadDecisionPointsView();
                }
                break;
        }
    }

    // 启动应用
    if (document.readyState === 'loading') {
        document.addEventListener('DOMContentLoaded', init);
    } else {
        init();
    }
})();

