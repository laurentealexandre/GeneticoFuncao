Como rodar o código:
    1. Abra a pasta no VsCode selecione e rode o arquivo funcao.py
    2. Ao rodar será solicitado que você digite os seguintes dados em negrito:
        2.1. Digite o tamanho da população inicial: 10 e aperte enter
        2.2. Digite a taxa de mutação (entre 0 e 1): número entre 0 e 1 (dependendo da sua escolha) e aperte enter
        2.3.  Digite o número de pontos de cruzamento (1 ou 2): número 1 ou 2 (dependendo da sua escolha) e aperte enter
Após digitar estes dados o código entrará em execução;

Como funciona o programa
A função `decodificar_cromossomo` converte o cromossomo binário para um valor real entre -10 e 10.
A função `criar_populacao_inicial` gera uma população aleatória de indivíduos.
A função `calcular_aptidao` avalia quão boa é uma solução. (quanto menor o valor da função objetivo, maior a aptidão)
Utilizamos o método de seleção por torneio (`selecao_torneio`) que seleciona aleatoriamente um grupo de indivíduos e escolhe o melhor deles.
  A função `cruzamento` combina dois pais para criar dois filhos. (pode usar um ou dois pontos de corte, dependendo da configuração)
A função `mutacao` aplica pequenas alterações aleatórias nos indivíduos. (os melhores indivíduos de uma geração são preservados na próxima (se ativado).)
Loop Principal do Algoritmo Genético:
   O algoritmo executa por um número fixo de gerações (MAX_GERACOES).
   Em cada geração:
    1. A população é ordenada por aptidão.
    2. Os melhores indivíduos são preservados (elitismo).
    3. Novos indivíduos são criados por seleção, cruzamento e mutação.
    4. A nova população substitui a antiga.
    5. O melhor indivíduo da geração é exibido.
   Após todas as gerações, o algoritmo retorna a melhor solução encontrada.

Claro, vou explicar como este algoritmo genético resolve o problema de encontrar o valor de x que minimiza a função f(x) = x³ - 6x + 14 no intervalo [-10, 10].

Como o algoritmo resolve o problema


O algoritmo começa solicitando ao usuário alguns parâmetros configuráveis: tamanho da população, taxa de mutação e número de pontos de cruzamento. Outros parâmetros são predefinidos, como o uso de elitismo, percentual de elitismo e número máximo de gerações. Cada solução potencial (valor de x) é representada por um cromossomo binário de 16 bits. A função `decodificar_cromossomo` converte o cromossomo binário para um valor real no intervalo [-10, 10]. Uma população inicial é criada aleatoriamente usando a função `criar_populacao_inicial`. A função `calcular_aptidao` avalia cada indivíduo. Como queremos minimizar f(x), a aptidão é calculada como 1 / (1 + |f(x)|). Quanto menor o valor de f(x), maior a aptidão. A seleção é feita por torneio usando a função `selecao_torneio`. Ela escolhe aleatoriamente 3 indivíduos e seleciona o melhor deles. O cruzamento é realizado pela função `cruzamento`, que pode usar 1 ou 2 pontos de corte, dependendo da configuração. A mutação é aplicada pela função `mutacao`, que inverte bits aleatoriamente com base na taxa de mutação definida. Se ativado, os melhores indivíduos de cada geração são preservados na próxima geração. O algoritmo passa por várias gerações (até MAX_GERACOES). Em cada geração: A população é ordenada por aptidão. os melhores indivíduos são preservados se o elitismo estiver ativado, novos indivíduos são criados por seleção, cruzamento e mutação até preencher a população, o melhor indivíduo da geração é avaliado e seu valor é impresso. Ao final das gerações, o algoritmo retorna o melhor x encontrado e o valor correspondente de f(x).

Este algoritmo resolve o problema iterativamente, explorando o espaço de busca através de operações genéticas (seleção, cruzamento, mutação) e convergindo para uma solução que minimiza a função objetivo. A codificação binária permite uma representação precisa no intervalo [-10, 10], e as operações genéticas permitem tanto a exploração global do espaço de busca quanto o refinamento local de soluções promissoras.
