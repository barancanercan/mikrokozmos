import streamlit as st
from mikrokozmos.services.character_service import CharacterService
from mikrokozmos.services.mcp_service import MCPService
import os
from dotenv import load_dotenv
from mikrokozmos.characters.character import Character
import logging

# Logging ayarları
logging.basicConfig(level=logging.INFO)
logger = logging.getLogger(__name__)

# .env dosyasını yükle
load_dotenv()

# API anahtarını kontrol et
if not os.getenv("GEMINI_API_KEY"):
    st.error("GEMINI_API_KEY bulunamadı. Lütfen Streamlit Cloud'da Secrets ayarlarını kontrol edin.")
    st.stop()

# Set page config
st.set_page_config(
    page_title="Toplumsal Mikrokozmos",
    page_icon="🏘️",
    layout="wide"
)

# Initialize services
try:
    logger.info("Servisler başlatılıyor...")
    character_service = CharacterService()
    mcp_service = MCPService()
    logger.info("Servisler başarıyla başlatıldı.")
except Exception as e:
    logger.error(f"Servis başlatma hatası: {str(e)}")
    st.error(f"Servis başlatma hatası: {str(e)}")
    st.stop()

# Simülasyon durumu için session state
if 'simulation_running' not in st.session_state:
    st.session_state.simulation_running = False

# Sidebar
st.sidebar.title("🏘️ Toplumsal Mikrokozmos")
st.sidebar.markdown("---")

# Character selection
try:
    character_names = character_service.get_character_names()
    logger.info(f"Bulunan karakterler: {character_names}")
    selected_characters = st.sidebar.multiselect(
        "Karakterleri Seçin",
        character_names,
        default=character_names[:3] if len(character_names) >= 3 else character_names
    )
except Exception as e:
    logger.error(f"Karakter seçimi hatası: {str(e)}")
    st.error(f"Karakter seçimi hatası: {str(e)}")
    st.stop()

# Gündem input
st.sidebar.markdown("---")
gundem = st.sidebar.text_area("Gündemi Girin", height=100)

# Aktivite seçimi
st.sidebar.markdown("---")
aktivite = st.sidebar.selectbox(
    "Aktivite Seçin",
    ["TV İzle", "Pazara Git", "Kahvede Otur", "Alışverişe Çık", "Camide Buluş"]
)

# Main content
st.title("🏘️ Toplumsal Mikrokozmos")
st.markdown("""
Bu simülasyon, Türkiye'nin toplumsal ve siyasi dinamiklerini yapay zeka destekli karakterler aracılığıyla 
sanal bir köy ortamında simüle etmeyi amaçlamaktadır.
""")

# Simülasyon kontrol butonları
col1, col2 = st.columns(2)
with col1:
    if not st.session_state.simulation_running:
        if st.button("▶️ Simülasyonu Başlat", type="primary"):
            st.session_state.simulation_running = True
            logger.info("Simülasyon başlatıldı.")
            st.rerun()
with col2:
    if st.session_state.simulation_running:
        if st.button("⏹️ Simülasyonu Durdur", type="secondary"):
            st.session_state.simulation_running = False
            logger.info("Simülasyon durduruldu.")
            st.rerun()

# Simülasyon durumu göstergesi
status_color = "green" if st.session_state.simulation_running else "red"
status_text = "Çalışıyor" if st.session_state.simulation_running else "Durduruldu"
st.markdown(f"<p style='color:{status_color};'>Simülasyon Durumu: {status_text}</p>", unsafe_allow_html=True)

# Simülasyon çalışıyorsa etkileşimleri göster
if st.session_state.simulation_running and selected_characters and gundem:
    try:
        # Ekonomik verileri al
        logger.info("Ekonomik veriler alınıyor...")
        economic_context = mcp_service.get_economic_context()
        logger.info(f"Ekonomik veriler alındı: {economic_context[:100]}...")

        # Create columns for characters
        cols = st.columns(len(selected_characters))

        # Display character interactions
        st.markdown("### Gündem Tepkileri")
        for char_name in selected_characters:
            try:
                logger.info(f"{char_name} karakteri yükleniyor...")
                character = character_service.get_character(char_name)
                with st.expander(f"{char_name}'in Tepkisi"):
                    response = character.react_to_event(f"{gundem}\n\n{economic_context}")
                    st.write(response)
                logger.info(f"{char_name} tepkisi başarıyla oluşturuldu.")
            except Exception as e:
                logger.error(f"{char_name} karakteri işlenirken hata: {str(e)}")
                st.error(f"{char_name} karakteri işlenirken hata oluştu: {str(e)}")

        # Display character activities
        if aktivite:
            st.markdown("### Aktivite Etkileşimleri")
            for i, char_name in enumerate(selected_characters):
                try:
                    character = character_service.get_character(char_name)
                    with cols[i]:
                        st.markdown(f"#### {char_name}")
                        response = character.get_response(
                            context=f"Şu anda {aktivite} aktivitesini yapıyorsun. Gündemdeki konu: {gundem}\n\n{economic_context}",
                            prompt=f"{aktivite} sırasında gündemdeki '{gundem}' konusu ve güncel ekonomik durum hakkında ne düşünüyorsun ve ne yapıyorsun?"
                        )
                        st.write(response)
                    logger.info(f"{char_name} aktivite tepkisi başarıyla oluşturuldu.")
                except Exception as e:
                    logger.error(f"{char_name} aktivite işlenirken hata: {str(e)}")
                    st.error(f"{char_name} aktivite işlenirken hata oluştu: {str(e)}")

        # Character interactions
        if len(selected_characters) >= 2:
            st.markdown("### Karakter Etkileşimleri")
            for i, char1_name in enumerate(selected_characters):
                for j, char2_name in enumerate(selected_characters[i+1:], i+1):
                    try:
                        char1 = character_service.get_character(char1_name)
                        char2 = character_service.get_character(char2_name)
                        
                        with st.expander(f"{char1_name} ve {char2_name} Arasındaki Konuşma"):
                            response1 = char1.interact_with(char2, f"{gundem}\n\n{economic_context}")
                            st.write(f"{char1_name}: {response1}")
                            
                            response2 = char2.interact_with(char1, f"{gundem}\n\n{economic_context}")
                            st.write(f"{char2_name}: {response2}")
                        logger.info(f"{char1_name} ve {char2_name} arasındaki etkileşim başarıyla oluşturuldu.")
                    except Exception as e:
                        logger.error(f"{char1_name} ve {char2_name} etkileşimi sırasında hata: {str(e)}")
                        st.error(f"{char1_name} ve {char2_name} etkileşimi sırasında hata oluştu: {str(e)}")

    except Exception as e:
        logger.error(f"Simülasyon çalıştırılırken hata: {str(e)}")
        st.error(f"Simülasyon çalıştırılırken bir hata oluştu: {str(e)}")
else:
    if not st.session_state.simulation_running:
        st.info("Simülasyonu başlatmak için yukarıdaki 'Simülasyonu Başlat' butonuna tıklayın.")
    elif not selected_characters:
        st.warning("Lütfen en az bir karakter seçin.")
    elif not gundem:
        st.warning("Lütfen bir gündem konusu girin.") 