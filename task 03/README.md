# task 03 - RPNStacker Automatic/Regex Scanning
   - le arquivo com a expressão em RPN e devolve a expressão avaliada
   - a feature de scanning retorna uma lista de tokens utilizando regex
   - a partir dessa lista de tokens, realiza a interpretação das expressões com uma pilha
   - a feature de scanning retorna um erro caso nao reconheca um "num" [numero] ou "op" [operator]

## exemplo de entrada:
```
10
10
+
```
**saída: 20**

## para rodar:
```
python rpnStacker.py [nome do arquivo]        
```
_obs.: se um arquivo não for dado como entrada, usa o `Calc1.stk` presente na pasta como padrão_