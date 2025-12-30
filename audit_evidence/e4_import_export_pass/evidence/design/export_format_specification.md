# Export Format Specification (Non-Constitutional Layer)

**Date**: 2025-12-27  
**Purpose**: Define export artifacts that contain ONLY factual data, no ranking, no usage stats, no recommendation signals

**Note**: This is application-level specification, NOT a CANONICAL document

---

## Export Format Principles

**Export artifacts contain ONLY factual data:**
- ✅ Pattern instances (conform to PATTERN_INSTANCE_SCHEMA)
- ✅ Registry entries (conform to PATTERN_REGISTRY_ONTOLOGY)
- ✅ Version lineage relationships (factual linkage only)
- ✅ Traceability information (factual records only)

**Export artifacts MUST NOT contain:**
- ❌ Ranking fields
- ❌ Usage statistics
- ❌ "recommended/standard/common" labels
- ❌ "latest preferred" indicators
- ❌ UI rendering hints that imply preference
- ❌ Auto-upgrade suggestions
- ❌ Default selection indicators

---

## Pattern Instance Export Format

**Format**: JSON (conforms to PATTERN_INSTANCE_SCHEMA.md)

**Required Fields**:
- pattern_id (required)
- pattern_name (required)
- pattern_version (required)
- created_at (required)
- created_by (required)

**Allowed Optional Fields**:
- description
- capability_references (reference only)
- evidence_references (reference only)
- metadata

**Forbidden Fields**:
- execution_order
- workflow_steps
- conditions
- success_criteria
- failure_criteria
- triggers
- automation_rules
- ranking
- usage_stats
- recommended_flag
- latest_preferred
- ui_hints

---

## Registry Entry Export Format

**Format**: JSON (conforms to PATTERN_REGISTRY_ONTOLOGY.md)

**Required Fields**:
- registry_entry_id
- pattern_instance_reference
- registered_at
- registered_by

**Allowed Optional Fields**:
- version_lineage_information (factual linkage only)
- traceability_information (factual records only)
- descriptive_markers_and_tags

**Forbidden Fields**:
- ranking
- usage_stats
- recommended_flag
- latest_preferred
- auto_upgrade_suggestion
- default_selection_indicator
- ui_rendering_hints

---

## Version Lineage Export Format

**Format**: JSON (factual linkage only)

**Allowed Fields**:
- parent_version_id (factual reference)
- child_version_ids (factual references)
- sibling_version_ids (factual references)
- relationship_type (factual descriptor: "inherits_from", "branches_from", "parallel_to")

**Forbidden Fields**:
- latest_version_indicator
- recommended_version
- auto_upgrade_path
- version_ranking
- version_preference

---

## Export Artifact Structure

**Pattern Instances Export**:
```json
{
  "export_metadata": {
    "exported_at": "2025-12-27T13:00:00Z",
    "exported_by": "human",
    "source_workspace": "WORKSPACE-A",
    "format_version": "1.0.0"
  },
  "pattern_instances": [
    {
      "pattern_id": "P-MD-CONV-001",
      "pattern_name": "Markdown Document Conversion Pattern",
      "pattern_version": "1.0.0",
      "created_at": "2025-12-27T10:05:00Z",
      "created_by": "human",
      "description": "A descriptive pattern for converting Markdown documents to HTML format",
      "capability_references": [
        {
          "capability_id": "C-MD-HTML-001",
          "reference_type": "descriptive_reference"
        }
      ]
    }
  ]
}
```

**Registry Entries Export**:
```json
{
  "export_metadata": {
    "exported_at": "2025-12-27T13:00:00Z",
    "exported_by": "human",
    "source_workspace": "WORKSPACE-A",
    "format_version": "1.0.0"
  },
  "registry_entries": [
    {
      "registry_entry_id": "REG-001",
      "pattern_instance_reference": {
        "pattern_id": "P-MD-CONV-001",
        "pattern_version": "1.0.0"
      },
      "registered_at": "2025-12-27T10:05:00Z",
      "registered_by": "human",
      "version_lineage_information": {
        "parent_version": null,
        "child_versions": []
      },
      "descriptive_markers": {
        "tags": ["markdown", "conversion"],
        "deprecated": false
      }
    }
  ]
}
```

---

## Constitutional Compliance

**Export format compliance**:
- ✅ Contains only factual data
- ✅ No ranking fields
- ✅ No usage statistics
- ✅ No recommendation signals
- ✅ No default selection indicators
- ✅ No UI rendering hints that imply preference
- ✅ Version lineage is factual linkage only
- ✅ Conforms to PATTERN_INSTANCE_SCHEMA.md
- ✅ Conforms to PATTERN_REGISTRY_ONTOLOGY.md

---

**END OF EXPORT FORMAT SPECIFICATION**

