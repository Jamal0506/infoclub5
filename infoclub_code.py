import streamlit as st

# 페이지 설정
st.set_page_config(page_title="암호 방탈출", layout="centered")
st.title("🎉 축제 암호 방탈출")
st.markdown("""
**컨셉:** 축제를 즐기던 중, 이상한 방에 갇히게 되었다.  
남겨진 쪽지를 해독해서 탈출하라!

---
""")

# 단계 상태 저장
if 'stage' not in st.session_state:
    st.session_state.stage = 1

# 1단계
if st.session_state.stage == 1:
    st.subheader("1단계: 이상한 방")
    st.markdown("""
    당신은 축제를 즐기고 있었지만, 정신을 차려보니 낯선 방 안입니다.

    바닥에는 쪽지가 적혀 있습니다:

    `암호를 풀어야 나갈 수 있다. 준비됐는가? 그렇다면 'START'를 입력하라.`
    """)
    answer1 = st.text_input("쪽지에 적힌 암호는?", key="stage1_input")

    if answer1.strip().lower() == "start":
        st.success("정답입니다! 다음 방으로 이동하세요.")
        st.session_state.stage = 2

# 2단계
if st.session_state.stage == 2:
    st.subheader("2단계: 알 수 없는 코드")
    st.markdown("""
    종이에 적힌 암호: `@#*!&`

    힌트: 간단한 치환 암호. 원문은 5글자. 축제를 즐길 때 사용하는 단어.
    """)
    answer2 = st.text_input("원문은 무엇일까요?", key="stage2_input")

    if answer2.strip().lower() == "enjoy":
        st.success("정답입니다! 마지막 방으로 이동하세요.")
        st.session_state.stage = 3

# 3단계
if st.session_state.stage == 3:
    st.subheader("3단계: 고전 암호의 귀환")
    st.markdown("""
    쪽지에 다음과 같이 적혀있습니다:

    - 힌트: `+3`
    - 암호문: `ihvwlYdo`

    (힌트: 알파벳을 각각 왼쪽으로 3칸 이동시키세요. 모두 소문자로 입력)
    """)
    answer3 = st.text_input("암호를 해독해보세요!", key="stage3_input")

    if answer3.strip().lower() == "festival":
        st.success("🎉 축하합니다! 탈출에 성공했습니다!")
        st.balloons()
        if st.button("처음으로 돌아가기"):
            st.session_state.stage = 1
