# README Jogo da Velha

## Descrição
Este código implementa uma versão simples do clássico jogo da velha para dois jogadores jogarem no terminal. O jogo permite que os jogadores, alternadamente, escolham uma posição no tabuleiro para marcar com seu símbolo ("X" ou "O"). O jogo continua até que um dos jogadores vença alinhando três de seus símbolos verticalmente, horizontalmente ou diagonalmente, ou até que todas as posições estejam ocupadas, resultando em um empate.

## Funcionamento do Jogo
O jogo segue estas etapas:

1. Um tabuleiro vazio é exibido.
2. O jogador "X" começa o jogo escolhendo uma posição no tabuleiro, de 1 a 9.
3. O tabuleiro é atualizado e exibido novamente com a marcação do jogador.
4. A vez é alternada para o jogador "O", que então escolhe uma posição livre no tabuleiro.
5. O processo se repete até que um jogador vença ou até que não haja mais posições livres, resultando em um empate.
6. O jogo exibe o resultado (vitória de um dos jogadores ou empate) e termina.

## Funções do Código
- `criar_tabuleiro()`: Cria e retorna um tabuleiro de jogo vazio.
- `imprimir_tabuleiro(tabuleiro)`: Exibe o tabuleiro atual no terminal.
- `receber_jogada(jogador, tabuleiro)`: Permite que o jogador atual escolha uma posição livre no tabuleiro.
- `checar_vitoria(tabuleiro, jogador)`: Verifica se o jogador atual venceu o jogo.
- `checar_empate(tabuleiro)`: Verifica se o jogo terminou em um empate.
- `jogo_da_velha()`: Controla o fluxo do jogo, alternando entre os jogadores e checando o estado do jogo após cada jogada.

## Notas Adicionais
- Este jogo é para dois jogadores, jogando no mesmo dispositivo.
- Não há implementação de inteligência artificial para jogar contra o computador.
- O código é simples e focado na funcionalidade básica do jogo da velha, sem recursos avançados de interface gráfica ou rede.

Divirta-se jogando o clássico jogo da velha diretamente do seu terminal!
