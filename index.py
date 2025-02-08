import streamlit as st
import time


def main():  # Def Main, definir tudo que será exibido na tela
    st.title("Esse é o título")
    st.write("Texto simples gerado")
    input_text = st.text_input("Digite um texto aqui: ")
    if input_text:
        st.write("Você digitou: ", input_text)

    st.header("Seleção")
    selected_option = st.selectbox("Selecione uma opção: ", [
                                   "Opção 1", "Opção 2", "Opção 3"])
    if selected_option:
        st.write("Opção selecionada : ", selected_option)

    st.header("Slider")
    slider_value = st.slider("Escolhau um valor: ", 0, 100, 50)
    st.write(slider_value)

    st.header("Checkbox")

    checkbox_state = st.checkbox("Marque para ativar")
    st.write("Checkbox ativado: ", checkbox_state)


    st.header("Botão")

    if st.button("clique aqui"):
        st.write("Você clicou!")


    st.header("Loading")
    with st.spinner("Aguarde..."):
        time.sleep(3)
    st.success("Carregado")

    st.header("Upload de Arquivos")

    upload_file = st.file_uploader("Escolha um arquivo: ", type=["pdf", "jpeg"])
    if upload_file:
        st.write("Nome do arquivo: ", upload_file.name)


    st.header("Gráficos")

    data = {'x': [1, 2, 3 , 4 , 5], 'y' : [10, 20, 30 , 40 ,50 ]}
    st.line_chart(data)


main()
