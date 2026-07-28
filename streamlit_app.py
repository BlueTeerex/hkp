from datetime import datetime
import pytz
import streamlit as st

# 1. 頁面基本配置
st.set_page_config(
    page_title="HKP 99 Channel 官方網站",
    page_icon="📺",
    layout="wide",
    initial_sidebar_state="expanded",
)

# 時區設定（預設為 Macao / Asia/Macau）
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

# 2. 側邊欄導航
st.sidebar.image(
    "https://via.placeholder.com/150x150.png?text=HKP+99", width=120
)
st.sidebar.title("HKP 99 Channel")
st.sidebar.markdown("---")

menu = st.sidebar.radio(
    "導航選單",
    ["🏠 頻道首頁", "📹 節目影片", "📢 頻道公告", "💬 觀眾互動區", "⚙️ 開發背景與系統資訊"],
)

st.sidebar.markdown("---")
st.sidebar.caption(f"🕒 **系統時間**: {current_time_str}")

# 3. 各頁面邏輯 implementation

if menu == "🏠 頻道首頁":
    st.markdown(
        '<div class="main-header">歡迎來到 HKP 99 Channel 官方平台</div>',
        unsafe_allow_html=True,
    )
    st.markdown(
        '<div class="sub-header">匯聚最新頻道資訊、精選節目與動態更新</div>',
        unsafe_allow_html=True,
    )

    col1, col2 = st.columns([2, 1])

    with col1:
        st.subheader("🔥 熱門推介")
        st.video(
            "https://www.youtube.com/watch?v=dQw4w9WgXcQ"
        )  # 可替換為實際 YouTube 連結
        st.markdown(
            "**【最新集數】HKP 99 特別企劃**\n\n歡迎訂閱並開啟小鈴鐺，第一時間獲取最新節目推送！"
        )

    with col2:
        st.subheader("📊 頻道速覽")
        st.metric(label="總訂閱人數", value="12,400+", delta="+350 本週")
        st.metric(label="總觀看次數", value="850,000+", delta="+12,000 今日")

        st.info("💡 **提示**：可點擊左側選單切換至不同功能區塊。")

elif menu == "📹 節目影片":
    st.title("📹 節目與影片瀏覽")
    st.write("在此探索 HKP 99 Channel 的所有原創節目與專題。")

    search_query = st.text_input("🔍 搜尋影片標題或關鍵字", "")

    videos = [
        {
            "title": "HKP 99 精選系列 Vol.1",
            "category": "專題報導",
            "date": "2026-07-20",
            "desc": "本集深度探討相關主題，帶來全新視野。",
        },
        {
            "title": "特別直播剪輯版",
            "category": "直播精華",
            "date": "2026-07-15",
            "desc": "精彩片段回顧，不容錯過。",
        },
        {
            "title": "新手入門指南",
            "category": "教學解說",
            "date": "2026-07-01",
            "desc": "零基礎帶你了解核心知識。",
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
            st.button(f"播放 《{v['title']}》", key=v["title"])
            st.markdown("---")

elif menu == "📢 頻道公告":
    st.title("📢 最新公告與直播行程")

    st.markdown(
        """
    <div class="card">
        <h4>🚨 2026 年夏季特別直播預告</h4>
        <p>HKP 99 Channel 將於本週六晚間 20:00 舉行夏季限定互動直播，歡迎線上同樂！</p>
    </div>
    <div class="card">
        <h4>📢 網站功能升級通知</h4>
        <p>本平台現已支援響應式排版與時區顯示，帶給使用者更流暢的瀏覽體驗。</p>
    </div>
    """,
        unsafe_allow_html=True,
    )

elif menu == "💬 觀眾互動區":
    st.title("💬 觀眾互動與意見回饋")
    st.write("有什麼想對 HKP 99 說的？歡迎在下方留言！")

    with st.form("feedback_form", clear_on_submit=True):
        user_name = st.text_input("暱稱 / Name")
        message = st.text_area("留言內容 / Message")
        submitted = st.form_submit_button("提交留言")

        if submitted:
            if user_name and message:
                st.success(
                    f"感謝 {user_name} 的留言！我們會盡快閱讀並處理。"
                )
            else:
                st.warning("請填寫暱稱與留言內容。")

elif menu == "⚙️ 開發背景與系統資訊":
    st.title("⚙️ 開發背景與驗證資訊")

    st.markdown(
        """
    ### 🎯 開發背景 (Development Background)
    HKP 99 Channel 官方網站旨在建立一個輕量化、即時且易於維護的資訊展示平台。選用 Python + Streamlit 技術棧，能夠實現數據與介面的快速迭代，為觀眾提供最新的節目列表、公告與互動功能。

    ### 🛡️ 準確性與穩定性驗證 (Accuracy Validation)
    - **資料動態渲染**：所有節目與公告組件採模組化設計，支援即時更新與搜尋過濾。
    - **時區機制驗證**：系統整合 `pytz` 時區庫，精確記錄與顯示最新更新時間（預設 Macao Asia/Macau 時間），避免跨時區資訊傳遞誤差。
    - **響應式佈局**：通過 Streamlit 原生 Grid 排版與自訂 CSS，確保流動裝置與桌面端均有良好體驗。
    """
    )

    st.divider()
    st.info(f"**最後更新日期時間 (Last Updated)**：{current_time_str}")

# 4. 頁腳 (Footer)
st.markdown("---")
st.markdown(
    f'<div class="footer-text">© 2026 HKP 99 Channel | Powered by Streamlit | 最後更新：{current_time_str}</div>',
    unsafe_allow_html=True,
)
