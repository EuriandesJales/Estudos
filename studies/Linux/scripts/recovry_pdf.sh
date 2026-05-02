#!/bin/bash
###########################################################################################
# 				Automação do processo de recuperação de pdf
#################################################################################################
# versão 1.0

# Árvore de objetos corrompida.
# 	Internal Error: xref num 3 not found... try to reconstruct
#	Syntax Error: Kid object (page 1) is wrong type (null)





# Criar um diretório de saída para não sobrescrever os originais imediatamente (Segurança)
mkdir -p corrigidos

for arquivo in *.pdf; do # para cada aquivo na pasta com extenção .pdf faça
    # Pular o loop se não houver arquivos .pdf
    [ -e "$arquivo" ] || continue
    
    echo "⚙️ Processando: $arquivo..."
    
    # Executa o Ghostscript
    # Usamos uma variável para o arquivo de saída temporário
    gs -o "corrigidos/$arquivo" \ # Pular o loop se não houver arquivos .pdf
       -sDEVICE=pdfwrite \ # Pular o loop se não houver arquivos .pdf
       -dPDFSETTINGS=/prepress \ #Define um perfil de alta qualidade. Isso garante que fontes e imagens não sejam excessivamente comprimidas.
       -dBATCH -dNOPAUSE -dQUIET \ #Faz com que o processo seja automático dquit Silencia o log interno do GS, mostrando apenas erros críticos.
       "$arquivo"
    
    if [ $? -eq 0 ]; then
        echo "✅ $arquivo corrigido com sucesso."
    else
        echo "❌ Erro ao processar $arquivo."
    fi
done

echo "🏁 Processo concluído. Os arquivos estão na pasta 'corrigidos'."

# rode os comandos abaixo depois de certificar que a operação foi concluida com exito
# mv corrigidos/*.pdf . && rm -rf corrigidos
