# Sprint 02 - Day 01

## Goal

Implement the Add Project feature for the Developer Portfolio Manager.

## User Story

As a developer,

I want to add new projects through the CLI,

so that I can store and manage my portfolio information in one place.

## Today's Feature

- Add Project

## Definition of Done

- User can enter:
  - Project Name
  - Description
  - Technology
  - GitHub Link
  - Status
- Project Name validation implemented.
- Technology validation implemented.
- Status validation implemented.
- Project data saved to `projects.json`.
- `projects.json` initializes with `[]` if empty.
- Multiple projects can be added without overwriting existing data.
- Success message displayed after saving.
- Application returns to the main menu after adding a project.
- Manual testing completed.
- Code committed using a feature branch.

## Status

Completed ✅

# Sprint 02 Day-02

## Goal

Implement the View Projects feature for the Developer Portfolio Manager.

## User Story

As a developer,

I want to view all my saved portfolio projects,

so that I can easily review and track my projects.

## Today's Feature

- View Projects

## Definition of Done

- Projects are loaded from `projects.json`.
- If `projects.json` does not exist, an empty list is returned.
- If `projects.json` is empty or contains no projects, an appropriate message is displayed.
- All saved projects are displayed in a readable format.
- Each project displays:
  - Project Name
  - Description
  - Technology
  - GitHub Link
  - Status
- User is returned to the main menu after viewing projects.
- Manual testing completed.
- Code committed using a feature branch.

## Status

Completed ✅

# Sprint 02 - Day 03

## Goal

Implement the Search Projects feature for the Developer Portfolio Manager.

## User Story

As a developer,

I want to search for a saved portfolio project by its name,

so that I can quickly locate a specific project without browsing the entire project list.

## Today's Feature

- Search Projects

## Definition of Done

- User can select the **Search Project** option from the main menu.
- User is prompted to enter a project name.
- Empty search input is validated and an appropriate message is displayed.
- Search is performed using the existing project data loaded from `projects.json`.
- Search is **case-insensitive**.
- Partial project names are supported (e.g., "Port" matches "Portfolio Manager").
- Matching project(s) are displayed in a clean and readable format.
- If no matching project exists, an appropriate message is displayed.
- Existing `load_projects()` functionality is reused instead of duplicating file-reading logic.
- Search logic is implemented in the **Service Layer**.
- CLI layer is responsible only for user interaction and displaying results.
- Manual testing completed for:
  - Exact match
  - Partial match
  - Case-insensitive search
  - Empty input
  - No matching project
- Code committed using a feature branch.

## Status

Completed ✅