# UI Core Pages Implementation

This document describes the UI prototype implementation based on `UI_DESIGN_DRAFT_001.md`.

## Overview

This implementation provides a complete UI prototype with 8 core pages, mock data, and bilingual (Chinese/English) support. It uses React Router for navigation and mock data for demonstration purposes.

## Structure

```
src/
├── pages/              # 8 core page components
│   ├── DashboardPage.tsx
│   ├── CompanyViewPage.tsx
│   ├── CellsManagementPage.tsx
│   ├── CellDetailPage.tsx
│   ├── RolesLibraryPage.tsx
│   ├── TaskForcesPage.tsx
│   ├── ConnectionsPage.tsx
│   └── MethodologiesPage.tsx
├── components/         # Shared components
│   └── Layout.tsx     # Main layout with sidebar and header
├── mock/              # Mock data
│   └── data.ts        # All mock data definitions
├── i18n/              # Internationalization
│   ├── config.ts
│   └── locales/
│       ├── en/
│       │   └── common.json
│       └── zh/
│           └── common.json
└── App.tsx            # Main app with routing
```

## Pages

### 1. Dashboard (`/`)
- Organization overview
- Quick statistics
- Navigation shortcuts

### 2. Company View (`/company`)
- Company information display
- Organization structure placeholder
- Related content statistics

### 3. Cells Management (`/cells`)
- List of all cells
- Search and filter functionality
- Create/View/Edit/Delete actions (UI only)

### 4. Cell Detail (`/cells/:id`)
- Cell detailed information
- Members list
- Roles list
- Connections list

### 5. Roles Library (`/roles`)
- List of all roles
- Role cards with details
- Search and filter functionality

### 6. Task Forces (`/task-forces`)
- List of all task forces
- Status indicators
- Search and filter functionality

### 7. Connections (`/connections`)
- List view of connections
- Graph view placeholder
- Connection type indicators

### 8. Methodologies (`/methodologies`)
- List of methodologies
- Category indicators
- Application statistics

## Features

### Internationalization
- Full bilingual support (Chinese/English)
- Language switcher in header
- All UI text is translatable
- Language preference saved in localStorage

### Navigation
- Sidebar navigation with icons
- Active route highlighting
- Breadcrumb navigation on detail pages
- Direct links between related entities

### Mock Data
All mock data is defined in `src/mock/data.ts`:
- Company information
- Cells (departments/groups)
- Roles (job definitions)
- Task Forces (project teams)
- Connections (relationships)
- Methodologies (work methods)

## Installation & Setup

1. Install dependencies:
```bash
npm install
```

Required dependencies (already in package.json):
- `react-router-dom` - For routing
- `lucide-react` - For icons
- `react-i18next` & `i18next` - For internationalization

2. Start development server:
```bash
npm run dev
```

3. Open browser:
Navigate to `http://localhost:5173` (or the port Vite assigns)

## Usage

### Language Switching
Click the language buttons in the top-right header to switch between English and Chinese.

### Navigation
- Use the left sidebar to navigate between main sections
- Click on items in lists to view details
- Use the back button or sidebar to return to previous pages

### Search & Filter
Most list pages include:
- Search box for filtering by name
- Filter dropdowns (UI ready, functionality not implemented)

## Implementation Notes

### Design Compliance
- All pages follow the layout and structure defined in `UI_DESIGN_DRAFT_001.md`
- Field names and labels match the design document
- UI components use Tailwind CSS for styling
- Icons from Lucide React library

### Limitations (By Design)
- **No Backend Integration**: All data is mock data only
- **No Data Persistence**: Changes are not saved
- **No CRUD Operations**: Create/Edit/Delete buttons are UI only
- **No Authentication**: No user login/permission system
- **Placeholder Views**: Some views (like graph visualization) are placeholders

### Future Enhancements
When ready to integrate with backend:
1. Replace mock data imports with API calls
2. Implement actual CRUD operations
3. Add form validation
4. Add error handling
5. Implement graph visualization library
6. Add user authentication

## Code Style

- TypeScript for type safety
- Functional components with hooks
- Tailwind CSS for styling
- Component-based architecture
- Translation keys follow i18n conventions

## Testing

To verify implementation:
1. Navigate through all 8 pages
2. Test language switching on each page
3. Verify all mock data displays correctly
4. Check that navigation links work
5. Ensure responsive design works on different screen sizes

## Troubleshooting

### Routing Issues
- Ensure `react-router-dom` is installed
- Check that `BrowserRouter` wraps the app

### Translation Issues
- Check that i18n config is imported in `main.tsx`
- Verify translation keys exist in JSON files
- Clear localStorage if language switching breaks

### Styling Issues
- Ensure Tailwind CSS is configured correctly
- Check `tailwind.config.js` and `postcss.config.js`
- Verify CSS imports in `index.css`

