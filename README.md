# DataGate

DataGate is an open-source governance layer for controlled access, editing, export, and auditing of internal databases.

## 🚀 Overview

DataGate provides a secure and controlled interface to interact with internal databases, replacing direct access tools like Adminer or raw SQL queries.

It introduces:

- Controlled data access
- Approval workflows for sensitive operations
- Audit logging
- Secure data export
- API-first architecture

## 🎯 Goal

The goal of DataGate is to:

- Eliminate uncontrolled database access
- Enable safe editing of sensitive data
- Provide full traceability of changes
- Introduce approval-based workflows
- Expose data safely to internal and external systems

## 🧠 Core Concepts

- **Governance Layer**: sits between users and databases
- **Permissions**: granular control over who can see or modify data
- **Approval Workflow**: sensitive changes require validation
- **Audit Log**: every action is tracked
- **API-first**: designed to integrate with other systems

## 🏗️ Architecture (initial)

```text
Frontend (future)
       |
   FastAPI Backend
       |
 Internal Databases
