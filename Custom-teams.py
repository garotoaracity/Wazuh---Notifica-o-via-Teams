Criar /var/ossec/integrations/custom-teams.py.
nano /var/ossec/integrations/custom-teams.py

#!/usr/bin/env python3
import sys
import json
import requests

# Lê o alerta do Wazuh
alert_file = open(sys.argv[1])
alert_json = json.loads(alert_file.read())
alert_file.close()

# Pega dados principais
alert_level = alert_json.get('rule', {}).get('level', 'N/A')
description = alert_json.get('rule', {}).get('description', 'N/A')
agent = alert_json.get('agent', {}).get('name', 'N/A')
full_log = alert_json.get('full_log', '')

# Webhook do Teams
hook_url = sys.argv[3]

# Definição de cores por severidade
if int(alert_level) >= 10:
    color = "FF0000"   # vermelho crítico
elif int(alert_level) >= 7:
    color = "FFA500"   # laranja alto
elif int(alert_level) >= 4:
    color = "FFFF00"   # amarelo médio
else:
    color = "00FF00"   # verde baixo

# Monta o card no formato Teams (MessageCard)
msg_data = {
    "@type": "MessageCard",
    "@context": "http://schema.org/extensions",
    "themeColor": color,
    "summary": f"Alerta Wazuh - Nível {alert_level}",
    "sections": [{
        "activityTitle": f"🚨 Alerta Wazuh (Nível {alert_level})",
        "activitySubtitle": f"Agente: {agent}",
        "facts": [
            {"name": "Descrição", "value": description},
            {"name": "Agente", "value": agent},
            {"name": "Severidade", "value": str(alert_level)},
        ],
        "text": f"```{full_log}```"
    }]
}

# Envia pro Teams
headers = {'Content-Type': 'application/json'}
response = requests.post(hook_url, headers=headers, data=json.dumps(msg_data))

if response.status_code != 200:
    print(f"Erro ao enviar para Teams: {response.status_code} - {response.text}")
    sys.exit(1)

sys.exit(0)

Ajuste no ossec.conf
<integration>
    <name>custom-teams</name>
    <level>3</level>
    <hook_url>https://outlook.office.com/webhook/SEU_WEBHOOK_AQUI</hook_url>
    <alert_format>json</alert_format>
</integration>

