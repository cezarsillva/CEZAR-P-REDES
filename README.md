# Projeto Zabbix + Docker Compose

Este projeto cria um **ambiente completo de monitoramento com Zabbix** usando Docker Compose, incluindo servidor, banco de dados, web interface e agentes simulando hosts monitorados.  

---

## **Conteúdo do Projeto**

O projeto inclui:

- **Banco de dados MySQL** (`zabbix-mysql`)  
  - Armazena todas as informações do Zabbix (itens, triggers, históricos).  
  - Volume persistente: `mysql_data`.  

- **Zabbix Server** (`zabbix-server`)  
  - Recebe métricas dos agentes, processa triggers e alertas.  
  - Volumes persistentes: `zabbix_alertscripts`, `zabbix_export`.  

- **Zabbix Web Interface** (`zabbix-web`)  
  - Interface gráfica para administração e visualização de métricas e alertas.  
  - Portas expostas: `8080` (HTTP) e `8443` (HTTPS).  

- **Agentes Zabbix**  
  - `zabbix-agent2` → monitora o host Docker.  
  - `Docker01` e `Docker02` → hosts simulados.  
  - `zabbix-server-agent` → monitora o próprio servidor Zabbix.  

- **Rede personalizada** (`redecezar`) com IPs fixos para garantir comunicação estável entre containers.  
- **Volumes persistentes** para manter dados importantes mesmo após reinicialização dos containers.

---
