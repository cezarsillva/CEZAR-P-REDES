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

- **Como levantar o projeto**


- **Suba os containers:**

docker compose up -d


- **Verifique os containers:**

docker ps


- **Acesse a interface web:**

http://localhost:8080
https://localhost:8443


Usuário padrão: Admin
Senha padrão: zabbix

- **Verificar a rede interna**

- **Lista todas as redes Docker:**

docker network ls


- **Inspecione a rede redecezar:**

docker network inspect redecezar


- **Aqui você verá os IPs fixos de cada container e sua comunicação interna.**

- **Parar ou reiniciar o projeto**

- **Parar:**

docker compose down


- **Reiniciar sem perder dados:**

docker compose up -d

- **Estrutura de IPs**

- **Container	IP**

- MySQL Server	172.28.0.2
- Zabbix Server	172.28.0.3
- Zabbix Web Interface	172.28.0.4
- Docker Host Agent	172.28.0.5
- Cliente Docker01	172.28.0.6
- Cliente Docker02	172.28.0.7
- Zabbix Server Agent	172.28.0.8

---

- ** Como adicionar os templates no Zabbix **

Configuration → Hosts → Create Host.

Preencha:

Host name: Docker01 (mesmo do ZBX_HOSTNAME)

Groups: Linux servers (ou crie Docker hosts)

Agent interfaces:

Type: Zabbix agent

IP: container name (Docker01) ou IP do container na rede Docker

Port: 10050 (padrão do agente Zabbix)

Vincule templates:

Template OS Linux → monitora CPU, memória, disco e rede.

Se quiser, adicione templates Docker se você instalar o monitor de Docker.

Repita para Docker02.
Repita para os outros a ser monitorado. Observando os ips e Host name.
