"use client"

import { Card, CardContent, CardDescription, CardHeader, CardTitle } from "@/components/ui/card"
import { Button } from "@/components/ui/button"
import { Badge } from "@/components/ui/badge"
import { Tabs, TabsContent, TabsList, TabsTrigger } from "@/components/ui/tabs"
import { AlertCircle, FileText, Box, Layers } from "lucide-react"

interface TemplateLibraryProps {
  isFrozen: boolean
}

const cellTemplates = [
  {
    id: "research-cell",
    name: "Research Cell",
    source: "built-in",
    frozen: true,
    description: "Responsibility for information gathering and analysis",
  },
  {
    id: "validation-cell",
    name: "Validation Cell",
    source: "built-in",
    frozen: true,
    description: "Responsibility for verification and quality assurance",
  },
]

const workflowTemplates = [
  {
    id: "linear-workflow",
    name: "Linear Workflow",
    source: "built-in",
    frozen: true,
    description: "Sequential cell arrangement with dependency chain",
  },
  {
    id: "parallel-workflow",
    name: "Parallel Workflow",
    source: "built-in",
    frozen: true,
    description: "Multiple cells operating with shared dependencies",
  },
]

const companyTemplates = [
  {
    id: "consulting-company",
    name: "Consulting Company",
    source: "built-in",
    frozen: true,
    description: "Complete structure for advisory and recommendation services",
  },
  {
    id: "research-company",
    name: "Research Company",
    source: "built-in",
    frozen: true,
    description: "Complete structure for investigation and analysis tasks",
  },
]

export function TemplateLibrary({ isFrozen }: TemplateLibraryProps) {
  return (
    <div className="space-y-6">
      <div className="flex items-center justify-between">
        <div>
          <h2 className="text-2xl font-semibold tracking-tight">Template Library</h2>
          <p className="text-sm text-muted-foreground mt-1">Reusable structural patterns for faster design iteration</p>
        </div>
      </div>

      <Card className="border-dashed">
        <CardContent className="pt-6">
          <div className="flex items-start gap-2 text-sm text-muted-foreground">
            <AlertCircle className="h-4 w-4 mt-0.5 flex-shrink-0" />
            <div className="space-y-1 text-xs leading-relaxed">
              <p className="font-medium">Template Usage Rules:</p>
              <ul className="list-disc list-inside space-y-1 ml-2">
                <li>Templates are structural starting points, not auto-generated solutions</li>
                <li>Using a template requires explicit human confirmation</li>
                <li>Templates can be edited after application (if not frozen)</li>
                <li>Templates do NOT include execution logic or judgment points</li>
              </ul>
            </div>
          </div>
        </CardContent>
      </Card>

      <Tabs defaultValue="cells" className="space-y-4">
        <TabsList className="grid w-full grid-cols-3 font-mono">
          <TabsTrigger value="cells" className="gap-2">
            <Box className="h-4 w-4" />
            Cell Templates
          </TabsTrigger>
          <TabsTrigger value="workflows" className="gap-2">
            <Layers className="h-4 w-4" />
            Workflow Templates
          </TabsTrigger>
          <TabsTrigger value="companies" className="gap-2">
            <FileText className="h-4 w-4" />
            Company Templates
          </TabsTrigger>
        </TabsList>

        <TabsContent value="cells" className="space-y-4">
          {cellTemplates.map((template) => (
            <Card key={template.id}>
              <CardHeader>
                <div className="flex items-start justify-between">
                  <div className="flex-1">
                    <div className="flex items-center gap-2 mb-2">
                      <CardTitle className="text-base font-mono">{template.name}</CardTitle>
                      <Badge variant="outline" className="text-xs font-mono">
                        {template.source}
                      </Badge>
                      {template.frozen && (
                        <Badge variant="secondary" className="text-xs">
                          frozen
                        </Badge>
                      )}
                    </div>
                    <CardDescription className="text-sm leading-relaxed">{template.description}</CardDescription>
                  </div>
                  <Button variant="outline" size="sm" disabled={isFrozen}>
                    Use Template
                  </Button>
                </div>
              </CardHeader>
            </Card>
          ))}
        </TabsContent>

        <TabsContent value="workflows" className="space-y-4">
          {workflowTemplates.map((template) => (
            <Card key={template.id}>
              <CardHeader>
                <div className="flex items-start justify-between">
                  <div className="flex-1">
                    <div className="flex items-center gap-2 mb-2">
                      <CardTitle className="text-base font-mono">{template.name}</CardTitle>
                      <Badge variant="outline" className="text-xs font-mono">
                        {template.source}
                      </Badge>
                      {template.frozen && (
                        <Badge variant="secondary" className="text-xs">
                          frozen
                        </Badge>
                      )}
                    </div>
                    <CardDescription className="text-sm leading-relaxed">{template.description}</CardDescription>
                  </div>
                  <Button variant="outline" size="sm" disabled={isFrozen}>
                    Use Template
                  </Button>
                </div>
              </CardHeader>
            </Card>
          ))}
        </TabsContent>

        <TabsContent value="companies" className="space-y-4">
          {companyTemplates.map((template) => (
            <Card key={template.id}>
              <CardHeader>
                <div className="flex items-start justify-between">
                  <div className="flex-1">
                    <div className="flex items-center gap-2 mb-2">
                      <CardTitle className="text-base font-mono">{template.name}</CardTitle>
                      <Badge variant="outline" className="text-xs font-mono">
                        {template.source}
                      </Badge>
                      {template.frozen && (
                        <Badge variant="secondary" className="text-xs">
                          frozen
                        </Badge>
                      )}
                    </div>
                    <CardDescription className="text-sm leading-relaxed">{template.description}</CardDescription>
                  </div>
                  <Button variant="outline" size="sm" disabled={isFrozen}>
                    Use Template
                  </Button>
                </div>
              </CardHeader>
            </Card>
          ))}
        </TabsContent>
      </Tabs>
    </div>
  )
}
