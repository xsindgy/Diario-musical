🎵 Diário Musical

Registre sua música do dia, seu humor e acompanhe como você se sente ao longo do tempo.

Um projeto feito em Python puro — sem frameworks, sem dependências externas — que combina persistência de dados em JSON, validação de entrada e geração de relatórios mensais num terminal interativo.

💡 Sobre o projeto
A ideia surgiu de uma pergunta simples: e se eu pudesse olhar pra trás e ver exatamente o que eu estava ouvindo nos meus dias mais difíceis — ou nos melhores?
O Diário Musical permite registrar uma entrada por dia com sua música mais ouvida, seu estado emocional e uma nota de humor. No fim do mês, o programa gera um relatório com média de humor, músicas mais ouvidas e o melhor dia registrado.

🖥️ Como funciona
Menu principal
Mostrar Imagem
O programa roda no terminal com um menu interativo. O usuário navega pelas opções digitando o número correspondente. O match/case (Python 3.10+) garante um fluxo limpo e legível.

Coleta de dados
Mostrar Imagem
A função como_esta_se_sentido() coleta os dados do usuário com validação robusta:

Usa while True + try/except para garantir que a nota seja sempre um número válido entre 0 e 5
Usa f-string para confirmar o artista da música digitada, reduzindo erros de associação
Retorna um dicionário completo com data, sentimento, nota, música e artista


Persistência em JSON
Mostrar Imagem
Os dados são salvos localmente num arquivo dicionario_humor.json como uma lista de dicionários:

carregar_arquivo_json() trata o caso do arquivo não existir ainda com FileNotFoundError
salvar_registros() sobrescreve o arquivo com a lista atualizada a cada novo registro
registrar_dia() orquestra todo o fluxo: carregar → coletar → adicionar → salvar


⚙️ Funcionalidades

Registrar o dia — coleta humor, nota, música e artista com validação completa
Ver histórico — exibe todos os registros formatados com emojis e separadores
Relatório do mês — mostra total de dias, média de humor, top 5 músicas mais ouvidas e o melhor dia registrado
Limpeza de terminal — compatível com Windows (cls) e Mac/Linux (clear) via os.name


🗂️ Estrutura do projeto
diario_musical/
├── main.py              ← código principal
└── dicionario_humor.json  ← gerado automaticamente no primeiro uso

🚀 Como rodar
Pré-requisitos: Python 3.10 ou superior
bash# Clone o repositório
git clone https://github.com/seu-usuario/diario-musical.git

# Entre na pasta
cd diario-musical

# Rode o programa
python main.py
Nenhuma instalação de dependências necessária — o projeto usa apenas bibliotecas nativas do Python.

🧠 O que aprendi construindo esse projeto

Estruturação de dados com dicionários e listas
Persistência de dados com JSON (json.load e json.dump)
Validação de entrada com while True + try/except
Manipulação de datas com o módulo datetime
Contagem de ocorrências com Counter do módulo collections
Busca de máximo com max() + lambda
Compatibilidade entre sistemas operacionais com os.name
Boas práticas: funções com responsabilidade única, comentários objetivos e if __name__ == '__main__'


📌 Próximos passos

 Filtrar o relatório por mês específico
 Exportar o relatório como PDF
 Plotar gráfico de humor ao longo do tempo com matplotlib
 Versão com interface gráfica usando tkinter


Feito com 🎧 e muito print().
