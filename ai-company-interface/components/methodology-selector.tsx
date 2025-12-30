"use client"

import { useState } from "react"
import { Card, CardContent, CardDescription, CardHeader, CardTitle } from "@/components/ui/card"
import { Label } from "@/components/ui/label"
import { RadioGroup, RadioGroupItem } from "@/components/ui/radio-group"
import { Textarea } from "@/components/ui/textarea"
import { Badge } from "@/components/ui/badge"
import { AlertCircle } from "lucide-react"

interface MethodologySelectorProps {
  isFrozen: boolean
}

const builtInMethodologies = [
  {
    id: "none",
    name: "None",
    description: "No specific methodology perspective applied",
    status: "available",
  },
  {
    id: "waterfall",
    name: "Waterfall-Inspired View",
    description: "Sequential phase organization for understanding",
    status: "available",
  },
  {
    id: "agile",
    name: "Agile-Inspired View",
    description: "Iterative sprint-based conceptual grouping",
    status: "available",
  },
  {
    id: "hybrid",
    name: "Hybrid Approach",
    description: "Combined perspectives for complex structures",
    status: "available",
  },
]

export function MethodologySelector({ isFrozen }: MethodologySelectorProps) {
  const [selectedMethodology, setSelectedMethodology] = useState("none")
  const [customMethodology, setCustomMethodology] = useState("")

  return (
    <div className="space-y-6">
      <div className="flex items-center justify-between">
        <div>
          <h2 className="text-2xl font-semibold tracking-tight">Methodology Perspective</h2>
          <p className="text-sm text-muted-foreground mt-1">
            Choose a cognitive lens for organizing and viewing structure
          </p>
        </div>
        <Badge variant="outline" className="font-mono text-xs">
          PERSPECTIVE ONLY
        </Badge>
      </div>

      <Card className="border-dashed">
        <CardContent className="pt-6">
          <div className="flex items-start gap-2 text-sm text-muted-foreground">
            <AlertCircle className="h-4 w-4 mt-0.5 flex-shrink-0" />
            <div className="space-y-1 text-xs leading-relaxed">
              <p className="font-medium">Methodology as Perspective:</p>
              <ul className="list-disc list-inside space-y-1 ml-2">
                <li>Methodology is a VIEW, not a system mode</li>
                <li>Changing perspective does NOT change data or structure</li>
                <li>No methodology is recommended or evaluated</li>
                <li>Methodology does NOT drive operations or constraints</li>
                <li>This affects how YOU think, not how the system behaves</li>
              </ul>
            </div>
          </div>
        </CardContent>
      </Card>

      <Card>
        <CardHeader>
          <CardTitle className="text-lg font-mono">Built-In Methodologies</CardTitle>
          <CardDescription>Select a pre-defined perspective for structural organization</CardDescription>
        </CardHeader>
        <CardContent>
          <RadioGroup
            value={selectedMethodology}
            onValueChange={setSelectedMethodology}
            disabled={isFrozen}
            className="space-y-4"
          >
            {builtInMethodologies.map((methodology) => (
              <div key={methodology.id} className="flex items-start space-x-3 space-y-0">
                <RadioGroupItem value={methodology.id} id={methodology.id} />
                <Label htmlFor={methodology.id} className="font-normal cursor-pointer flex-1">
                  <div className="space-y-1">
                    <div className="flex items-center gap-2">
                      <span className="font-mono text-sm">{methodology.name}</span>
                      <Badge variant="secondary" className="text-xs">
                        {methodology.status}
                      </Badge>
                    </div>
                    <p className="text-xs text-muted-foreground leading-relaxed">{methodology.description}</p>
                  </div>
                </Label>
              </div>
            ))}
          </RadioGroup>
        </CardContent>
      </Card>

      <Card>
        <CardHeader>
          <CardTitle className="text-lg font-mono">Custom Methodology</CardTitle>
          <CardDescription>Define your own perspective declaration (local draft only)</CardDescription>
        </CardHeader>
        <CardContent className="space-y-4">
          <div className="space-y-2">
            <Label htmlFor="custom-methodology" className="font-mono text-xs">
              Methodology Description (Optional)
            </Label>
            <Textarea
              id="custom-methodology"
              value={customMethodology}
              onChange={(e) => setCustomMethodology(e.target.value)}
              disabled={isFrozen}
              placeholder="Describe your custom organizational perspective..."
              className="min-h-32 font-mono text-sm"
            />
          </div>
          <p className="text-xs text-muted-foreground">Custom methodologies are saved as draft-only and not shared</p>
        </CardContent>
      </Card>
    </div>
  )
}
