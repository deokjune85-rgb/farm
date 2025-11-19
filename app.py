import streamlit as st
import time
import datetime

# ==========================================
# [1. 설정 및 스타일] - 문서 서식 & 글자색 강제 고정
# ==========================================
st.set_page_config(
    page_title="청년농부 AI 비서",
    page_icon="🌾",
    layout="centered",
    initial_sidebar_state="collapsed"
)

st.markdown("""
<style>
    @import url('https://fonts.googleapis.com/css2?family=Noto+Sans+KR:wght@400;700;900&display=swap');
    html, body, [class*="css"] { font-family: 'Noto Sans KR', sans-serif; }
    
    /* 메인 배경: 연한 회색 (서류 느낌) */
    .stApp {
        background-color: #f0f2f5;
        color: #000000 !important;
    }

    /* ==============================================
       [NUCLEAR CSS] 글자색 강제 검정 (안 보임 해결)
       ============================================== */
    p, div, span, label, h1, h2, h3, h4, h5, h6, td, th {
        color: #000000 !important;
    }
    .stTextInput > div > div > input {
        color: #000000 !important;
        background-color: #ffffff !important;
    }
    .stTextArea > div > div > textarea {
        color: #000000 !important;
        background-color: #ffffff !important;
    }

    /* ==============================================
       [UI] 진짜 '공문서' 같은 영농일지 스타일
       ============================================== */
    .paper-form {
        background-color: white;
        border: 1px solid #000;
        padding: 30px;
        box-shadow: 5px 5px 15px rgba(0,0,0,0.1);
        margin-top: 20px;
        position: relative;
    }
    
    /* 표 스타일 (공무원 스타일) */
    .doc-table {
        width: 100%;
        border-collapse: collapse;
        margin-top: 15px;
        margin-bottom: 15px;
    }
    .doc-table th {
        background-color: #e2e8f0;
        border: 1px solid #000;
        padding: 10px;
        text-align: center;
        font-weight: 900;
        font-size: 0.95rem;
        width: 30%;
    }
    .doc-table td {
        border: 1px solid #000;
        padding: 10px;
        font-size: 0.95rem;
        background-color: #fff;
    }

    /* 도장 찍힌 효과 */
    .stamp {
        position: absolute;
        top: 20px;
        right: 20px;
        border: 3px solid #cc0000;
        color: #cc0000 !important;
        padding: 5px 10px;
        font-weight: 900;
        font-size: 1.2rem;
        transform: rotate(-15deg);
        border-radius: 5px;
        opacity: 0.8;
    }

    /* 버튼 스타일 */
    .stButton > button {
        background-color: #15803d !important; /* 농협 초록색 */
        color: white !important;
        border: none;
        padding: 15px 0;
        font-size: 1.1rem !important;
        font-weight: bold;
        border-radius: 8px;
    }
    .stButton > button:hover {
        background-color: #166534 !important;
    }
</style>
""", unsafe_allow_html=True)

# ==========================================
# [2. 로직 함수]
# ==========================================

def process_voice_to_log(text):
    """음성 텍스트 -> 구조화된 데이터 변환"""
    today = datetime.date.today().strftime("%Y년 %m월 %d일")
    # 시뮬레이션 결과값
    return {
        "date": today,
        "weather": "맑음 / 기온 24℃",
        "location": "제 2농장 (파주시 탄현면)",
        "crop": "설향 딸기",
        "work": "정식 포트 작업 및 액비 관주",
        "input_mat": "양액 A/B액 10L, 코코피트 배지",
        "hours": "06:00 ~ 11:30 (5.5시간)",
        "worker": "김철수(본인), 이영희(배우자)"
    }

# ==========================================
# [3. 메인 UI]
# ==========================================

st.markdown("<h2 style='text-align: center; border-bottom: 2px solid #15803d; padding-bottom: 10px;'>🌾 스마트 영농일지 시스템</h2>", unsafe_allow_html=True)

# 탭 구성
tab1, tab2 = st.tabs(["📝 일지 작성 (음성)", "📂 내 기록 보관함"])

with tab1:
    st.markdown("<h4 style='margin-top:20px;'>🎙️ 음성으로 오늘의 작업을 기록하세요</h4>", unsafe_allow_html=True)
    st.info("💡 **[사용법]** 마이크 버튼을 누르고 오늘 한 일을 편하게 말씀하세요.\nAI가 **'관공서 제출용 표준 양식'**으로 자동 변환합니다.")
    
    # 음성 입력 시뮬레이션
    voice_input = st.text_area(
        "음성 인식 내용 (예시)", 
        height=80, 
        value="오늘 아침 6시부터 11시 반까지 2농장에서 딸기 포트 작업했어. 와이프랑 같이 했고 양액 10리터 썼다. 날씨는 맑았어."
    )
    
    if st.button("⚡ AI 문서 변환 및 등록", use_container_width=True):
        with st.spinner("AI가 공문서 양식으로 변환 중입니다..."):
            time.sleep(1.5)
        
        log = process_voice_to_log(voice_input)
        
        # 결과 화면: 진짜 종이 서류처럼 보이게 HTML Table 사용
        st.markdown(f"""
        <div class="paper-form">
            <div class="stamp">AI 검증필</div>
            <h3 style="text-align:center; text-decoration:underline; margin-bottom:20px;">영 농 작 업 일 지</h3>
            
            <table class="doc-table">
                <tr>
                    <th>작업 일자</th>
                    <td>{log['date']}</td>
                </tr>
                <tr>
                    <th>기상 / 날씨</th>
                    <td>{log['weather']}</td>
                </tr>
                <tr>
                    <th>작업 장소</th>
                    <td>{log['location']}</td>
                </tr>
                <tr>
                    <th>품 목 (작물)</th>
                    <td>{log['crop']}</td>
                </tr>
                <tr>
                    <th>작 업 내 용</th>
                    <td>{log['work']}</td>
                </tr>
                <tr>
                    <th>투입 자재<br>(비료/농약)</th>
                    <td>{log['input_mat']}</td>
                </tr>
                <tr>
                    <th>작업 시간</th>
                    <td>{log['hours']}</td>
                </tr>
                <tr>
                    <th>작 업 자</th>
                    <td>{log['worker']}</td>
                </tr>
            </table>
            
            <div style="margin-top:20px; text-align:right; font-size:0.9rem;">
                <p>위와 같이 영농 사실을 기록합니다.</p>
                <p><strong>작성자: 김 철 수 (인)</strong></p>
            </div>
            
            <div style="border-top:1px dashed #000; margin-top:20px; padding-top:10px; font-size:0.8rem; color:#333 !important;">
                ※ 본 문서는 직불금 신청 및 GAP 인증 심사 시 증빙 자료로 효력이 있습니다.<br>
                ※ Agrix(농림사업정보시스템) 데이터 표준을 준수합니다.
            </div>
        </div>
        """, unsafe_allow_html=True)
        
        col1, col2 = st.columns(2)
        with col1:
            st.button("🖨️ PDF로 인쇄", key="print_btn", use_container_width=True)
        with col2:
            st.button("📲 조합장님께 전송", key="send_btn", use_container_width=True)

with tab2:
    st.markdown("### 📅 지난 영농 기록")
    st.warning("🔒 유료 회원(조합원) 전용 기능입니다. 지난 3년치 데이터를 엑셀로 다운로드할 수 있습니다.")
