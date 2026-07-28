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
        .social-btn {
            display: inline-block;
            padding: 0.5rem 1rem;
            margin: 0.2rem;
            border-radius: 5px;
            color: white;
            text-decoration: none;
            font-weight: bold;
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
    """
* 🔴 [YouTube 頻道](#)
* 📸 [Instagram (IG)](#)
* 🔵 [Facebook 專頁](#)
* 🧵 [Threads](#)
* 🎵 [抖音 (TikTok)](#)
* 📺 [Bilibili 嗶哩嗶哩](#)
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
        st.link_button("🔴 YouTube", "https://www.youtube.com")
    with col_s2:
        st.link_button("📸 Instagram", "https://www.instagram.com")
    with col_s3:
        st.link_button("🔵 Facebook", "https://www.facebook.com")
    with col_s4:
        st.link_button("🧵 Threads", "https://www.threads.net")
    with col_s5:
        st.link_button("🎵 抖音", "https://www.douyin.com")
    with col_s6:
        st.link_button("📺 Bilibili", "https://www.bilibili.com")

    st.markdown("---")

    col1, col2 = st.columns([2, 1])

    with col1:
        st.subheader("🔥 最新熱門推介")
        st.video(
            "https://www.youtube.com/watch?v=dQw4w9WgXcQ"
        )  # 可替換為實際 YouTube / Bilibili 影片連結
        st.markdown(
            "**【濠江英才九九頻道】最新作品發表**\n\n歡迎追蹤我們的社交平台並訂閱頻道，第一時間獲取最新動態！"
        )

    with col2:
        st.subheader("📊 頻道速覽")
        st.metric(label="社群關注總數", value="15,000+", delta="+500 本週")
        st.metric(label="Minecraft 檔案下載量", value="3,200+", delta="+180 本週")

        st.info(
            "💡 **提示**：點擊左側選單可前往「**Minecraft HKP 下載區**」取得最新地圖與模組檔案！"
        )

elif menu == "🎮 Minecraft HKP 下載區":
    st.title("🎮 Minecraft HKP 專屬下載區")
    st.write(
        "歡迎來到 Minecraft HKP 下載專區！同學們可以在這裡下載由九九頻道團隊或同學製作的 Minecraft 地圖、材質包與模組資源。"
    )

    st.markdown("---")

    tab1, tab2, tab3 = st.tabs(
        ["🗺️ 專案地圖下載", "🧩 模組與材質包", "📖 安裝與使用教學"]
    )

    with tab1:
        st.subheader("🗺️ 濠江英才校園 Minecraft 地圖與冒險關卡")

        col_mc1, col_mc2 = st.columns(2)

        with col_mc1:
            st.markdown(
                """
            <div class="mc-card">
                <h3>🏫 濠江英才校園 1:1 還原地圖 (v1.2)</h3>
                <p><b>適用版本：</b>Java 版 1.20.1+</p>
                <p><b>檔案大小：</b>45 MB</p>
                <p><b>簡介：</b>精心打造的校園建築再現，包含教學樓、禮堂與運動場，歡迎同學們下載探索！</p>
            </div>
            """,
                unsafe_allow_html=True,
            )
            # 範例下載按鈕（可放置實際檔案連結或雲端硬碟網址）
            st.download_button(
                label="⬇️ 下載校園地圖 (.zip)",
                data=b"Minecraft HKP Campus Map Dummy Content",
                file_name="Minecraft_HKP_Campus_v1.2.zip",
                mime="application/zip",
            )
            st.link_button(
                "🔗 備用雲端下載 (Google Drive / 網盤)", "https://drive.google.com"
            )

        with col_mc2:
            st.markdown(
                """
            <div class="mc-card">
                <h3>⚔️ HKP 99 闖關冒險地圖 Vol.1</h3>
                <p><b>適用版本：</b>Java / 基岩版 (Bedrock)</p>
                <p><b>檔案大小：</b>28 MB</p>
                <p><b>簡介：</b>含有解謎與跑酷元素的特色地圖，適合單人或多合同學一起挑戰！</p>
            </div>
            """,
                unsafe_allow_html=True,
            )
            st.download_button(
                label="⬇️ 下載冒險地圖 (.mcworld)",
                data=b"Minecraft HKP Adventure Map Dummy Content",
                file_name="HKP_Adventure_Vol1.mcworld",
                mime="application/octet-stream",
            )
            st.link_button(
                "🔗 備用雲端下載 (Google Drive / 網盤)", "https://drive.google.com"
            )

    with tab2:
        st.subheader("🧩 專屬資源包與模組組件")

        st.markdown(
            """
        * **校園專屬校服皮膚包 (Skin Pack)**
            * 提供濠江英才校服風格的玩家皮膚！
            * [⬇️ 下載皮膚包 (.zip)](#)
        * **HKP 99 頻道光影與材質建議包**
            * 提升畫面品質，呈現最佳校園場景效果。
            * [⬇️ 下載材質包 (.zip)](#)
        """
        )

    with tab3:
        st.subheader("📖 檔案安裝指引")
        st.markdown(
            """
        1. **Java 版地圖安裝步驟**：
           - 下載 `.zip` 檔案並解壓縮。
           - 按下 `Win + R` 鍵，輸入 `%appdata%\\.minecraft\\saves` 並按下 Enter。
           - 將解壓後的資料夾複製到 `saves` 資料夾中即可。
        2. **基岩版 (Bedrock / 手機版 / Windows 10) 安裝步驟**：
           - 直接點擊下載的 `.mcworld` 檔案，遊戲將自動啟動並匯入地圖。
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
            "title": "九九頻道短影音精選 (抖音/Threads 特輯)",
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
        """
    <div class="card">
        <h4>🎮 Minecraft HKP 地圖 v1.2 正式開放下載！</h4>
        <p>校園地圖已更新至 1.2 版本，修復了部分建築細節並增加了互動元素，歡迎前往下載區體驗。</p>
    </div>
    <div class="card">
        <h4>📱 官方社群平台全線開通</h4>
        <p>九九頻道現已同步進駐 YouTube、IG、Facebook、Threads、抖音及 Bilibili，歡迎大家點擊關注！</p>
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
    - **社群媒體整合**：網羅 YouTube、IG、FB、Threads、抖音及 Bilibili 等主流平台。
    - **資源下載驗證**：Minecraft 專區支援直接檔下載（`.zip`, `.mcworld`）與外部備用雲端連結。
    - **時區機制驗證**：系統整合 `pytz` 時區庫，精確顯示澳門當地時間 (`Asia/Macau`)。
    """
    )

    st.divider()
    st.info(f"**最後更新日期時間 (Last Updated)**：{current_time_str}")

# 4. 頁腳 (Footer)
st.markdown("---")
st.markdown(
    f'<div class="footer-text">© 2026 濠江英才九九頻道 (HKP 99 Channel) | Powered by Streamlit | 最後更新：{current_time_str}</div>',
    unsafe_allow_html=True,
)
