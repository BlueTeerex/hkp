from datetime import datetime
import pytz
import streamlit as st

# 1. 頁面基本配置
st.set_page_config(
    page_title="濠江英才九九頻道 (HKP 99 Channel)",
    page_icon="📺",
    layout="wide",
    initial_sidebar_state="expanded",
)

# 時區設定（Macao / Asia/Macau）
user_tz = pytz.timezone("Asia/Macau")
current_time_str = datetime.now(user_tz).strftime("%Y-%m-%d %H:%M:%S (%Z)")

# 核心連結設定 (@hkp_99channel)
DRIVE_MINECRAFT_URL = "https://drive.google.com/drive/folders/1bikY29LxzVjKP5pFBPZpoK_l9OBvZz7P?usp=drive_link"
IG_URL = "https://www.instagram.com/hkp_99channel/"
YT_URL = "https://www.youtube.com/@hkp_99channel"
THREADS_URL = "https://www.threads.net/@hkp_99channel"
BILIBILI_URL = "https://space.bilibili.com"  # 可在後續替換為精確UID空間頁


# 自訂 CSS 樣式
def inject_custom_css():
    st.markdown(
        """
        <style>
        .main-header {
            font-size: 2.2rem;
            font-weight: 700;
            color: #1E88E5;
            margin-bottom: 0.2rem;
        }
        .sub-header {
            font-size: 1.1rem;
            color: #555555;
            margin-bottom: 1.5rem;
        }
        .card {
            background-color: #f8f9fa;
            border-radius: 10px;
            padding: 1.5rem;
            margin-bottom: 1.2rem;
            border-left: 5px solid #1E88E5;
        }
        .mc-card {
            background-color: #f1f8e9;
            border-radius: 10px;
            padding: 1.5rem;
            margin-bottom: 1.2rem;
            border-left: 5px solid #4CAF50;
        }
        .footer-text {
            font-size: 0.85rem;
            color: #888888;
            text-align: center;
            margin-top: 3rem;
        }
        </style>
    """,
        unsafe_allow_html=True,
    )


inject_custom_css()

# 2. 側邊欄導航與社交媒體連結
st.sidebar.title("濠江英才九九頻道")
st.sidebar.caption("HKP 99 Channel 官方網站")
st.sidebar.markdown("---")

# 僅保留兩個分頁
menu = st.sidebar.radio("📌 導航選單", ["🏠 主頁", "🎮 Minecraft HKP"])

st.sidebar.markdown("---")
st.sidebar.subheader("🌐 關注九九頻道 (@hkp_99channel)")
st.sidebar.markdown(
    f"""
* 🔴 [YouTube 頻道]({YT_URL})
* 📸 [Instagram]({IG_URL})
* 🧵 [Threads]({THREADS_URL})
* 📺 [Bilibili 嗶哩嗶哩]({BILIBILI_URL})
"""
)

st.sidebar.markdown("---")
st.sidebar.caption(f"🕒 **系統時間**: {current_time_str}")

# 3. 各頁面邏輯 implementation

if menu == "🏠 主頁":
    st.markdown(
        '<div class="main-header">歡迎來到 濠江英才九九頻道 (HKP 99 Channel)</div>',
        unsafe_allow_html=True,
    )
    st.markdown(
        '<div class="sub-header">匯聚最新頻道資訊、社群平台動態與 Minecraft HKP 校園專案</div>',
        unsafe_allow_html=True,
    )

    # 官方社交媒體快速入口
    st.subheader("🔗 官方社群平台直接連結")
    col_s1, col_s2, col_s3, col_s4 = st.columns(4)
    with col_s1:
        st.link_button(
            "🔴 YouTube (@hkp_99channel)", YT_URL, use_container_width=True
        )
    with col_s2:
        st.link_button(
            "📸 Instagram (@hkp_99channel)", IG_URL, use_container_width=True
        )
    with col_s3:
        st.link_button(
            "🧵 Threads (@hkp_99channel)",
            THREADS_URL,
            use_container_width=True,
        )
    with col_s4:
        st.link_button(
            "📺 Bilibili 嗶哩嗶哩", BILIBILI_URL, use_container_width=True
        )

    st.markdown("---")

    # 頻道簡介與快速捷徑
    col1, col2 = st.columns([2, 1])

    with col1:
        st.markdown(
            """
        <div class="card">
            <h3>📢 關於 濠江英才九九頻道</h3>
            <p>我們是由濠江英才學生團隊營運的創作頻道！在這裡你會看到校園生活、創作專題、短影音以及同學們聯手打造的 <b>Minecraft HKP 校園建築與冒險地圖專案</b>。</p>
            <p>歡迎追蹤我們的社群平台 <b>@hkp_99channel</b>，鎖定最新動態！</p>
        </div>
        """,
            unsafe_allow_html=True,
        )

    with col2:
        st.markdown(
            """
        <div class="mc-card">
            <h3>🎮 Minecraft 下載捷徑</h3>
            <p>想遊玩濠江英才校園地圖或下載專屬資源？</p>
        </div>
        """,
            unsafe_allow_html=True,
        )
        st.link_button(
            "🚀 開啟 Google Drive 雲端下載庫",
            DRIVE_MINECRAFT_URL,
            type="primary",
            use_container_width=True,
        )

elif menu == "🎮 Minecraft HKP":
    st.title("🎮 Minecraft HKP 專屬下載區")
    st.write(
        "歡迎來到 Minecraft HKP 專區！同學們可以直接開啟 Google Drive 雲端資料夾取得所有最新的校園地圖、材質包與模組資源。"
    )

    st.markdown("---")

    # 主要 Google Drive 下載入口卡片
    st.markdown(
        """
    <div class="mc-card">
        <h3>📂 濠江英才九九頻道 Minecraft 雲端資料夾</h3>
        <p>包含校園 1:1 還原地圖、冒險關卡、專屬皮膚與材質包，點擊下方按鈕即可開啟 Google Drive 雲端硬碟直接下載！</p>
    </div>
    """,
        unsafe_allow_html=True,
    )

    st.link_button(
        "🚀 前往 Google Drive 資源下載庫",
        DRIVE_MINECRAFT_URL,
        type="primary",
        use_container_width=True,
    )

    st.markdown("---")

    tab1, tab2 = st.tabs(["📦 雲端資源說明", "📖 安裝與使用教學"])

    with tab1:
        st.subheader("🗺️ 資料夾現有資源項目")
        st.markdown(
            f"""
        在 Google Drive 資料夾中包含以下檔案資源：
        * **🏫 濠江英才校園地圖檔案** (`.zip` / `.mcworld`)
        * **⚔️ 冒險地圖與闖關關卡**
        * **👕 專屬皮膚包與材質包資源**
        * **🧩 支援組件與模組**

        👉 [點我開啟 Google Drive 雲端資料夾]({DRIVE_MINECRAFT_URL})
        """
        )

    with tab2:
        st.subheader("📖 檔案安裝指引")
        st.markdown(
            """
        1. **Java 版地圖安裝步驟**：
           - 從 Google Drive 下載 `.zip` 檔案並解壓縮。
           - 按下 `Win + R` 鍵，輸入 `%appdata%\\.minecraft\\saves` 並按下 Enter。
           - 將解壓後的資料夾複製到 `saves` 資料夾中即可。
        2. **基岩版 (Bedrock / 手機版 / Windows 10) 安裝步驟**：
           - 下載 `.mcworld` 檔案後直接點擊，遊戲將自動啟動並匯入地圖。
        """
        )

# 4. 頁腳 (Footer)
st.markdown("---")
st.markdown(
    f'<div class="footer-text">© 2026 濠江英才九九頻道 (HKP 99 Channel) | Instagram & YouTube: @hkp_99channel | Powered by Streamlit | 最後更新：{current_time_str}</div>',
    unsafe_allow_html=True,
)
