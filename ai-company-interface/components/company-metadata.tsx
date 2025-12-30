"use client"

import { useState } from "react"
import { Card, CardContent, CardDescription, CardHeader, CardTitle } from "@/components/ui/card"
import { Input } from "@/components/ui/input"
import { Textarea } from "@/components/ui/textarea"
import { Label } from "@/components/ui/label"
import { Badge } from "@/components/ui/badge"
import { AlertCircle } from "lucide-react"

interface CompanyMetadataProps {
  isFrozen: boolean
}

export function CompanyMetadata({ isFrozen }: CompanyMetadataProps) {
  const [draftId] = useState(`draft-${Math.random().toString(36).substr(2, 9)}`)
  const [companyName, setCompanyName] = useState("")
  const [description, setDescription] = useState("")
  const [designStage, setDesignStage] = useState("Structure Definition")

  return (
    <div className="space-y-6">
      <div className="flex items-center justify-between">
        <div>
          <h2 className="text-2xl font-semibold tracking-tight">Company Metadata</h2>
          <p className="text-sm text-muted-foreground mt-1">
            Define the identity and purpose of this virtual company structure
          </p>
        </div>
        <Badge variant={isFrozen ? "secondary" : "outline"} className="font-mono">
          {isFrozen ? "FROZEN" : "DRAFT"}
        </Badge>
      </div>

      <Card>
        <CardHeader>
          <CardTitle className="text-lg font-mono">Design-Time Company Draft</CardTitle>
          <CardDescription>This is a structural declaration, not an executable entity</CardDescription>
        </CardHeader>
        <CardContent className="space-y-6">
          <div className="space-y-2">
            <Label htmlFor="draft-id" className="font-mono text-xs">
              Draft ID (Auto-generated)
            </Label>
            <Input id="draft-id" value={draftId} disabled className="font-mono text-sm bg-muted" />
            <p className="text-xs text-muted-foreground">Temporary identifier for this design session</p>
          </div>

          <div className="space-y-2">
            <Label htmlFor="company-name" className="font-mono text-xs">
              Company Name (Required)
            </Label>
            <Input
              id="company-name"
              value={companyName}
              onChange={(e) => setCompanyName(e.target.value)}
              disabled={isFrozen}
              placeholder="Enter a human-readable name..."
              className="font-mono"
            />
          </div>

          <div className="space-y-2">
            <Label htmlFor="description" className="font-mono text-xs">
              Human-Readable Description (Required)
            </Label>
            <Textarea
              id="description"
              value={description}
              onChange={(e) => setDescription(e.target.value)}
              disabled={isFrozen}
              placeholder="Describe what this company structure is designed to accomplish..."
              className="min-h-32 font-mono text-sm leading-relaxed"
            />
          </div>

          <div className="space-y-2">
            <Label htmlFor="design-stage" className="font-mono text-xs">
              Current Design Stage (Descriptive Only)
            </Label>
            <Input
              id="design-stage"
              value={designStage}
              onChange={(e) => setDesignStage(e.target.value)}
              disabled={isFrozen}
              className="font-mono"
            />
            <p className="text-xs text-muted-foreground">This is a label for human understanding, not a system state</p>
          </div>

          <div className="pt-4 border-t">
            <div className="flex items-start gap-2 text-sm text-muted-foreground">
              <AlertCircle className="h-4 w-4 mt-0.5 flex-shrink-0" />
              <div className="space-y-1 text-xs leading-relaxed">
                <p className="font-medium">Important Notes:</p>
                <ul className="list-disc list-inside space-y-1 ml-2">
                  <li>Company does NOT execute or run</li>
                  <li>Company does NOT have operational states</li>
                  <li>Company is a semantic anchor for structure grouping</li>
                  <li>Freezing converts this to a read-only reference for Run-Time use</li>
                </ul>
              </div>
            </div>
          </div>
        </CardContent>
      </Card>
    </div>
  )
}
