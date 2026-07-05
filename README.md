# CSPM Agent

[![CI](https://github.com/kogunlowo123/cspm-agent/actions/workflows/ci.yml/badge.svg)](https://github.com/kogunlowo123/cspm-agent/actions/workflows/ci.yml)
[![Python 3.11+](https://img.shields.io/badge/python-3.11+-blue.svg)](https://www.python.org/downloads/)
[![License: MIT](https://img.shields.io/badge/License-MIT-green.svg)](https://opensource.org/licenses/MIT)

> **Category**: Security AI | **Cloud**: MULTI-CLOUD | **LLM**: gpt-4o

Cloud Security Posture Management agent that continuously monitors cloud infrastructure against CIS benchmarks, detects configuration drift, prioritizes findings by risk, and generates remediation scripts.

---

## Domain-Specific Tools

| Tool | Description |
|------|-------------|
| `analyze` | Primary analysis function for CSPM Agent |
| `scan` | Scan target for issues relevant to CSPM Agent |
| `report` | Generate report for CSPM Agent |
| `remediate` | Execute remediation action |
| `monitor` | Monitor for ongoing issues |

## API Endpoints

| Method | Path | Description |
|--------|------|-------------|
| `POST` | `/api/v1/cspm/analyze` | Run analysis |
| `POST` | `/api/v1/cspm/scan` | Scan target |
| `POST` | `/api/v1/cspm/report` | Generate report |
| `POST` | `/api/v1/cspm/remediate` | Execute remediation |
| `GET` | `/api/v1/cspm/status` | Get status |

## Features

- Cspm
- Reporting
- Monitoring

## Integrations

- Siem Connector
- Edr Connector
- Threat Intel
- Ticketing System

## Architecture

```
cspm-agent/
├── src/
│   ├── agent/              # Domain-specific agent logic
│   │   ├── cspm_agent_agent.py  # Main agent with domain tools
│   │   ├── tools.py        # 5 domain-specific tools
│   │   └── prompts.py      # Expert system prompts
│   ├── api/                # FastAPI routes
│   │   └── routes/
│   │       ├── domain.py   # 5 domain-specific endpoints
│   │       └── health.py   # Health check
│   ├── connectors/         # 4 integration connectors
│   ├── config/             # Settings and configuration
│   ├── models/             # Domain-specific Pydantic schemas
│   ├── rag/                # RAG pipeline
│   ├── mcp/                # MCP server
│   └── a2a/                # Agent-to-agent protocol
├── tests/
├── infrastructure/         # Terraform, K8s, Helm, Docker
├── dashboard/              # Next.js frontend
└── docs/                   # Architecture and deployment docs
```

## Quick Start

```bash
# Install
pip install -e ".[dev]"

# Run
make dev

# Test
make test

# Docker
docker compose up -d
```

## Primary Service

**Security Platform + LLM**

---

Built as part of the Enterprise AI Agent Platform.
