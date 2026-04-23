# 🚀 Ideal Memory

Projeto desenvolvido com foco em práticas modernas de desenvolvimento, integração contínua (CI), conteinerização com Docker e automação de workflows com GitHub Actions.

---

## 📌 Objetivo

Este projeto tem como objetivo demonstrar a construção de uma aplicação com:

- Integração contínua (CI)
- Pipeline automatizado
- Validação de código com linters
- Conteinerização com Docker
- Integração com serviços externos (Discord)
- Boas práticas de DevOps

---

## 🧠 Tecnologias Utilizadas

### 🔹 Backend
- Python
- (Possível uso de FastAPI)

### 🔹 Frontend
- HTML
- CSS
- JavaScript

### 🔹 DevOps & Infra
- Docker
- Docker Hub
- GitHub Actions (CI/CD)

### 🔹 Qualidade de Código
- Pylint (Python)
- ESLint (JavaScript)
- Stylelint (CSS)
- HTMLHint (HTML)

### 🔹 Integrações
- Webhook Discord (notificação de commits)

---

## ⚙️ Pipeline CI/CD

O projeto utiliza GitHub Actions para automação completa do fluxo de desenvolvimento.

### 🔄 Etapas do Pipeline:

#### ✅ 1. Validação de Código (CI)
Executado em `pull_request`:

- Análise estática com Pylint
- Validação de HTML, CSS e JS
- Garantia de qualidade antes do merge

#### 🐳 2. Build e Deploy (CD)
Executado em `push` na branch `main`:

- Build da imagem Docker
- Push automático para Docker Hub

#### 🔔 3. Notificação
- Envio automático de commits para o Discord via webhook

---

## 🐳 Docker

O projeto é conteinerizado, permitindo fácil execução e portabilidade.