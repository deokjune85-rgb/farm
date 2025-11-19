import streamlit as st
import time
import datetime

# ==========================================
# [1. 설정 및 스타일]
# ==========================================
st.set_page_config(
    page_title="청년농부 AI 비서",
    page_icon="🌾",
    layout="centered",
    initial_sidebar_state="collapsed"
)

# CSS 핵: 글자색 강제 검정 & 문서 스타일링
st.markdown("""
<style>
    @import url('https://fonts.googleapis.com/css2?family=Noto+Sans+KR:wght@400;700;900&display=swap');
    html, body, [class*="css"] { font-family: 'Noto Sans KR', sans-serif; }
    
    /* 배경은 연한 회색 */
    .stApp {
        background-color: #f0f2f5;
    }

    /* ★★★ 글자색 강제 검정 (핵심 수정) ★★★ */
    p, div, span, label, h1, h2, h3, h4, h5, h6, td, th, li {
        color: #000000 !important;
    }
    
    /* 입력창 스타일 */
    .stTextInput > div > div > input, .stTextArea > div > div > textarea {
        color: #000000 !important;
        background-color: #ffffff !important;
        border: 1px solid #ccc;
    }

    /* 영농일지 종이 서식 (A4 용지 느낌) */
    .paper-form {
        background-color: white;
        border: 1px solid #000;
        padding: 30px;
        box-shadow: 5px 5px 15px rgba(0,0,0,0.1);
        margin-top: 20px;
        margin-bottom: 20px;
        position: relative;
    }
    
    /* 표 스타일 (공무원 서식) */
    table.doc-table {
        width: 100%;
        border-collapse: collapse;
        margin-top: 15px;
        margin-bottom: 15px;
        border: 1px solid #000;
    }
    table.doc-table th {
        background-color: #e2e8f0;
        border: 1px solid #000;
        padding: 10px;
        text-align: center;
        font-weight: 900;
        font-size: 0.9rem;
        width: 30%;
        vertical-align: middle;
    }
    table.doc-table td {
        border: 1px solid #000;
        padding: 10px;
        font-size: 0.95rem;
        background-color: #fff;
        vertical-align: middle;
    }

    /* 도장 효과 */
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
        z-index: 10;
    }

    /* 지원사업 카드 스타일 */
    .grant-card {
        background-color: #ffffff;
        border: 1px solid #ddd;
        border-left: 5px solid #3b82f6;
        padding: 15px;
        margin-bottom: 15px;
        border-radius: 5px;
        box-shadow: 0 2px 5px rgba(0,0,0,0.05);
    }
    .grant-tag {
        background-color: #eff6ff;
        color: #1e40af !important;
        padding: 3px 8px;
        border-radius: 10px;
        font-size: 0.8rem;
        font-weight: bold;
    }

    /* 버튼 스타일 */
    .stButton > button {
        background-color: #15803d !important;
        color: white !important;
        border: none;
        padding: 15px 0;
        font-size: 1.1rem !important;
        font-weight: bold;
        border-radius: 8px;
        width: 100%;
    }
    .stButton > button:hover {
        background-color: #166534 !important;
    }
    
    /* 탭 스타일 */
    .stTabs [data-baseweb="tab-list"] {
        gap: 10px;
    }
    .stTabs [data-baseweb="tab"] {
        background-color: #fff;
        border-radius: 5px 5px 0 0;
        padding: 10px 20px;
    }
    .stTabs [aria-selected="true"] {
        background-color: #15803d !important;
        color: white !important;
    }
</style>
""", unsafe_allow_html=True)

# ==========================================
# [2. 로직 함수]
# ==========================================

def process_voice_to_log(text):
    """음성 텍스트 -> 구조화된 데이터 변환"""
    today = datetime.date.today().strftime("%Y년 %m월 %d일")
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

def match_grants():
    """지원사업 매칭 데이터 (복구됨)"""
    return [
        {
            "title": "2025년 청년창업농 영농정착지원사업",
            "amount": "월 110만원 (최장 3년)",
            "agency": "농림축산식품부",
            "match": "만 40세 미만 / 독립경영 3년 이하 조건 충족",
            "d_day": "D-12"
        },
        {
            "title": "스마트팜 ICT 융복합 확산사업",
            "amount": "시설 구축비 50% 보조 (최대 2억원)",
            "agency": "지자체/농정원",
            "match": "시설원예(딸기) 재배 농가 대상",
            "d_day": "D-25"
        }
    ]

# ==========================================
# [3. 메인 UI]
# ==========================================

st.markdown("<h2 style='text-align: center; color:#15803d; font-weight:900; margin-bottom:20px;'>🌾 스마트 영농 비서</h2>", unsafe_allow_html=True)

# 탭 구성
tab1, tab2 = st.tabs(["📝 일지 작성 (음성)", "💰 지원사업 매칭"])

# --- [Tab 1] 영농일지 ---
with tab1:
    st.markdown("<h4 style='margin-top:20px;'>🎙️ 음성으로 오늘의 작업을 기록하세요</h4>", unsafe_allow_html=True)
    st.info("💡 마이크 버튼을 누르고 오늘 한 일을 편하게 말씀하세요. AI가 **'관공서 표준 양식'**으로 자동 변환합니다.")
    
    # 음성 입력 시뮬레이션
    voice_input = st.text_area(
        "음성 인식 내용", 
        height=80, 
        value="오늘 아침 6시부터 11시 반까지 2농장에서 딸기 포트 작업했어. 와이프랑 같이 했고 양액 10리터 썼다. 날씨는 맑았어."
    )
    
    if st.button("⚡ AI 문서 변환 및 등록", use_container_width=True):
        with st.spinner("AI가 공문서 양식으로 변환 중입니다..."):
            time.sleep(1.5)
        
        log = process_voice_to_log(voice_input)
        
        # ★★★ HTML 들여쓰기 제거 및 변수 삽입 (코드 노출 방지) ★★★
        html_content = f"""
<div class="paper-form">
<div class="stamp">AI 검증필</div>
<h3 style="text-align:center; text-decoration:underline; margin-bottom:20px; font-weight:900;">영 농 작 업 일 지</h3>
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
"""
        st.markdown(html_content, unsafe_allow_html=True)
        
        col1, col2 = st.columns(2)
        with col1: st.button("🖨️ PDF로 인쇄", key="print")
        with col2: st.button("📲 조합장님께 전송", key="send")

# --- [Tab 2] 지원사업 매칭 ---
with tab2:
    st.markdown("### 💰 김철수님을 위한 '숨은 돈' 찾기")
    st.markdown("""
    <div style='background:#eff6ff; padding:15px; border-radius:10px; margin-bottom:20px;'>
        <strong>📊 김철수님 프로파일링 결과</strong><br>
        • 나이: 만 32세 (청년농)<br>
        • 작목: 시설 딸기 (스마트팜 대상)<br>
        • 지역: 경기도 파주 (접경지역 가산점)
    </div>
    """, unsafe_allow_html=True)
    
    if st.button("🔄 실시간 공고문 스캔하기", use_container_width=True):
        with st.spinner("농림축산식품부, 지자체 공고문을 털고 있습니다..."):
            time.sleep(2)
        
        grants = match_grants()
        st.success(f"총 {len(grants)}건의 맞춤 지원사업을 찾았습니다!")
        
        for grant in grants:
            # 지원금 카드 HTML 구성
            grant_html = f"""
<div class="grant-card">
<div style="display:flex; justify-content:space-between; align-items:start;">
<h4 style="margin:0; color:#1e40af; font-weight:bold;">{grant['title']}</h4>
<span style="color:#ef4444; font-weight:bold;">{grant['d_day']}</span>
</div>
<p style="font-size:1.2rem; font-weight:900; color:#d97706; margin:10px 0;">{grant['amount']}</p>
<div style="margin-bottom:10px;">
<span class="grant-tag">{grant['agency']}</span>
</div>
<p style="font-size:0.9rem; color:#4b5563; background:#f3f4f6; padding:8px; border-radius:5px;">
💡 <strong>AI 매칭 분석:</strong> {grant['match']}
</p>
</div>
"""
            st.markdown(grant_html, unsafe_allow_html=True)
            st.button(f"📝 '{grant['title']}' 사업계획서 자동작성", key=grant['title'])

# 하단 푸터
st.markdown("---")
st.markdown("<div style='text-align:center; font-size:0.8rem; color:#666;'>청년농부조합 전용 솔루션 | Developed by IMD</div>", unsafe_allow_html=True)
