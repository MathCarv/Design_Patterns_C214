# Exercício de Design Patterns

## Descrição

Este repositório contém o código relacionado ao exercício de Design Patterns. O exercício tem como objetivo explorar a implementação dos padrões Observer e Strategy em um contexto de ordenação de dados.

## Padrões de Design Utilizados

### Observer 

O padrão Observer é utilizado para estabelecer uma comunicação de "um-para-muitos" entre um objeto chamado de "observável" e vários objetos chamados de "observadores". No contexto desse exercício, o padrão Observer é utilizado para notificar os observadores sobre a análise de frases.

### Strategy 

O padrão Strategy é utilizado para definir uma família de algoritmos, encapsulá-los e torná-los intercambiáveis. No contexto desse exercício, o padrão Strategy é utilizado para implementar diferentes estratégias de ordenação dos dados.

## Funcionalidade

O código fornecido contém as seguintes funcionalidades:

   ```sh
   SortStrategy: Classe abstrata que define a interface para as estratégias de ordenação.
   ```
   ```sh
   BubbleSort: Implementação da estratégia de ordenação Bubble Sort.
   ```
   ```sh
   QuickSort: Implementação da estratégia de ordenação Quick Sort.
   ```
   ```sh
   InsertionSort: Implementação da estratégia de ordenação Insertion Sort.
   ```
   ```sh
   Sorter: Classe responsável por executar a ordenação dos dados de acordo com a estratégia escolhida.
   ``` 
   ```sh  
   Observavel: Classe que representa o objeto observável no padrão Observer.
   ```
   ```sh
   Observer: Classe abstrata que define a interface para os observadores.
   ```
   ```sh
   ConcreteObserver: Implementação concreta do observador que realiza a análise das frases.
   ```
   
Além disso, o código também inclui um arquivo de testes test_strategy.py que verifica a correta implementação das estratégias de ordenação.

### Instalação

1. Clone o repositório

   ```sh
   git clone https://github.com/MathCarv/Design_Patterns_C214
   ```
2. Entre em observer

   ```sh
   cd observer
   ```
3. Execute com:

   ```sh
   python3 observer.py
   ```
   
4. Para executar os testes faça:

   ```sh
   python3 test_observer.py
   ```

5. Entre em strategy:

   ```sh
   cd strategy
   ```

5. Execute com:   

   ```sh
   python3 strategy.py
   ```

6. Para executar os testes faça:

   ```sh
   python3 test_strategy.py
   ```

### Alunos

Matheus GEC 1877  

Igor da Silva Villamarim GEC 1641
