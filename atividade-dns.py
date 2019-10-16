import os
os.system('clear') or None
x=0:
while x ==0:
	print("---------- SERVIDOR DNS ----------")
	pergunta = input(int("Selecione uma opção:\n1 - Criar o arquivo para receber os dados dos hosts\n 2 - Inserir novos dados – nome do host e ip - no arquivo\n 3 - Consultar um host pelo nome e exibir seus seu ip\n 4 - Consultar um host pelo IP e exibir seu nome \n5 - Apresentar a quantidade de hosts de um determinado domínio\n 6 - Apresentar um relatório com todos os hostnames em formato incorreto\n 7 - Alterar os dados de um host\n8 - Sair\n>>  "))
	
	if pergunta == 1:
		os.system('clear') or None
		arq = open(hosts.txt,'w')
		arq.close()
		print("O arquivo hosts.txt foi criado")
		

	elif pergunta == 2:
		os.system('clear') or None
		nome_host = input("Digite o nome do host: ")
		ip = input("Digite o IP: ")
		dominio = input("Digite o dominio: ")
		arq = open(hosts.txt,'a')
		arq.write( nome_host"@"nome_host"."dominio ip)
		arq.close()

	def pesquisar_registro(txt):
		resultado = ""
		with open( 'arq.txt', 'r' ) as a:
    	for linha in a:
        	if resultado == "":
            	if txt in linha:
                	resultado = linha
                	ip = resultado.split('br ')[1].strip('\n')
                	print(ip);
    	else: a.close()
		pritn("nome não encontrado");

	def pesquisar_registro(ip):
		resultado = ""
		with open( 'arq.txt', 'r' ) as a:
		for linha in a:
	    	if resultado == "":
	        	if ip in linha:
	            	resultado = linha
	            	ip = resultado.split(' ',1).strip('\n')
	            	print(ip);
		else: a.close()
		pritn("nome não encontrado");

	elif pergunta == 3:
		os.system('clear') or None
		consulta_nome = input("Digite o nome do host: ")
		pesquisar_registro(consulta_nome)
		arq.close()

	elif pergunta == 4:
		os.system('clear') or None
		consulta_ip = input("Digite o nome do ip: ")
		pesquisar_ip(consulta_ip)
		arq.close()

	elif pergunta == 5:
		os.system('clear') or None
		dom = input("Digite o nome do domínio: ")
		with open('arquivo.txt') as f:
    		num_hosts = f.read().count(dom)
		print("o domínio "dom" possui "num_hosts" hosts.")		
		arq.close()

	elif pergunta == 6:
		print("Relatório com todos os hostnames: \n")
		# como selecionar o ip: arq.open('arq.txt' r'(\d{3}\.?\d{3}\.?\d{3}\.)')
