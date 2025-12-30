import { BrowserRouter, Routes, Route } from 'react-router-dom'
import { Layout } from './components/Layout'
import { DashboardPage } from './pages/DashboardPage'
import { CompanyViewPage } from './pages/CompanyViewPage'
import { CellsManagementPage } from './pages/CellsManagementPage'
import { CellDetailPage } from './pages/CellDetailPage'
import { RolesLibraryPage } from './pages/RolesLibraryPage'
import { TaskForcesPage } from './pages/TaskForcesPage'
import { ConnectionsPage } from './pages/ConnectionsPage'
import { MethodologiesPage } from './pages/MethodologiesPage'

function App() {
  return (
    <BrowserRouter>
      <Layout>
        <Routes>
          <Route path="/" element={<DashboardPage />} />
          <Route path="/company" element={<CompanyViewPage />} />
          <Route path="/cells" element={<CellsManagementPage />} />
          <Route path="/cells/:id" element={<CellDetailPage />} />
          <Route path="/roles" element={<RolesLibraryPage />} />
          <Route path="/task-forces" element={<TaskForcesPage />} />
          <Route path="/connections" element={<ConnectionsPage />} />
          <Route path="/methodologies" element={<MethodologiesPage />} />
        </Routes>
      </Layout>
    </BrowserRouter>
  )
}

export default App
