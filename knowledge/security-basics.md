# Fundamentos de Segurança

Base conceitual compartilhada para análises de vulnerabilidade, avaliação de risco e orientação defensiva.

## Vulnerabilidade, Ameaça e Risco
- **Vulnerabilidade:** é uma fraqueza ou falha em código, configuração, arquitetura, dependência ou processo que pode ser explorada.
- **Ameaça:** é qualquer agente, ator ou condição capaz de explorar uma vulnerabilidade (por exemplo, entrada maliciosa, credencial comprometida ou exposição indevida).
- **Risco:** é a combinação da **probabilidade** de uma ameaça explorar uma vulnerabilidade com o **impacto** desse evento no contexto do sistema, dos dados e do negócio. Uma falha grave em um ambiente isolado de laboratório tem risco diferente da mesma falha em produção exposta à internet.

## Tríade CID
- **Confidencialidade:** protege informações contra acesso, leitura ou divulgação não autorizados. Violação ocorre, por exemplo, em vazamento de dados, credenciais ou consultas indevidas.
- **Integridade:** garante que dados, código e configurações sejam precisos, completos e alterados apenas de forma autorizada. Violação ocorre em adulteração de registros, comandos injetados ou modificação não autorizada de arquivos.
- **Disponibilidade:** assegura que sistemas, serviços e dados estejam acessíveis e operacionais quando necessário. Violação ocorre em travamentos, sobrecarga, exclusão de dados ou bloqueio de acesso legítimo.

## Boas Práticas Defensivas
- **Separação entre código e dados:** nunca montar comandos SQL, shell ou consultas estruturadas concatenando entrada de usuário diretamente; usar parâmetros ou APIs seguras.
- **Princípio do menor privilégio:** conceder apenas as permissões mínimas necessárias para cada usuário, processo, conta de serviço ou aplicação.
- **Validação e tratamento de entradas:** validar formato, tipo e limites na entrada, mas sem depender apenas de "lista negra" como substituto de controles estruturais.
- **Redução de superfície de ataque:** expor apenas portas, serviços, endpoints e recursos estritamente necessários, mantendo sistemas e dependências atualizados.
- **Verificação pós-correção:** após aplicar uma mitigação, testar e revisar novamente para confirmar que a causa raiz foi resolvida sem introduzir novos problemas.