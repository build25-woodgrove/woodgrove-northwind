# Shift-Left Security Demo

Intentionally vulnerable application for demonstrating **Microsoft Defender for Cloud** shift-left security features.

> **WARNING**: This repository contains deliberate security vulnerabilities for demo purposes. DO NOT deploy to production.

## Scanner Coverage

| Scanner | Trigger Files | Findings |
|---------|--------------|----------|
| **Trivy** (CVEs) | `requirements.txt`, `package.json`, `Dockerfile` | Vulnerable dependencies + container base image |
| **Bandit** (Python) | `src/script.py` | Hardcoded creds, eval, shell injection, SQL injection, weak crypto |
| **ESLint** (JavaScript) | `src/app.js` | eval(), unused vars, loose equality, SQL concat |
| **Checkov / Terrascan** (Terraform) | `main.tf`, `terraform/` | Public S3, open SG, unencrypted RDS, public storage |
| **Template Analyzer** (Bicep/ARM) | `insecure.bicep` | No HTTPS, weak TLS, public blob access, no soft-delete |

## Pipelines

- **MSDO Scan** (`.github/workflows/msdo.yml`) - Runs all Defender CLI scanners and publishes results to MDC
- **Build & Push** (`.github/workflows/build-and-push.yml`) - Builds container image and pushes to ACR

## Setup

1. Connect this repo to Microsoft Defender for Cloud via GitHub connector
2. Configure `ACR_ENDPOINT` variable and `REGISTRY_USERNAME` / `REGISTRY_PASSWORD` secrets
3. Push to `main` to trigger both pipelines
4. View results in MDC → Defender for DevOps → Security tab
