# 🔐 Wazuh Integrations – Telegram & Microsoft Teams

Este repositório contém scripts de integração personalizados para enviar alertas do **Wazuh** diretamente para:

- 💬 **Microsoft Teams**

---

## 📌 Requisitos

- Wazuh Manager instalado (>= 4.x)
- Python 3 com módulo `requests`
- Acesso a criar webhooks no Teams.

Instalar dependências no servidor:

```bash
sudo apt update && sudo apt install python3-pip -y
pip3 install requests

**Criar o script de integração.**
nano /var/ossec/integrations/custom-teams
Cópia Conteúdo
Custom-teams

Dar permissões:
chown root:wazuh /var/ossec/integrations/custom-teams*
chmod 750 /var/ossec/integrations/custom-teams*

Criar /var/ossec/integrations/custom-teams.py
nano /var/ossec/integrations/custom-teams.py

cópia Conteúdo
Custom-teams.py
