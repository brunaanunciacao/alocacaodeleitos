---

Resumo do projeto

 - O projeto de Regulação de Leitos funciona a partir da inserção da    quantidade de pacientes e leitos, ambos aleatórios.  
 - Após a definição da quantidade, são gerados dados tanto para os pacientes (número de identificação, gravidade e idade), quanto para os leitos (número do leito, id do hospital e tipo do leito).  
 - Em seguida é verificada a idade do paciente e sua prioridade na fila adequada, para logo em seguida alocar o paciente para o leito mais recente. 
 - E por fim, os dados do leito ocupado são excluídos do sistema.  
 - Os ciclos do projeto funcionam a partir de "dias" que são exibidos na interface.     
 - Além dos ciclos, existem eventos aleatórios durante a execução, um    paciente pode melhorar durante a fila de espera ou piorar dependendo    da probabilidade do evento acontecer.
---
Justificativa

**Fila de Prioridade**
Para a fila de pacientes, foi escolhido o uso de uma fila de prioridade para cada idade do paciente. Porque assim que o dado for coletado já é armazenado de uma maneira mais rápida pela fila de prioridade. Foi usado como referencia para a construção da fila[^1].
**Pilha** 
Para os leitos do hospital, foi necessário a utilização de uma pilha. Pois os leitos mais recentes eram os leitos utilizados primeiramente e a estrutura da pilha faz exatamente essa função, em que os itens inseridos por último são retirados primeiro.
**Tupla**
A escolha da tupla foi para armazenar mais de um dado para cada paciente e leito. De maneira que uma só variável pudesse retornar tanto o número, quando o tipo e a gravidade do paciente. 

---

Referências bibliográficas

[^1]:https://www.geeksforgeeks.org/priority-queue-using-linked-list/

  
