# fintech-secure-pipeline-demo

# Fintech DevSecOps CI/CD Pipeline (GitHub Actions Demo)

## Overview
This hands-on project shows how to build a secure CI/CD pipeline for a fintech Python application using GitHub Actions. Every code change triggers security checks using Bandit (code SAST) and Trivy (container vulnerability scanning)—just like in a real fintech environment.

---

## 🚀 Quickstart (Terminal Commands)

```bash
# 1. Clone your repository
git clone https://github.com/YOUR_USERNAME/fintech-secure-pipeline-demo.git
cd fintech-secure-pipeline-demo

# 2. (If needed) Add the demo Python app
nano app.py
# (Paste code from below, save with Ctrl+O, Enter, then exit with Ctrl+X)

# 3. Add a Dockerfile for Trivy scanning
nano Dockerfile
# (Paste Dockerfile code from below)

# 4. Add GitHub Actions workflow
mkdir -p .github/workflows
nano .github/workflows/security.yml
# (Paste YAML from below)

# 5. Commit and push changes
git add .
git commit -m "Initial commit: fintech app with DevSecOps pipeline"
git push origin main

