import streamlit as st

st.set_page_config(layout="wide") # 넓은 화면 설정
st.title("💖 숫자랑 놀아요 🔢")
st.markdown("---")

# 학습할 숫자 리스트
numbers = [1, 2, 3, 4, 5]

# st.tabs를 사용하여 각 숫자에 대한 탭 생성
tabs = st.tabs([f"숫자 {n}" for n in numbers])

# 숫자 3 탭 콘텐츠 예시
with tabs[2]: # 세 번째 탭 (숫자 3)
    st.header("숫자 3")
    st.subheader("이것이 세 개! (개념 연계 활동)")
    
    # 1. 추상적 숫자 기호 강조
    st.markdown("## ✨ **3**", unsafe_allow_html=True)
    
    # 2. 구체적 형태 (3개) 시각화
    # st.columns를 사용해 3개의 이미지를 나란히 배치
    col1, col2, col3 = st.columns(3)
    
    with col1:
        st.image("apple_icon.png", caption="하나") # 실제 이미지 경로로 대체
    with col2:
        st.image("apple_icon.png", caption="둘")
    with col3:
        st.image("apple_icon.png", caption="셋")
        
    st.markdown("---")

    # 3. 간단한 인터랙티브 활동 (정답 맞히기)
    st.subheader("숨겨진 3을 찾아보자! (인터랙션)")
    
    options = [2, 3, 5]
    selection = st.radio(
        "사과가 세 개 있는 것은 무엇일까요?", 
        options,
        horizontal=True
    )
    
    if st.button("정답 확인"):
        if selection == 3:
            st.success("🎉 **맞았어요! 사과 🍎🍎🍎** 세 개!")
        else:
            st.error("앗, 다시 세어볼까요? 🤔")