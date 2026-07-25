import streamlit as st
import pandas as pd
import json

# ---------------------------------------------------
# CONFIGURAÇÃO DA PÁGINA
# ---------------------------------------------------

st.set_page_config(
    page_title="TechSolutions Folha",
    page_icon="💰",
    layout="wide"
)

st.title("💰 Processador de Folha TechSolutions")
st.caption("PMV 4.0 • Streamlit Edition")

# ---------------------------------------------------
# ESTADO DA SESSÃO
# ---------------------------------------------------

if "holerites" not in st.session_state:
    st.session_state.holerites = []

# ---------------------------------------------------
# FUNÇÃO DE FORMATAÇÃO
# ---------------------------------------------------

def formatar_moeda(valor):
    return (
        f"{valor:,.2f}"
        .replace(",", "X")
        .replace(".", ",")
        .replace("X", ".")
    )

# ---------------------------------------------------
# SIDEBAR
# ---------------------------------------------------

with st.sidebar:

    st.header("Cadastro")

    with st.form("form_colaborador"):

        colaborador = st.text_input("Colaborador")

        cargo = st.text_input("Cargo")

        valor = st.number_input(
            "Valor (R$)",
            min_value=0.0,
            step=100.0,
            format="%.2f"
        )

        enviar = st.form_submit_button("Cadastrar")

        if enviar:

            if colaborador and cargo:

                registro = {
                    "Colaborador": colaborador,
                    "Cargo": cargo,
                    "Valor": valor
                }

                st.session_state.holerites.append(registro)

                st.success("Holerite registrado com sucesso!")

            else:
                st.warning(
                    "Informe Colaborador e Cargo."
                )

# ---------------------------------------------------
# DATAFRAME
# ---------------------------------------------------

df = pd.DataFrame(st.session_state.holerites)

# ---------------------------------------------------
# MÉTRICAS
# ---------------------------------------------------

st.subheader("Resumo Geral")

total_folha = (
    df["Valor"].sum()
    if not df.empty
    else 0
)

col1, col2 = st.columns(2)

with col1:
    st.metric(
        "Total de Holerites",
        len(st.session_state.holerites)
    )

with col2:
    st.metric(
        "Total da Folha",
        f"R$ {formatar_moeda(total_folha)}"
    )

# ---------------------------------------------------
# TABELA INTERATIVA
# ---------------------------------------------------

st.subheader("Folha Consolidada")

if not df.empty:

    st.dataframe(
        df,
        use_container_width=True,
        hide_index=True
    )

else:

    st.info(
        "Nenhum colaborador cadastrado."
    )

# ---------------------------------------------------
# EXPORTAÇÃO CSV
# ---------------------------------------------------

csv_data = df.to_csv(
    index=False
).encode("utf-8")

st.download_button(
    label="⬇️ Exportar CSV",
    data=csv_data,
    file_name="folha_lote.csv",
    mime="text/csv"
)

# ---------------------------------------------------
# EXPORTAÇÃO JSON
# ---------------------------------------------------

json_data = json.dumps(
    st.session_state.holerites,
    indent=4,
    ensure_ascii=False
)

st.download_button(
    label="⬇️ Exportar JSON",
    data=json_data,
    file_name="folha_lote.json",
    mime="application/json"
)