import streamlit as st

# ==========================================
# CONFIGURAÇÃO DA PÁGINA
# ==========================================
st.set_page_config(
    page_title="Dinaldo | Tecnologia",
    page_icon="🚀",
    layout="wide",
    initial_sidebar_state="collapsed"
)

# ==========================================
# CSS MODERNO E EFEITOS TECNOLÓGICOS
# ==========================================
st.markdown("""
<style>

/* Importar fonte moderna */
@import url('https://fonts.googleapis.com/css2?family=Orbitron:wght@400;500;600;700;800&family=Poppins:wght@300;400;500;600;700&display=swap');

/* Fundo geral */
.stApp {
    background:
        radial-gradient(ellipse at top left, #102c4c 0%, transparent 45%),
        radial-gradient(ellipse at bottom right, #063b35 0%, transparent 40%),
        linear-gradient(135deg, #050816, #0b1120 60%, #071b24);

    color: #f0f6ff;
    font-family: 'Poppins', sans-serif;
}

/* Ocultar menu e rodapé */
#MainMenu {
    visibility: hidden;
}

footer {
    visibility: hidden;
}

header {
    background: transparent !important;
}

/* Remover espaços desnecessários */
.block-container {
    padding-top: 3rem;
    padding-bottom: 2rem;
    max-width: 1100px;
}

/* Animação de entrada */
@keyframes entrada {
    from {
        opacity: 0;
        transform: translateY(35px);
        filter: blur(8px);
    }
    to {
        opacity: 1;
        transform: translateY(0);
        filter: blur(0);
    }
}

/* Efeito de brilho */
@keyframes brilho {
    0%, 100% {
        text-shadow: 0 0 10px rgba(0, 217, 255, 0.3);
    }
    50% {
        text-shadow: 0 0 25px rgba(0, 217, 255, 0.8),
                     0 0 45px rgba(0, 217, 255, 0.3);
    }
}

/* Partículas luminosas */
@keyframes flutuar {
    0%, 100% {
        transform: translateY(0px);
    }
    50% {
        transform: translateY(-8px);
    }
}

/* Linha tecnológica */
@keyframes linha {
    0% {
        transform: scaleX(0);
        opacity: 0;
    }
    100% {
        transform: scaleX(1);
        opacity: 1;
    }
}

/* Cartão principal */
.hero {
    background: linear-gradient(
        145deg,
        rgba(18, 32, 58, 0.88),
        rgba(7, 20, 37, 0.88)
    );

    border: 1px solid rgba(0, 217, 255, 0.28);
    border-radius: 28px;
    padding: 55px 35px;
    text-align: center;

    box-shadow:
        0 0 35px rgba(0, 217, 255, 0.08),
        0 20px 60px rgba(0, 0, 0, 0.35);

    animation: entrada 1.2s ease-out;
    position: relative;
    overflow: hidden;
}

/* Reflexo no cartão */
.hero::before {
    content: "";
    position: absolute;
    top: 0;
    left: -100%;
    width: 60%;
    height: 2px;

    background: linear-gradient(
        90deg,
        transparent,
        #00d9ff,
        #00ff9d,
        transparent
    );

    animation: passagem 5s linear infinite;
}

@keyframes passagem {
    0% {
        left: -100%;
    }
    100% {
        left: 150%;
    }
}

/* Pequeno selo */
.selo {
    display: inline-block;
    padding: 9px 18px;
    border-radius: 30px;

    border: 1px solid rgba(0, 255, 157, 0.4);
    background: rgba(0, 255, 157, 0.07);

    color: #00ffb3;
    font-size: 12px;
    font-weight: 600;
    letter-spacing: 3px;

    margin-bottom: 25px;
}

/* Título */
.titulo {
    font-family: 'Orbitron', sans-serif;
    font-size: clamp(30px, 5vw, 54px);
    font-weight: 800;

    background: linear-gradient(
        90deg,
        #ffffff,
        #00d9ff,
        #00ffb3
    );

    -webkit-background-clip: text;
    -webkit-text-fill-color: transparent;

    margin-bottom: 15px;
    line-height: 1.3;

    animation: brilho 4s ease-in-out infinite;
}

/* Subtítulo */
.subtitulo {
    font-family: 'Poppins', sans-serif;
    color: #b4c6dc;
    font-size: 17px;
    line-height: 1.9;
    font-weight: 300;

    max-width: 650px;
    margin: 0 auto 25px auto;
}

/* Linha decorativa */
.linha-neon {
    width: 130px;
    height: 3px;
    margin: 25px auto;

    background: linear-gradient(
        90deg,
        #00d9ff,
        #00ff9d
    );

    border-radius: 20px;
    box-shadow: 0 0 18px rgba(0, 217, 255, 0.8);

    animation: linha 1.5s ease-out;
}

/* Imagem */
.imagem-container {
    padding: 20px;
    animation: flutuar 5s ease-in-out infinite;
}

/* Botões */
.stLinkButton > a {
    display: inline-flex;
    justify-content: center;
    align-items: center;

    background: linear-gradient(
        100deg,
        #007cf0,
        #00d9ff,
        #00e6a0
    ) !important;

    color: #04111e !important;
    border: none !important;
    border-radius: 14px !important;

    padding: 16px 34px !important;

    font-family: 'Poppins', sans-serif !important;
    font-size: 15px !important;
    font-weight: 700 !important;

    transition: all 0.3s ease !important;

    box-shadow:
        0 0 20px rgba(0, 217, 255, 0.18),
        0 8px 25px rgba(0, 0, 0, 0.25);
}

/* Efeito ao passar o mouse */
.stLinkButton > a:hover {
    transform: translateY(-4px) scale(1.03);

    box-shadow:
        0 0 30px rgba(0, 217, 255, 0.5),
        0 0 50px rgba(0, 255, 157, 0.15);

    border: none !important;
}

/* Indicadores inferiores */
.indicadores {
    display: flex;
    justify-content: center;
    flex-wrap: wrap;
    gap: 14px;

    margin-top: 35px;
}

.indicador {
    padding: 10px 16px;
    border-radius: 12px;

    background: rgba(255, 255, 255, 0.035);
    border: 1px solid rgba(150, 190, 230, 0.13);

    color: #b7c9dc;
    font-size: 12px;
    letter-spacing: 1px;
}

/* Rodapé personalizado */
.rodape {
    text-align: center;
    margin-top: 45px;
    padding: 20px;

    color: #71869e;
    font-size: 12px;
    letter-spacing: 1px;
}

.rodape span {
    color: #00d9ff;
}

/* Ajustes para celulares */
@media (max-width: 768px) {
    .block-container {
        padding-top: 1.5rem;
    }

    .hero {
        padding: 35px 18px;
        border-radius: 20px;
    }

    .subtitulo {
        font-size: 14px;
    }

    .selo {
        font-size: 10px;
        letter-spacing: 2px;
    }

    .stLinkButton > a {
        width: 100%;
        padding: 14px 20px !important;
    }
}

/* Respeitar preferência por movimento reduzido */
@media (prefers-reduced-motion: reduce) {
    *,
    *::before,
    *::after {
        animation: none !important;
        transition: none !important;
    }
}

</style>
""", unsafe_allow_html=True)


# ==========================================
# CONTEÚDO PRINCIPAL
# ==========================================

st.markdown("""
<div class="hero">

    <div class="selo">
        ● SISTEMA ONLINE
    </div>

    <div class="titulo">
        DINALDO TECH
    </div>

    <div class="linha-neon"></div>

    <div class="subtitulo">
        Tecnologia, programação e inovação.<br>
        Explore projetos, soluções digitais e conhecimentos
        que conectam ideias ao futuro.
    </div>

</div>
""", unsafe_allow_html=True)


# ==========================================
# IMAGEM
# ==========================================

st.markdown("<br>", unsafe_allow_html=True)

col1, col2, col3 = st.columns([1, 1.2, 1])

with col2:
    try:
        st.image(
            "tec.png",
            use_container_width=True
        )
    except Exception:
        st.info(
            "Coloque a imagem tec.png na mesma pasta do arquivo app.py."
        )


# ==========================================
# BOTÃO DE ACESSO
# ==========================================

st.markdown("<br>", unsafe_allow_html=True)

col1, col2, col3 = st.columns([1, 1.2, 1])

with col2:
    st.link_button(
        "🚀 ACESSAR MEU SITE",
        "https://dinaldo.com.br",
        use_container_width=True
    )


# ==========================================
# INDICADORES TECNOLÓGICOS
# ==========================================

st.markdown("""
<div class="indicadores">

    <div class="indicador">⚡ TECNOLOGIA</div>

    <div class="indicador">💻 PROGRAMAÇÃO</div>

    <div class="indicador">🌐 INOVAÇÃO DIGITAL</div>

</div>
""", unsafe_allow_html=True)


# ==========================================
# RODAPÉ
# ==========================================

st.markdown("""
<div class="rodape">
    DESENVOLVIDO COM <span>♥</span> E TECNOLOGIA<br><br>
    © 2026 DINALDO JORGE · TODOS OS DIREITOS RESERVADOS
</div>
""", unsafe_allow_html=True)