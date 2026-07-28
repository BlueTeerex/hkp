from datetime import datetime
import pytz
import streamlit as st
import streamlit.components.v1 as components

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

# 核心連結與 Google Drive 設定
GDRIVE_FOLDER_ID = "1bikY29LxzVjKP5pFBPZpoK_l9OBvZz7P"
GDRIVE_DIRECT_URL = f"https://drive.google.com/drive/folders/{GDRIVE_FOLDER_ID}?usp=drive_link"
GDRIVE_EMBED_URL = (
    f"https://drive.google.com/embeddedfolderview?id={GDRIVE_FOLDER_ID}#grid"
)

# 社群連結 (@hkp_99channel)
IG_URL = "https://www.instagram.com/hkp_99channel/"
YT_URL = "https://www.youtube.com/@hkp_99channel"
THREADS_URL = "https://www.threads.net/@hkp_99channel"
BILIBILI_URL = "https://space.bilibili.com"

# 頭像圖片路徑（預設為質感預設圖，若在 GitHub 上傳 avatar.png 可直接替換）
AVATAR_IMAGE = "https://api.dicebear.com/7.x/bottts/svg?seed=HKP99Channel"


# 2. 高級 UI 美化 CSS
def inject_custom_css():
    st.markdown(
        """
        <style>
        /* 全局字體與背景美化 */
        .main {
            background-color: #fafafa;
        }
        
        /* 頂部 Header Banner */
        .header-container {
            display: flex;
            align-items: center;
            background: linear-gradient(135deg, #1E88E5 0%, #1565C0 100%);
            padding: 1.8rem 2rem;
            border-radius: 16px;
            color: white;
            box-shadow: 0 8px 20px rgba(30, 136, 229, 0.25);
            margin-bottom: 2rem;
        }
        .header-avatar {
            width: 90px;
            height: 90px;
            border-radius: 50%;
            border: 3px solid rgba(255, 255, 255, 0.8);
            margin-right: 1.5rem;
            object-fit: cover;
            background-color: white;
        }
        .header-title {
            font-size: 2.2rem;
            font-weight: 800;
            margin: 0;
            letter-spacing: 0.5px;
        }
        .header-subtitle {
            font-size: 1.05rem;
            opacity: 0.9;
            margin-top: 0.3rem;
        }

        /* 卡片元件設計 */
        .custom-card {
            background-color: #ffffff;
            border-radius: 12px;
            padding: 1.5rem;
            margin-bottom: 1.2rem;
            border: 1px solid #e0e0e0;
            box-shadow: 0 4px 12px rgba(0,0,0,0.04);
            transition: transform 0.2s ease, box-shadow 0.2s ease;
        }
        .custom-card:hover {
            box-shadow: 0 6px 16px rgba(0,0,0,0.08);
        }
        
        /* Minecraft 專用主題卡片 */
        .mc-theme-card {
            background: linear-gradient(135deg, #f1f8e9 0%, #dedef0 100%);
            border-radius: 12px;
            padding: 1.5rem;
            margin-bottom: 1.2rem;
            border-left: 6px solid #4CAF50;
            box-shadow: 0 4px 12px rgba(76, 175, 80, 0.12);
        }

        /* 頁腳文字 */
        .footer-text {
            font-size: 0.85rem;
            color: #757575;
            text-align: center;
            margin-top: 3rem;
            padding-top: 1rem;
            border-top: 1px solid #e0e0e0;
        }
        </style>
    """,
        unsafe_allow_html=True,
    )


inject_custom_css()

# 3. 側邊欄設計 (Sidebar)
with st.sidebar:
    # 顯示頭像與頻道名稱
    col_av1, col_av2 = st.columns([1, 2])
    with col_av1:
        st.image(AVATAR_IMAGE, width=70)
    with col_av2:
        st.markdown("**濠江英才九九頻道**")
        st.caption("@hkp_99channel")

    st.markdown("---")

    # 僅保留兩頁分頁
    menu = st.radio("📌 導航選單", ["🏠 主頁", "🎮 Minecraft HKP"])

    st.markdown("---")
    st.markdown("### 🌐 關注我們")
    st.markdown(
        f"""
    * 🔴 [YouTube 頻道]({YT_URL})
    * 📸 [Instagram]({IG_URL})
    * 🧵 [Threads]({THREADS_URL})
    * 📺 [Bilibili 嗶哩嗶哩]({BILIBILI_URL})
    """
    )

    st.markdown("---")
    st.caption(f"🕒 **系統時間**: {current_time_str}")

# 4. 主頁面內容

if menu == "🏠 主頁":
    # 頂部大 Banner（含頭像與名稱）
    st.markdown(
        f"""
    <div class="header-container">
        <img src="{AVATAR_IMAGE}" class="header-avatar">
        <div>
            <div class="header-title">濠江英才九九頻道</div>
            <div class="header-subtitle">HKP 99 Channel 官方網站 | 校園創作與 Minecraft 專案展示基地</div>
        </div>
    </div>
    """,
        unsafe_allow_html=True,
    )

    # 官方社群平台快速連結
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

    col1, col2 = st.columns([2, 1])

    with col1:
        st.markdown(
            """
        <div class="custom-card">
            <h3>📢 關於 濠江英才九九頻道</h3>
            <p>我們是由濠江英才學生團隊營運的創作頻道！在這裡你會看到校園生活、創作專題、短影音以及同學們聯手打造的 <b>Minecraft HKP 校園建築與冒險地圖專案</b>。</p>
            <p>歡迎關注我們的各大社群平台 <b>@hkp_99channel</b>，鎖定第一手消息！</p>
        </div>
        """,
            unsafe_allow_html=True,
        )

    with col2:
        st.markdown(
            """
        <div class="mc-theme-card">
            <h3>🎮 Minecraft HKP</h3>
            <p>想下載濠江英才 1:1 校園地圖或地圖組件？</p>
        </div>
        """,
            unsafe_allow_html=True,
        )
        st.link_button(
            "🚀 前往 Minecraft 下載區",
            GDRIVE_DIRECT_URL,
            type="primary",
            use_container_width=True,
        )

elif menu == "🎮 Minecraft HKP":
    st.title("🎮 Minecraft HKP 專屬下載區")
    st.write(
        "歡迎來到 Minecraft HKP 專區！以下已直接嵌入頻道官方 Google Drive 雲端資料夾，你可以直接在此瀏覽並下載最新的地圖與檔案。"
    )

    st.markdown("---")

    # 內嵌 Google Drive 檔案瀏覽器
    st.subheader("📂 雲端資料夾即時預覽與下載")

    # 使用 iframe 嵌入 Google Drive 資料夾
    st.markdown(
        f"""
    <div style="border: 2px solid #4CAF50; border-radius: 12px; overflow: hidden; box-shadow: 0 4px 12px rgba(0,0,0,0.1);">
        <iframe src="{GDRIVE_EMBED_URL}" width="100%" height="550" frameborder="0"></iframe>
    </div>
    """,
        unsafe_allow_html=True,
    )

    st.write("")
    # 備用跳轉按鈕
    st.link_button(
        "↗️ 在新頁面開啟 Google Drive 雲端硬碟",
        GDRIVE_DIRECT_URL,
        type="primary",
        use_container_width=True,
    )

    st.markdown("---")

    tab1, tab2 = st.tabs(["📦 雲端資源說明", "📖 安裝與使用教學"])

    with tab1:
        st.subheader("🗺️ 資料夾現有資源項目")
        st.markdown(
            f"""
        在上方雲端資料夾中包含以下檔案資源：
        * **🏫 濠江英才校園地圖檔案** (`.zip` / `.mcworld`)
        * **⚔️ 冒險地圖與闖關關卡**
        * **👕 專屬皮膚包與材質包資源**
        * **🧩 支援組件與模組**
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

# 5. 頁腳 (Footer)
st.markdown(
    f'<div class="footer-text">© 2026 濠江英才九九頻道 (HKP 99 Channel) | Instagram & YouTube: @hkp_99channel | Powered by Streamlit | 最後更新：{current_time_str}</div>',
    unsafe_allow_html=True,
)
