# Security-Aware E-Commerce Platform

A full-stack e-commerce platform with React, Flask, and MySQL. The app includes customer shopping flows, seller and admin dashboards, authentication, forensic logging, and a normalized relational schema.

## Documentation

- [Project Docs](docs/README.md)
- [API Documentation](docs/api-documentation.md)
- [Installation Guide](docs/installation-guide.md)
- [Deployment Guide](docs/deployment-guide.md)
- [Database Schema](docs/database-schema.md)
- [Use Case Diagram](docs/use-case-diagram.md)
- [Class Diagram](docs/class-diagram.md)
- [Sequence Diagram](docs/sequence-diagram.md)
- [Activity Diagram](docs/activity-diagram.md)

## Repository Layout

- [frontend](frontend) - React + Vite frontend with Tailwind CSS.
- [backend](backend) - Flask API with SQLAlchemy, JWT auth, commerce, and forensic modules.
- [database](database) - MySQL schema and database notes.
- [docs](docs) - Project documentation and diagrams.

## Stack

- React
- Vite
- Tailwind CSS
- Flask
- SQLAlchemy
- MySQL
- JWT authentication

## Highlights

- Responsive storefront pages for home, auth, catalog, cart, checkout, profile, orders, admin, and seller views.
- Secure backend modules for authentication, product management, commerce, and forensic visibility.
- Normalized schema with audit, login, security, transaction, fraud, and evidence tables.