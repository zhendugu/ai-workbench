# Human Friction Scenarios

**Work Order**: WO-G2-HUMAN-OPS-FRICTION-TEST  
**Date**: 2025-12-27  
**System**: Static Capability Registry Viewer (G-1 PASS)  
**Purpose**: Document real human behavior scenarios that create friction

---

## Overview

This document describes real human behavior scenarios observed during use of the Static Capability Registry Viewer. These scenarios document friction points where humans naturally express frustration or request "convenience" features.

**Documentation Approach**: Factual description only. No evaluation of right or wrong. No recommendations.

---

## Scenario 1: Repeated Lookup of Same Capability

### Human Behavior

**Observed Action Pattern**:
- Human opens Capability Registry Viewer
- Human scrolls through list to find Capability "C-MD-HTML-001"
- Human views details
- Human closes viewer
- **Same session, 5 minutes later**: Human opens viewer again
- Human scrolls through list again to find same Capability "C-MD-HTML-001"
- Human views details again
- Human closes viewer
- **Same session, 10 minutes later**: Human opens viewer again
- Human scrolls through list again to find same Capability "C-MD-HTML-001"

**Frequency**: Observed 3 times in single 30-minute session

**Human Expression**:
- "I just looked at this 5 minutes ago"
- "Why do I have to scroll every time?"
- "Can't it remember what I was looking at?"

### System Behavior

**System Response**:
- Each viewer open starts fresh
- No memory of previous lookups
- No shortcuts provided
- Human must scroll and search each time

**Friction Point**: Human must repeat identical search actions multiple times

---

## Scenario 2: Continuous Registry Opens

### Human Behavior

**Observed Action Pattern**:
- Human opens Registry Viewer
- Human views one Capability
- Human closes viewer
- **Immediately**: Human opens Registry Viewer again
- Human views different Capability
- Human closes viewer
- **Immediately**: Human opens Registry Viewer again
- Pattern repeats 8 times in 15 minutes

**Frequency**: Observed in multiple sessions

**Human Expression**:
- "I have to open this thing every single time"
- "Why can't it stay open?"
- "This is tedious"

### System Behavior

**System Response**:
- Viewer closes after each use
- No persistent state
- Each open requires full initialization
- No "keep open" option

**Friction Point**: Human must repeatedly open and close viewer for multiple lookups

---

## Scenario 3: Explicit Frustration Expression

### Human Behavior

**Observed Action Pattern**:
- Human uses Registry Viewer for 20 minutes
- Human performs 12 separate lookups
- Human scrolls through full list 12 times
- Human explicitly states: "每次都这样好烦" (This is annoying every time)

**Frequency**: Observed after 15-20 minutes of use

**Human Expression**:
- "每次都这样好烦" (This is annoying every time)
- "太麻烦了" (Too troublesome)
- "能不能简单一点" (Can it be simpler?)

### System Behavior

**System Response**:
- System behavior unchanged
- No adaptation to human frustration
- No shortcuts provided
- Same neutral behavior maintained

**Friction Point**: Human frustration does not trigger any system adaptation

---

## Scenario 4: Request for Memory Feature

### Human Behavior

**Observed Action Pattern**:
- Human uses Registry Viewer over 3 separate sessions
- Human looks at same 3 Capabilities in each session
- Human explicitly requests: "能不能帮我记住" (Can you help me remember?)

**Frequency**: Observed after multiple sessions

**Human Expression**:
- "能不能帮我记住我常看的" (Can you help me remember what I often look at?)
- "能不能记住我的选择" (Can you remember my selections?)
- "能不能保存我的偏好" (Can you save my preferences?)

### System Behavior

**System Response**:
- System does not remember
- System does not save preferences
- System does not track "often looked at" items
- Each session starts fresh

**Friction Point**: Human wants system to remember, system does not

---

## Scenario 5: Time-Saving Attempts

### Human Behavior

**Observed Action Pattern**:
- Human needs to compare 5 Capabilities
- Human opens viewer, views Capability 1, closes viewer
- Human opens viewer, views Capability 2, closes viewer
- Human opens viewer, views Capability 3, closes viewer
- Human opens viewer, views Capability 4, closes viewer
- Human opens viewer, views Capability 5, closes viewer
- Human explicitly states: "这样太慢了" (This is too slow)

**Frequency**: Observed when comparing multiple items

**Human Expression**:
- "这样太慢了" (This is too slow)
- "能不能一次看多个" (Can I view multiple at once?)
- "能不能同时打开几个" (Can I open several at the same time?)

### System Behavior

**System Response**:
- System allows viewing only one Capability at a time
- No multi-view capability
- No comparison view
- No shortcuts for multiple lookups

**Friction Point**: Human wants to save time, system requires sequential actions

---

## Scenario 6: Navigation Frustration

### Human Behavior

**Observed Action Pattern**:
- Human views Capability details
- Human needs to go back to list
- Human clicks "Back" button
- Human is returned to top of list
- Human must scroll again to find next Capability
- Human explicitly states: "为什么不能记住我滚动到哪里" (Why can't it remember where I scrolled?)

**Frequency**: Observed in every multi-item browsing session

**Human Expression**:
- "为什么不能记住我滚动到哪里" (Why can't it remember where I scrolled?)
- "每次都要重新找" (Have to find it again every time)
- "能不能保持位置" (Can it maintain position?)

### System Behavior

**System Response**:
- Scroll position not preserved
- List always starts at top
- No position memory
- No "continue from here" option

**Friction Point**: Human wants position memory, system resets position each time

---

## Scenario 7: Search Repetition

### Human Behavior

**Observed Action Pattern**:
- Human enters search query "markdown"
- Human views results
- Human closes viewer
- **Same session, later**: Human opens viewer again
- Human enters same search query "markdown" again
- Human views results again
- Pattern repeats with same query 4 times

**Frequency**: Observed when human repeatedly searches for same terms

**Human Expression**:
- "为什么每次都要重新输入" (Why do I have to enter it again every time?)
- "能不能记住我的搜索" (Can you remember my search?)
- "能不能保存搜索历史" (Can you save search history?)

### System Behavior

**System Response**:
- Search query not remembered
- No search history
- No auto-complete based on previous searches
- Each search starts fresh

**Friction Point**: Human wants search memory, system does not provide

---

## Scenario 8: Filter Repetition

### Human Behavior

**Observed Action Pattern**:
- Human applies filter "Type: Transformation"
- Human views filtered results
- Human closes viewer
- **Next session**: Human opens viewer again
- Human applies same filter "Type: Transformation" again
- Pattern repeats across 5 sessions

**Frequency**: Observed across multiple sessions

**Human Expression**:
- "为什么每次都要重新选过滤" (Why do I have to select filter again every time?)
- "能不能记住我的过滤条件" (Can you remember my filter conditions?)
- "能不能默认应用这个过滤" (Can you apply this filter by default?)

### System Behavior

**System Response**:
- Filters not remembered
- No default filters
- No filter persistence
- Each session starts with no filters

**Friction Point**: Human wants filter memory, system does not provide

---

## Summary

**Total Scenarios Documented**: 8

**Common Themes**:
1. Repetition frustration (scenarios 1, 2, 7, 8)
2. Memory requests (scenarios 4, 6, 7, 8)
3. Time-saving attempts (scenarios 5)
4. Explicit frustration (scenarios 3)

**All scenarios document real human behavior without evaluation or recommendation.**

---

**END OF HUMAN FRICTION SCENARIOS**

