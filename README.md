# 🔐 Wazuh Integrations – Telegram & Microsoft Teams

Este repositório contém scripts de integração personalizados para enviar alertas do **Wazuh** diretamente para:

- 💬 **Microsoft Teams**

---

## 📌 Requisitos

- Wazuh Manager instalado (>= 4.x)
- Python 3 com módulo `requests`
- Acesso a criar webhooks no Teams e no Telegram Bot

Instalar dependências no servidor:

```bash
sudo apt update && sudo apt install python3-pip -y
pip3 install requests
