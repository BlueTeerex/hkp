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

# 核心連結設定
DRIVE_MINECRAFT_URL = "https://drive.google.com/drive/folders/1bikY29LxzVjKP5pFBPZpoK_l9OBvZz7P?usp=drive_link"
IG_URL = "https://www.instagram.com/hkp_99channel/"


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
            padding: 1.2rem;
            margin-bottom: 1rem;
            border-left: 4px solid #1E88E5;
        }
        .mc-card {
            background-color: #f1f8e9;
            border-radius: 10px;
            padding: 1.2rem;
            margin-bottom: 1rem;
            border-left: 4px solid #4CAF50;
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
st.sidebar.image(
    "https://via.placeholder.com/150x150.png?text=HKP+99", width=120
)
st.sidebar.title("濠江英才九九頻道")
st.sidebar.caption("HKP 99 Channel 官方網站")
st.sidebar.markdown("---")

menu = st.sidebar.radio(
    "導航選單",
    [
        "🏠 頻道首頁",
        "🎮 Minecraft HKP 下載區",
        "📹 節目影片",
        "📢 頻道公告",
        "💬 觀眾互動區",
        "⚙️ 開發背景與系統資訊",
    ],
)

st.sidebar.markdown("---")
st.sidebar.subheader("🌐 關注九九頻道")
st.sidebar.markdown(
    f"""
* 📸 [Instagram (@hkp_99channel)]({IG_URL})
* 🔴 [YouTube 頻道](https://www.youtube.com)
* 🔵 [Facebook 專頁](https://www.facebook.com)
* 🧵 [Threads](https://www.threads.net/@hkp_99channel)
* 🎵 [抖音 (TikTok)](https://www.douyin.com)
* 📺 [Bilibili 嗶哩嗶哩](https://www.bilibili.com)
"""
)

st.sidebar.markdown("---")
st.sidebar.caption(f"🕒 **系統時間**: {current_time_str}")

# 3. 各頁面邏輯 implementation

if menu == "🏠 頻道首頁":
    st.markdown(
        '<div class="main-header">歡迎來到 濠江英才九九頻道 (HKP 99 Channel)</div>',
        unsafe_allow_html=True,
    )
    st.markdown(
        '<div class="sub-header">匯聚最新頻道資訊、校園創作、Minecraft HKP 專案與社交平台動態</div>',
        unsafe_allow_html=True,
    )

    # 社交媒體快速入口
    st.subheader("🔗 官方社交媒體平台")
    col_s1, col_s2, col_s3, col_s4, col_s5, col_s6 = st.columns(6)
    with col_s1:
        st.link_button("📸 Instagram", IG_URL)
    with col_s2:
        st.link_button("🔴 YouTube", "https://www.youtube.com")
    with col_s3:
        st.link_button("🔵 Facebook", "https://www.facebook.com")
    with col_s4:
        st.link_button("🧵 Threads", "https://www.threads.net/@hkp_99channel")
    with col_s5:
        st.link_button("🎵 抖音", "https://www.douyin.com")
    with col_s6:
        st.link_button("📺 Bilibili", "https://www.bilibili.com")

    st.markdown("---")

    col1, col2 = st.columns([2, 1])

    with col1:
        st.subheader("🔥 最新熱門推介")
        st.video("https://www.youtube.com/watch?v=dQw4w9WgXcQ")
        st.markdown(
            "**【濠江英才九九頻道】最新作品發表**\n\n歡迎追蹤我們的 Instagram [@hkp_99channel](https://www.instagram.com/hkp_99channel/)，第一時間獲取最新動態與花絮！"
        )

    with col2:
        st.subheader("📊 頻道速覽")
        st.metric(label="Instagram 帳號", value="@hkp_99channel")
        st.metric(label="Minecraft 資源", value="開放下載中")

        st.info(
            "💡 **提示**：點擊左側選單可前往「**Minecraft HKP 下載區**」取得最新的 Google Drive 地圖與模組檔案！"
        )

elif menu == "🎮 Minecraft HKP 下載區":
    st.title("🎮 Minecraft HKP 專屬下載區")
    st.write(
        "歡迎來到 Minecraft HKP 下載專區！同學們可以直接前往官方 Google Drive 雲端資料夾取得所有最新地圖、材質包與模組資源。"
    )

    st.markdown("---")

    # 主要 Google Drive 下載入口卡片
    st.markdown(
        """
    <div class="mc-card">
        <h3>📂 濠江英才九九頻道 Minecraft 雲端資料夾</h3>
        <p>包含校園地圖、冒險關卡、專屬皮膚與材質包，點擊下方按鈕即可開啟 Google Drive 進行下載！</p>
    </div>
    """,
        unsafe_allow_html=True,
    )

    col_dl1, col_dl2 = st.columns([1, 2])
    with col_dl1:
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
        你在雲端資料夾中可以找到以下內容：
        * **🏫 濠江英才校園地圖檔案** (`.zip` / `.mcworld`)
        * **⚔️ 冒險地圖與闖關關卡**
        * **👕 專屬皮膚包與材質包資源**
        * **🧩 相容模組組件**

        👉 [點我直接開啟 Google Drive 資料夾]({DRIVE_MINECRAFT_URL})
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

elif menu == "📹 節目影片":
    st.title("📹 節目與影片作品")
    st.write("探索濠江英才九九 Channel 的所有原創影片、節目與剪輯。")

    search_query = st.text_input("🔍 搜尋影片標題或關鍵字", "")

    videos = [
        {
            "title": "【濠江英才】九九頻道特別報導 Vol.1",
            "category": "校園專題",
            "date": "2026-07-20",
            "desc": "帶你直擊校園大小事與學生創作精華。",
        },
        {
            "title": "Minecraft HKP 校園地圖製作紀錄片",
            "category": "遊戲專題",
            "date": "2026-07-15",
            "desc": "幕後花絮：同學們是如何在 Minecraft 中建造我們的校園？",
        },
        {
            "title": "九九頻道短影音精選 (IG Reels / Threads 特輯)",
            "category": "短影音",
            "date": "2026-07-01",
            "desc": "匯集短影音平台熱門內容與爆笑花絮。",
        },
    ]

    filtered_videos = [
        v for v in videos if search_query.lower() in v["title"].lower()
    ]

    for v in filtered_videos:
        with st.container():
            st.markdown(f"### {v['title']}")
            st.caption(f"分類：{v['category']} | 發布日期：{v['date']}")
            st.write(v["desc"])
            st.button(f"觀看 《{v['title']}》", key=v["title"])
            st.markdown("---")

elif menu == "📢 頻道公告":
    st.title("📢 最新公告與活動行程")

    st.markdown(
        f"""
    <div class="card">
        <h4>🎮 Minecraft HKP 雲端資料夾已全面開放！</h4>
        <p>同學們現在可以直接透過 <a href="{DRIVE_MINECRAFT_URL}" target="_blank">Google Drive 雲端連結</a> 下載最新校園地圖與資源。</p>
    </div>
    <div class="card">
        <h4>📸 Instagram 官方帳號開啟！</h4>
        <p>歡迎追蹤 <a href="{IG_URL}" target="_blank">@hkp_99channel</a>，即時獲取頻道限時動態與最新消息！</p>
    </div>
    """,
        unsafe_allow_html=True,
    )

elif menu == "💬 觀眾互動區":
    st.title("💬 同學與觀眾留言區")
    st.write("對頻道節目或 Minecraft 地圖有什麼建議？歡迎在此留言給我們！")

    with st.form("feedback_form", clear_on_submit=True):
        user_name = st.text_input("班級與暱稱 / Name")
        message = st.text_area("留言或建議內容 / Message")
        submitted = st.form_submit_button("提交留言")

        if submitted:
            if user_name and message:
                st.success(f"感謝 {user_name} 的留言！團隊會認真閱讀你的建議。")
            else:
                st.warning("請填寫暱稱與留言內容。")

elif menu == "⚙️ 開發背景與系統資訊":
    st.title("⚙️ 開發背景與驗證資訊")

    st.markdown(
        """
    ### 🎯 開發背景 (Development Background)
    濠江英才九九頻道 (HKP 99 Channel) 官方網站旨在為師生及觀眾提供一個整合頻道節目、社群媒體動態以及校園創作資源（如 Minecraft 專案下載）的跨平台展示基地。

    ### 🛡️ 準確性與穩定性驗證 (Accuracy Validation)
    - **社群媒體整合**：已綁定官方 Instagram (`@hkp_99channel`)。
    - **資源下載驗證**：已將「Minecraft HKP 下載區」直連至官方 Google Drive 共享資料夾。
    - **時區機制驗證**：系統整合 `pytz` 時區庫，精確顯示澳門當地時間 (`Asia/Macau`)。
    """
    )

    st.divider()
    st.info(f"**最後更新日期時間 (Last Updated)**：{current_time_str}")

# 4. 頁腳 (Footer)
st.markdown("---")
st.markdown(
    f'<div class="footer-text">© 2026 濠江英才九九頻道 (HKP 99 Channel) | Instagram: @hkp_99channel | Powered by Streamlit | 最後更新：{current_time_str}</div>',
    unsafe_allow_html=True,
)
