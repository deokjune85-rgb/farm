import streamlit as st
import time
import random
import datetime

# ==========================================
# [1. 설정 및 스타일] - 투박하지만 큰 글씨 (현장용)
# ==========================================
st.set_page_config(
    page_title="청년농부 AI 비서",
    page_icon="🌾",
    layout="mobile" # 모바일 친화적 레이아웃
)

st.markdown("""
<style>
    @import url('https://fonts.googleapis.com/css2?family=Noto+Sans+KR:wght@500;700;900&display=swap');
    html, body, [class*="css"] { font-family: 'Noto Sans KR', sans-serif; }
    
    /* 녹음 버튼 스타일 (크고 누르기 쉽게) */
    .record-btn {
        background-color: #ef4444; /* 빨강 */
        color: white;
        padding: 30px;
        border-radius: 50%;
        font-size: 2rem;
        text-align: center;
        box-shadow: 0 4px 15px rgba(239, 68, 68, 0.4);
        margin: 0 auto;
        display: block;
        width: 100px;
        height: 100px;
        line-height: 40px;
        border: none;
        cursor: pointer;
    }
    
    /* 일지 카드 */
    .log-card {
        background: white;
        border: 2px solid #22c55e;
        border-radius: 10px;
        padding: 20px;
        margin-top: 20px;
    }
    
    /* 지원금 카드 */
    .grant-card {
        background: #eff6ff;
        border-left: 5px solid #3b82f6;
        padding: 15px;
        margin-bottom: 10px;
        border-radius: 5px;
    }
</style>
""", unsafe_allow_html=True)

# ==========================================
# [2. 로직 함수 (시뮬레이션)]
# ==========================================

def process_voice_to_log(text):
    """음성 텍스트를 구조화된 일지 데이터로 변환 (LLM 시뮬레이션)"""
    # 실제로는 GPT-4가 파싱할 부분
    today = datetime.date.today().strftime("%Y-%m-%d")
    
    # 가상의 파싱 결과
    return {
        "date": today,
        "weather": "맑음 (AI 자동수집)",
        "location": "제2농장 (딸기 하우스)",
        "work": "모종 정식 및 관수 작업",
        "input": "복합비료 20kg 1포",
        "hours": "06:00 ~ 11:00 (5시간)",
        "worker": "본인 외 1명"
    }

def match_grants(profile):
    """농부 프로필 기반 지원사업 매칭 (RAG 시뮬레이션)"""
    grants = []
    
    if profile['age'] < 40:
        grants.append({
            "title": "2024 청년후계농 영농정착지원사업",
            "amount": "월 110만원 (최장 3년)",
            "match_reason": "만 40세 미만, 독립경영 3년 이하 조건 충족",
            "deadline": "D-12"
        })
    
    if "딸기" in profile['crop'] or "토마토" in profile['crop']:
        grants.append({
            "title": "스마트팜 ICT 융복합 확산사업",
            "amount": "시설 구축비 50% 보조 (최대 2억원)",
            "match_reason": "시설원예 작물 재배 농가 대상",
            "deadline": "D-25"
        })
        
    grants.append({
        "title": "농업인 안전재해 보험료 지원",
        "amount": "보험료 70% 국비 지원",
        "match_reason": "모든 농업 경영체 등록 농가 대상",
        "deadline": "상시 접수"
    })
    
    return grants

# ==========================================
# [3. 메인 UI]
# ==========================================

st.markdown("<h2 style='text-align: center;'>🌾 김농부님의 AI 비서</h2>", unsafe_allow_html=True)

# 탭 구성
tab1, tab2 = st.tabs(["📝 말로 쓰는 일지", "💰 돈 되는 지원사업"])

# --- 탭 1: 영농일지 ---
with tab1:
    st.markdown("### 🎙️ 오늘의 농사, 말만 하세요")
    st.info("버튼을 누르고 오늘 한 일을 대충 말하면, AI가 관공서 제출용 양식으로 싹 정리해줍니다.")
    
    # 음성 녹음 시뮬레이션 (텍스트 입력으로 대체)
    # 실제 앱에서는 오디오 레코더 위젯 사용
    voice_input = st.text_area("녹음 내용 (예시: 오늘 아침 6시부터 3번 밭에서 고추 따고 물 줬어. 아내는 옆에서 포장했고.)", height=100)
    
    if st.button("🎙️ 음성 변환 및 일지 생성", use_container_width=True):
        if voice_input:
            with st.status("AI가 목소리를 분석 중입니다...", expanded=True) as status:
                time.sleep(1)
                st.write("✅ 음성 인식 완료 (STT)")
                time.sleep(1)
                st.write("✅ 핵심 키워드 추출 (작업, 시간, 투입재)")
                time.sleep(1)
                st.write("✅ 날씨 데이터 자동 연동 (기상청 API)")
                status.update(label="일지 작성 완료!", state="complete", expanded=False)
            
            # 결과 카드
            log = process_voice_to_log(voice_input)
            st.markdown(f"""
            <div class="log-card">
                <h3 style="color: #15803d; margin-top:0;">✅ {log['date']} 영농일지</h3>
                <hr>
                <p><strong>📅 날씨:</strong> {log['weather']}</p>
                <p><strong>📍 장소:</strong> {log['location']}</p>
                <p><strong>🚜 작업내용:</strong> {log['work']}</p>
                <p><strong>💊 투입자재:</strong> {log['input']}</p>
                <p><strong>⏰ 작업시간:</strong> {log['hours']}</p>
                <p><strong>👥 작업자:</strong> {log['worker']}</p>
                <br>
                <div style="text-align:center; color:#666; font-size:0.8rem;">
                    * 이 기록은 직불금 신청 및 GAP 인증 자료로 자동 저장됩니다.
                </div>
            </div>
            """, unsafe_allow_html=True)
            
            col1, col2 = st.columns(2)
            with col1: st.button("🖨️ PDF 출력", use_container_width=True)
            with col2: st.button("📲 조합 전송", use_container_width=True)

# --- 탭 2: 지원사업 매칭 (RAG) ---
with tab2:
    st.markdown("### 💰 김농부님을 위한 '숨은 돈' 찾기")
    st.info("김농부님의 프로필과 정부 공고문 3,400건을 대조하여, **당첨 확률 80% 이상**인 사업만 골라냈습니다.")
    
    # 가상 프로필 (원래는 DB에서 가져옴)
    my_profile = {"age": 32, "crop": "시설 딸기", "area": "1000평"}
    
    if st.button("🔄 실시간 공고문 스캔하기", use_container_width=True):
        with st.spinner("농림축산식품부, 지자체 공고문을 털고 있습니다..."):
            time.sleep(2)
        
        results = match_grants(my_profile)
        
        st.success(f"총 {len(results)}건의 맞춤 지원사업을 찾았습니다!")
        
        for grant in results:
            st.markdown(f"""
            <div class="grant-card">
                <h4 style="margin:0; color:#1e40af;">{grant['title']}</h4>
                <p style="font-size:1.2rem; font-weight:bold; color:#d97706; margin:5px 0;">{grant['amount']}</p>
                <p style="font-size:0.9rem; color:#4b5563;">💡 <strong>매칭 이유:</strong> {grant['match_reason']}</p>
                <div style="display:flex; justify-content:space-between; align-items:center; margin-top:10px;">
                    <span style="color:#ef4444; font-weight:bold;">마감 {grant['deadline']}</span>
                    <button style="background:#2563eb; color:white; border:none; padding:5px 15px; border-radius:5px;">사업계획서 자동작성 ➔</button>
                </div>
            </div>
            """, unsafe_allow_html=True)

# 하단 푸터
st.markdown("---")
st.caption("청년농부조합 전용 솔루션 | 개발: IMD Architecture")
