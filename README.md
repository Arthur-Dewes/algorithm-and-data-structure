# algorithm-and-data-structure

## Repositório

Este repositório contém implementações de diferentes tipos de estruturas de dados encadeadas (listas, filas, pilhas) em Java e Python. A principal diferença entre as implementações é que a versão Python da **Linked List** é feita de forma funcional, utilizando uma sequência de tuplas, enquanto nas versões Java as estruturas são implementadas de forma imperativa, usando classes e nós.

## Descrição dos Arquivos

### Collections

1. **doubleLinkedList.java**  
   Implementação de uma lista duplamente encadeada em Java. A estrutura permite inserções e remoções eficientes tanto no início quanto no final da lista, além de métodos para acesso e manipulação de elementos.

2. **linkedList.java**  
   Implementação de uma lista encadeada simples em Java. A classe `linkedList` oferece funcionalidades típicas, como inserção no final, remoção, busca por elementos e manipulação de índices.

3. **QueueArray.java**  
   Implementação de uma fila em Java, utilizando um array para armazenar os elementos. Esta estrutura tem capacidade fixa e permite enfileirar e desenfileirar elementos de forma eficiente.

4. **Queue.java**  
   Implementação de uma fila em Java, utilizando uma estrutura encadeada. Os métodos principais incluem `enqueue`, `dequeue` e `peek`, que permitem manipular os elementos da fila.

5. **Stack.java**  
   Implementação de uma pilha em Java, usando uma estrutura encadeada. A classe `Stack` oferece os métodos básicos para empilhar, desempilhar e acessar o topo da pilha.

6. **linkedList.py**  
   Implementação de uma lista encadeada em Python utilizando uma abordagem funcional. A lista é representada como uma sequência de tuplas, com cada tupla contendo um elemento e a referência para o próximo elemento. Não há mutação de objetos, já que a implementação segue o paradigma funcional.

