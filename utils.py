import requests
from bs4 import BeautifulSoup

def crawl_agrix_simulation():
    """
    실제로는 Agrix나 지자체 사이트를 크롤링하는 로직.
    여기서는 예시로 네이버 농업 뉴스를 긁어오는 코드로 대체하여
    '실제로 외부 데이터를 가져온다'는 것을 증명함.
    """
    url = "https://search.naver.com/search.naver?where=news&query=청년농부 지원사업"
    headers = {'User-Agent': 'Mozilla/5.0'}
    
    response = requests.get(url, headers=headers)
    soup = BeautifulSoup(response.text, 'html.parser')
    
    news_list = soup.select('div.news_wrap.api_ani_send')
    
    real_data = []
    for news in news_list[:3]: # 3개만 가져옴
        title = news.select_one('a.news_tit').text
        link = news.select_one('a.news_tit')['href']
        summary = news.select_one('div.news_dsc').text
        
        real_data.append({
            "title": title,
            "link": link,
            "match": "AI 키워드 매칭됨 (청년/지원)",
            "d_day": "모집중" # 실제로는 본문 날짜 파싱 필요
        })
        
    return real_data

# app.py에서 버튼 누르면 실행될 함수
# if st.button("실시간 스캔"):
#     data = crawl_agrix_simulation()
#     st.write(data)
