import streamlit as st
import textwrap
from pathlib import Path

# ==========================================
# CONFIGURAÇÃO
# ==========================================
st.set_page_config(
    page_title="Dinaldo Tech",
    page_icon="🚀",
    layout="wide",
    initial_sidebar_state="collapsed"
)

# ==========================================
# CSS MODERNO
# ==========================================
st.markdown("""
<style>
@import url('https://fonts.googleapis.com/css2?family=Orbitron:wght@500;700;800&family=Poppins:wght@300;400;500;600;700&display=swap');

.stApp {
    background:
        radial-gradient(ellipse at top left, #15375a 0%, transparent 45%),
        radial-gradient(ellipse at bottom right, #064638 0%, transparent 40%),
        linear-gradient(135deg, #050816, #0b1120 60%, #071b24);
    color: #f0f6ff;
    font-family: 'Poppins', sans-serif;
}

header, footer, #MainMenu {
    visibility: hidden;
}

.block-container {
    max-width: 1100px;
    padding-top: 2rem;
    padding-bottom: 2rem;
}

/* Animação de entrada */
@keyframes entrada {
    from {
        opacity: 0;
        transform: translateY(25px);
    }
    to {
        opacity: 1;
        transform: translateY(0);
    }
}

/* Animação do brilho */
@keyframes brilho {
    0%, 100% {
        box-shadow: 0 0 15px #00d9ff22;
    }
    50% {
        box-shadow: 0 0 35px #00d9ff55;
    }
}

/* Animação flutuante */
@keyframes flutuar {
    0%, 100% {
        transform: translateY(0);
    }
    50% {
        transform: translateY(-8px);
    }
}

/* Cartão principal */
.hero {
    position: relative;
    overflow: hidden;
    text-align: center;
    padding: 50px 25px;
    border-radius: 25px;
    border: 1px solid #00d9ff66;
    background: linear-gradient(145deg, #14243bea, #081626ed);
    animation: entrada 1s ease-out, brilho 5s ease-in-out infinite;
}

/* Selo */
.selo {
    display: inline-block;
    padding: 8px 17px;
    margin-bottom: 20px;
    border: 1px solid #00ff9d77;
    border-radius: 30px;
    color: #00ffb3;
    background: #00ff9d10;
    font-family: 'Poppins', sans-serif;
    font-size: 12px;
    letter-spacing: 2px;
}

/* Título */
.titulo {
    font-family: 'Orbitron', sans-serif;
    font-size: clamp(30px, 5vw, 55px);
    font-weight: 800;
    line-height: 1.3;
    background: linear-gradient(90deg, #ffffff, #00d9ff, #00ffb3);
    -webkit-background-clip: text;
    background-clip: text;
    color: transparent;
    margin-bottom: 15px;
}

/* Linha neon */
.linha-neon {
    width: 120px;
    height: 3px;
    margin: 25px auto;
    border-radius: 10px;
    background: linear-gradient(90deg, #00d9ff, #00ff9d);
    box-shadow: 0 0 18px #00d9ff99;
}

/* Subtítulo */
.subtitulo {
    color: #c0cee0;
    font-family: 'Poppins', sans-serif;
    font-size: 16px;
    line-height: 1.9;
    font-weight: 300;
}

/* Botão principal */
.stLinkButton > a {
    background: linear-gradient(100deg, #007cf0, #00d9ff, #00e6a0) !important;
    color: #04111e !important;
    border: none !important;
    border-radius: 14px !important;
    padding: 15px 25px !important;
    font-family: 'Poppins', sans-serif !important;
    font-weight: 700 !important;
    transition: transform 0.3s ease, box-shadow 0.3s ease !important;
    box-shadow: 0 0 20px #00d9ff33;
}

.stLinkButton > a:hover {
    transform: translateY(-4px);
    box-shadow: 0 0 30px #00d9ff77;
}

/* Indicadores */
.indicadores {
    display: flex;
    justify-content: center;
    flex-wrap: wrap;
    gap: 12px;
    margin-top: 30px;
}

/* Cartões de navegação */
.indicador {
    display: inline-block;
    padding: 12px 18px;
    border: 1px solid #00d9ff44;
    border-radius: 12px;
    background: #ffffff08;
    color: #c0cee0;
    font-family: 'Poppins', sans-serif;
    font-size: 12px;
    letter-spacing: 1px;
    text-decoration: none !important;
    transition: all 0.3s ease;
}

.indicador:hover {
    color: #00ffb3 !important;
    border-color: #00ffb3;
    background: #00ff9d12;
    transform: translateY(-4px);
    box-shadow: 0 0 20px #00ff9d33;
}

/* Rodapé */
.rodape {
    text-align: center;
    margin-top: 40px;
    color: #8294aa;
    font-size: 12px;
    line-height: 1.8;
}

.rodape span {
    color: #00d9ff;
}

/* Responsividade */
@media (max-width: 768px) {
    .hero {
        padding: 35px 15px;
    }

    .subtitulo {
        font-size: 14px;
    }

    .block-container {
        padding-top: 1rem;
    }

    .indicador {
        padding: 12px;
        font-size: 11px;
    }
}

/* Acessibilidade */
@media (prefers-reduced-motion: reduce) {
    *, *::before, *::after {
        animation: none !important;
        transition: none !important;
    }
}
</style>
""", unsafe_allow_html=True)


# ==========================================
# CARTÃO PRINCIPAL
# ==========================================
html = """
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
        Explore projetos, soluções digitais e conhecimentos<br>
        que conectam ideias ao futuro.
    </div>

</div>
"""

st.markdown(
    textwrap.dedent(html).strip(),
    unsafe_allow_html=True
)


# ==========================================
# IMAGEM
# ==========================================
st.markdown("<br>", unsafe_allow_html=True)

col1, col2, col3 = st.columns([1, 1.2, 1])

with col2:

    imagem = Path(__file__).parent / "tec.png"

    if imagem.exists():

        st.image(
            str(imagem),
            use_container_width=True
        )

    else:

        st.warning(
            "Imagem tec.png não encontrada. "
            "Coloque-a na mesma pasta do app.py."
        )


# ==========================================
# BOTÃO PRINCIPAL DO SITE
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
# INDICADORES COM LINKS
# ==========================================

st.markdown("""
<div class="indicadores">

    <a class="indicador"
       href="https://dinaldo.com.br"
       target="_blank"
       rel="noopener noreferrer">
       ⚡ TECNOLOGIA
    </a>

    <a class="indicador"
       href="https://sites.google.com/view/python2023ifpb/in%C3%ACcio"
       target="_blank"
       rel="noopener noreferrer">
       💻 PROGRAMAÇÃO
    </a>

    <a class="indicador"
       href="https://dinaldo.com.br"
       target="_blank"
       rel="noopener noreferrer">
       🌐 INOVAÇÃO DIGITAL
    </a>

</div>
""", unsafe_allow_html=True)


# ==========================================
# RODAPÉ
# ==========================================
rodape = """
<div class="rodape">

    DESENVOLVIDO COM <span>♥</span> E TECNOLOGIA<br>

    © 2026 DINALDO JORGE · TODOS OS DIREITOS RESERVADOS

</div>
"""

st.markdown(
    textwrap.dedent(rodape).strip(),
    unsafe_allow_html=True
)
