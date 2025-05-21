# Auto-Healing Microservices Project

## Overview

This project demonstrates how to deploy simple Node.js microservices using Docker Compose on an AWS EC2 instance, monitor these services and the instance itself using Prometheus and Node Exporter, visualize metrics with Grafana, send alerts via Alertmanager to Slack, and automatically reboot the EC2 instance using an AWS Lambda function if it becomes unresponsive. This setup helps create a self-healing microservices environment.

---

## What is this project about?

- **Microservices:** Small, independently deployable applications (two simple HTTP servers).
- **Docker Compose:** Tool to easily run and manage multiple Docker containers together.
- **Prometheus:** Monitoring system that collects real-time metrics.
- **Node Exporter:** Collects hardware and OS metrics from the EC2 server.
- **Grafana:** Dashboard to visualize all collected metrics.
- **Alertmanager:** Sends alerts (e.g., service down) to communication tools like Slack.
- **AWS Lambda:** Runs a script to reboot the EC2 server automatically if it stops responding.
- **Auto-Healing:** System recovers itself without manual intervention.

---

## Who is this project for?

- Beginners wanting to learn Docker, monitoring with Prometheus & Grafana, alerting with Slack, and simple AWS automation.
- Anyone interested in setting up a resilient microservices environment on AWS.

---

## How is the project organized?

```text
auto-healing-microservices/
├── microservices/
│   └── docker-compose.yml          # Defines and runs two simple Node.js services
├── prometheus/
│   ├── prometheus.yml              # Prometheus configuration file
│   └── alert.rules.yml             # Prometheus alerting rules
├── alertmanager/
│   └── alertmanager.yml            # Config to send alerts to Slack
├── lambda/
│   └── auto_reboot_ec2.py          # AWS Lambda function to reboot EC2 instance
├── screenshots/                    # Add images of dashboards and alerts here
├── README.md                      # This file
└── .gitignore                     # Files to exclude from Git
