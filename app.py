import random
import streamlit as st

# 페이지 기본 설정
st.set_page_config(page_title="오늘 뭐 먹지?", page_icon="🍱")

# 앱 제목 및 설명
st.title("🍱 오늘의 점심 메뉴 추천")
st.write("결정 장애 해결! 아래 버튼을 눌러 오늘 먹을 점심을 추천받아 보세요.")

# 추천할 메뉴 리스트 (카테고리, 메뉴명, 이모지)
lunch_menus = [
    ("한식", "김치찌개", "🥘"),
    ("한식", "제육볶음", "🍖"),
    ("한식", "비빔밥", "🥗"),
    ("한식", "순대국밥", "🍲"),
    ("중식", "짜장면", "🍜"),
    ("중식", "짬뽕", "🔥"),
    ("중식", "마라탕", "🌶️"),
    ("일식", "돈까스", "🍛"),
    ("일식", "초밥", "🍣"),
    ("일식", "라멘", "🍥"),
    ("양식", "파스타", "🍝"),
    ("양식", "수제버거", "🍔"),
    ("분식", "떡볶이와 튀김", "🍢"),
    ("아시안", "쌀국수", "🍲"),
]

# 구분선
st.divider()

# 추천 버튼 (가로 전체 너비 사용)
if st.button("🎲 오늘의 점심 메뉴 뽑기!", use_container_width=True):
    # 리스트에서 무작위로 하나 선택
    category, menu, emoji = random.choice(lunch_menus)

    # 결과 출력
    st.balloons()  # 축하 풍선 효과
    st.success(f"오늘의 추천 메뉴는 **[{category}] {menu} {emoji}** 입니다!")
