import streamlit as st
### COLOCA UM TITULO
st.title("aluguel de carros")
### ESCREVE
st.write("Testando... esquerda e Direita")
### CRIA UMA BARRA LATERAL
st.sidebar.title("Aluguel de carros")

### CRIANDO A LISTA
carros = ["supramk4","diplomata","opala","inpala","bmw m4","eclipse"]
### CRIA A CAIXINHA NA BARRA LATERAL
st.sidebar.image("logo.png")


opção = st.sidebar._selectbox("Escolha o carro que foi alugado", carros)

st.image(f"{opção}.png")
st.markdown(f"voce alugou o modelo: {opção}")
st.markdown("--")

st.image(f"{opção}.png")
st.markdown(f"voce alugou o modelo: {opção}")
st.markdown("--")

st.image(f"{opção}.png")
st.markdown(f"voce alugou o modelo: {opção}")
st.markdown("--")