# 💣 supply-chain-poison-pipeline

This repo simulates a real-world supply chain attack targeting a FinTech CI/CD pipeline.

## 🎯 Scenario

A malicious dependency was injected into the build process via a trusted third-party package.  
Static analysis and dependency scans were too shallow to detect it. The pipeline continued, exposing customer financial data.

This project reproduces that failure — and shows how to catch it with hardened scanning and pipeline defense.

## 🔐 What You'll Learn

- How to simulate a poisoned dependency attack
- How to detect malicious packages using Bandit and Trivy
- How to integrate security scanning into the Software Development Lifecycle (SDLC)
- How to break and then fix trust boundaries in a FinTech pipeline

