Projeto zabbix com Docker Compose


Este repositório contém uma configuração completa para implantação do Zabbix utilizando Docker Compose.
O projeto inclui o servidor Zabbix, frontend web, banco de dados MySQL e vários agentes Zabbix, tudo rodando em contêineres conectados por uma rede criada com o nome de redecezar.



Serviços incluídos

- mysql-server

Imagem: mysql:8.0.38

Função: Banco de dados para o servidor Zabbix.

Variáveis de ambiente:

MYSQL_ROOT_PASSWORD=zabbix

MYSQL_DATABASE=zabbix

MYSQL_USER=zabbix

MYSQL_PASSWORD=zabbix

Volumes:

mysql_data → persistência dos dados do MySQL.

Healthcheck: Verifica se o banco está acessível antes de iniciar o servidor Zabbix.


- zabbix-server

Imagem: zabbix/zabbix-server-mysql:alpine-7.4-latest

Função: Servidor principal do Zabbix responsável por coletar e processar dados de monitoramento.

Porta exposta: 10051

Depende de: mysql-server (aguarda até o banco estar saudável).

Volumes:

zabbix_alertscripts → scripts de alerta personalizados.

zabbix_export → exportação de templates e dados.



- zabbix-web

Imagem: zabbix/zabbix-web-nginx-mysql:alpine-7.4-latest

Função: Interface web do Zabbix (frontend).

Portas expostas:

8080 → HTTP

8443 → HTTPS

Depende de: zabbix-server

Timezone: America/Cuiaba

Após o start, a interface estará disponível em:

http://localhost:8080


ou

https://localhost:8443


- zabbix-agent2

Imagem: zabbix/zabbix-agent2:alpine-7.4-latest

Função: Agente Zabbix executando no host Docker, coletando métricas do sistema e do Docker.

Volumes:

/var/run/docker.sock → permite o monitoramento de contêineres Docker.

Hostname no Zabbix: Docker Host


- Docker01 e Docker02

Imagem: zabbix/zabbix-agent2:alpine-7.4-latest

Função: Agentes simulando hosts monitorados separados.

Hostnames no Zabbix:

Docker01

Docker02

- Rede

O projeto utiliza uma rede bridge personalizada chamada redecezar, com o seguinte esquema de IPs fixos:

Serviço	Endereço IP
mysql-server	172.20.0.2
zabbix-server	172.20.0.3
zabbix-web	172.20.0.4
zabbix-agent2	172.20.0.5
Docker01	172.20.0.6
Docker02	172.20.0.7

Sub-rede: 172.20.0.0/16
Gateway: 172.20.0.1


- Volumes

Nome do volume 	             -------------------------                   Uso
mysql_data	                 -------------------------      Armazena dados persistentes do MySQL
zabbix_alertscripts          -------------------------       Scripts personalizados de alerta
zabbix_export	               -------------------------       Exportações de dados/templates


Subir os contêineres

docker compose up -d

3. Verificar se todos os serviços estão ativos

docker ps

5. Acessar o Zabbix Web

Abra o navegador e acesse:

http://localhost:8080


Login padrão:

Usuário: Admin

Senha: zabbix
